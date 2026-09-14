---
name: h3-scene-prompt
description: 為 MiniMax-H3 參考圖生影片（Ref2VA）模式產生分段 prompt。當使用者提到要把故事劇本、分鏡、場景拆成 H3 影片 prompt，或提到「每個場景 30 秒」「分段生成」「角色參考圖」「Picture 1 / Picture 2 綁定」「Cadi」「seg0X prompt」「參考圖要掛哪幾張」等情境時，務必觸發此 skill。也適用於檢查既有 H3 prompt 的參考圖綁定是否正確、跨段角色是否會漂移、單段長度是否落在合法 frame grid 上。此 skill 負責 prompt 的產生與驗證，不負責實際算圖。
---

# H3 分段 Prompt 產生器

把一份多場景劇本，轉成一組可以直接餵進 MiniMax-H3 Ref2VA 的分段 prompt，
並保證跨段的角色身份、參考圖綁定、時間軸不會漂移。

核心難點只有一個：**索引是「每一段自己的區域索引」，不是全域角色 ID。**
`<Picture N>` 對應 ComfyUI 節點的第 N 個 `ref_image` 插槽，也就是上傳順序；
`<Subject N>` 是從那張圖抽出來的身份，兩者配對使用：

```
<Subject 1> is <角色描述>. Her face, hair, and clothing follow <Picture 1>.
```

同一個 Cadi，在只有他出場的那段是 `<Subject 1>/<Picture 1>`，
在他和女主角同框那段是 `<Subject 2>/<Picture 2>`。
編號和上傳順序錯開，模型就會把女主角的臉貼到機器人身上。
這個 skill 的一半篇幅都在防這件事。

## 開工前必須先拿到的三樣東西

沒有這三樣就先問使用者，不要自己編：

1. **劇本**：每個場景的敘事內容、出場角色、地點。
2. **資產清單**：每張參考圖的檔案路徑，以及它代表誰／什麼。
3. **每個角色的 canonical description**：一段固定的英文外觀描述。
   這段字串之後會**逐字**出現在每一段 prompt 裡，是跨段一致性的主要來源。
   如果使用者沒有，從既有的 prompt（例如 seg04）裡抄出來，請他確認。

把這三樣寫進 `cast_registry.yaml`（範本在 `assets/cast_registry.template.yaml`）。
這份檔案是整個專案的單一事實來源，後續每一段都從它推導。

## 流程

### 步驟 1：把場景切成段

H3 單段上限是 362 frames = **15.083 秒**（frame 必須落在 `17n+5` 的格子上，24fps）。
所以 30 秒的場景 = 2 段，45 秒 = 3 段。合法長度換算表在 `references/h3-constraints.md`。

切點選在**動作的自然停頓**，不要切在動作中途。好的切點：角色停下腳步、轉頭、
鏡頭停止移動、一個道具剛落定。壞的切點：跳躍到一半、正在說話、鏡頭橫搖中。
理由很實際——B 段的開頭必須用文字重建 A 段結尾的狀態，靜止的狀態比運動中的狀態好描述得多。

### 步驟 2：決定每段的 cast，排出綁定表

列出這一段實際出場的資產，然後按**固定優先序**指派區域索引：

```
1. 女主角（若出場）
2. Cadi（若出場）
3. 其他角色 —— 依劇本首次出場順序
4. 場景／環境參考圖
5. 道具、風格參考圖
```

優先序固定，索引就能從 cast 清單機械推導出來，不需要判斷。範例：

| 場景 | 出場 | 綁定（= ref_image 上傳順序）|
|---|---|---|
| S01 | 只有女主角 | 1 = 女主角 |
| S02 | 只有 Cadi | 1 = Cadi |
| S03 | 女主角 + Cadi | 1 = 女主角，2 = Cadi |
| S04 | 女主角 + Cadi + 工廠 | 1 = 女主角，2 = Cadi，3 = 工廠 |
| S05 | Cadi + 新角色老工程師 | 1 = Cadi，2 = 老工程師 |

注意 S02 和 S05 的 Cadi 都是索引 1，S03/S04 的 Cadi 是索引 2。這是對的，不是 bug。
索引 N 同時決定 `<Subject N>`、`<Picture N>` 和節點上的 `ref_image_{N-1}` 插槽，三者必須一致。

**只掛這一段真正需要的圖。** 多掛一張沒出場的角色圖不是保險，是干擾——模型會試圖把
那個角色塞進畫面。上限是 9 張圖，但實務上一段超過 4 張，身份鎖定就開始鬆動。

### 步驟 3：寫 prompt

用 `assets/segment_prompt.template.txt` 的骨架。六個區段，順序固定：

```
subject_definitions:      每個 <Subject N> 是誰、跟哪張 <Picture N> —— canonical description 逐字抄
summary:                  以 [reference generation] 開頭，一到兩句話講這段發生什麼
retention_analysis:       每個 <Subject N> 有哪些特徵必須從 <Picture N> 保留
detailed_description:     主體。帶時間碼的動作時間軸 + 鏡頭 + 負面表列
overall_soundscape:       環境音、動作音、對白
non_diegetic_music:       配樂；沒有就寫 N/A
```

`detailed_description` 內部要有 **5–6 個時間碼 beat**，用 `0:03` 或 `[5s-8s]` 標記。
15 秒只給 2–3 個動作，模型後半段會停滯或循環——這是實測過最常見的失敗模式。
每 2–3 秒推進一個新動作。

全文用英文寫（模型的訓練分布），上限 7000 字元。

### 步驟 4：跑驗證

```bash
python scripts/check_prompt.py <prompt.txt> --registry cast_registry.yaml --segment S03a
```

會檢查：Subject/Picture 是否配對、索引連續無跳號、body 用到的每個索引都在 subject_definitions 宣告過、
綁定和 registry 一致、六個區段齊全且順序正確、字元數、canonical description 是否被改寫。
最後一項特別重要——agent 很容易「順手潤飾」角色描述，那正是跨段漂移的起點。

### 步驟 5：輸出 manifest

每段除了 prompt 檔，還要在 `manifest.csv` 追加一行，給執行算圖的人：

```csv
segment,scene,frames,seconds,seed,ref_order
S03a,3,362,15.083,7301,"heroine.png|cadi.png"
```

`ref_order` 的順序就是上傳順序，必須和 `<Picture 1..N>` 對齊。**這是最容易在交接時出錯的地方**——
prompt 寫得再對，上傳順序反了就全毀。

## 跨段一致性

這是整個工作流真正的難關。H3 的 Ref2VA **不能同時吃參考圖和首尾幀**，
所以 A 段的結尾畫面沒辦法直接傳給 B 段。兩種做法，各有代價：

**做法 A —— 純文字接續（兩段都走 Ref2VA）**

B 段的 `detailed_description` 開頭寫一段 state anchor，重建 A 段結尾的狀態：

```
Continuing without a cut from the previous shot: the engineer <Picture 1> is already
seated in the lounge chair, her right hand resting near the drink, shoulders relaxed.
Cadi <Picture 2> hovers at her front-left at chest height. The camera is at her
front-right, 35mm, static. Same late-afternoon cyan key light from the left.
```

要寫的四件事：**位置與姿勢、鏡頭機位與焦段、光線方向、上一段末尾的情緒狀態**。
同場景的兩段用**同一個 seed**。
優點是 B 段仍受參考圖約束；缺點是構圖會有可見的接縫。

**做法 B —— 鏈式（A 段 Ref2VA，B 段改走 I2VA 吃 A 的尾幀）**

身份靠像素延續，接縫幾乎看不見。缺點是 B 段失去參考圖約束，角色會隨著鏈條慢慢漂移，
而且 B 段要換 checkpoint 和 workflow。

**預設用做法 A**，除非該場景有明顯的連續動作橫跨 15 秒邊界。理由是 26 段的專案裡，
身份漂移累積起來比構圖接縫更難補救——接縫可以在剪輯時用轉場蓋掉，臉變了不行。

## 反覆出現的錯誤

- **索引跳號**：`<Picture 1>` 和 `<Picture 3>` 但沒有 `<Picture 2>`。會和 ref_image 插槽錯位。必須連續。
- **有 Subject 沒有 Picture**：身份沒綁到任何參考圖插槽，模型會自己編一個人。
- **潤飾 canonical description**：第 7 段把 "taupe-gray blazer" 寫成 "grayish-brown blazer"。
  逐字複製，不要改善措辭。
- **掛了沒出場的角色圖**：模型會硬把他塞進畫面。
- **negative 表列漏掉**：每段結尾都要有。共用樣板在 template 裡，再依該段風險追加
  （例如 Cadi 出場的段落一定要加 `no jelly or gelatinous head texture`）。
- **忘記 non_diegetic_music**：沒有配樂就明確寫 `None.`，留空模型會自己加。
- **提到秒數卻寫錯**：prompt 內文若寫 "the entire fifteen-second shot"，要和實際 362 frames
  一致。寫 "nine-second" 卻算 15 秒會讓模型壓縮節奏。

## 已定案的兩個格式決定

這兩件事原本待驗證，後來由 ComfyUI node pack 內建的契約文字確認：

1. **`<Subject N>` 和 `<Picture N>` 配對使用**，不是二選一。
   `<Picture N>` = 第 N 個 `ref_image` 插槽（上傳順序），`<Subject N>` = 從該圖抽出的身份。
   標準綁定句：`<Subject 1> is <描述>. Her face, hair, and clothing follow <Picture 1>.`
   只寫 `<Picture N>` 而沒有 `<Subject N>` 仍能出圖，但身份鎖定較弱。
2. **六區段，主體區段叫 `detailed_description`**（不是 base 模式的
   `integrated_multimodal_description`），且 `non_diegetic_music` 的空值寫法是 `N/A`。

registry 的 `label_style` / `section_style` 開關保留，以便日後換 node pack 時切換。

## 參考檔案

- `references/h3-constraints.md` —— frame grid 換算表、參考檔數量上限、各模式差異、比例限制
- `assets/cast_registry.template.yaml` —— 資產登記表範本
- `assets/segment_prompt.template.txt` —— 單段 prompt 骨架
- `scripts/check_prompt.py` —— 驗證器
