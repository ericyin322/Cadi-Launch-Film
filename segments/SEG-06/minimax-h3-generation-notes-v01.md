# SEG-06｜H3 生成說明 v01

依 `brief-v02.md` 與 `storyboard-v02.png` 製作；使用者看過新版後直接要求生成 H3，據此進入提示詞製作。未額外宣稱圖像已正式驗收。使用 h3-prompt-writing，並參照 minimaxh3-prompt-guide 的媒體綁定及連續性規則。影片尚未生成。

## 可直接使用的提示詞

| 檔案 | 規劃時長 | 劇情範圍 |
|---|---:|---|
| `seg06-a-minimax-h3-prompt-v01.txt` | 15秒 | 抵達站點、揮手招呼、hapa交付Spec、hana交付GP、兩者飛離 |
| `seg06-b-minimax-h3-prompt-v01.txt` | 9秒 | Cadi交代彙整原則、drop回應並開始交叉驗證 |

合計24秒，沿用原時槽01:56–02:20。15＋9秒為本次製作安排，未經配音實測；交付與回報同步進行。招呼僅揮手，未新增台詞。原 DLG-14–17 完整保留，DLG-16 稱呼沿用已授權的 drop。

## 圖片上傳順序

兩段採專案既定 Ref2VA `<Picture N>` 語法、16:9、seed 7601。

| 插槽／標籤 | A | B |
|---|---|---|
| ref_image_0／Picture 1 | `assets/characters/cadi Design Sheet.jpg` | 同左 |
| ref_image_1／Picture 2 | `assets/characters/agent3-drop.png` | 同左 |
| ref_image_2／Picture 3 | `assets/characters/agent2-hapa.png` | 不掛圖、不編索引 |
| ref_image_3／Picture 4 | `assets/characters/agent1-hana.png` | 不掛圖、不編索引 |

每張圖僅提供對應角色身分、比例及配色。場景採文字建構；不掛黑白 Storyboard、畫風參考、女主角或其他未出場素材。模型提示詞不含以上排除說明。Cadi 身分逐字沿用 SEG-05 本段 registry 的版本，避免身高比較句帶入未出場角色；主 registry 其他角色描述不變。

drop 身分依指定圖新建：實體白色水滴頭、藍眼、白色裝甲、黑色關節、藍色水滴胸核。與 Cadi 持續燃燒的非固體青藍電漿頭明確區分。成片畫風逐字取自主 registry 的 `project.visual_style`，全彩寫實電影質感。

## 時間與銜接

- A 0–1.5秒：承接 SEG-05B 背後視角與前傾姿態，直飛站點。
- A 1.5–3秒：Cadi、drop 揮手；3–4秒：hapa、hana 返回。
- A 4–10秒：hapa 完整回報並交付 Spec；10–13.5秒：hana 完整回報並交付 GP。
- A 13.5–15秒：兩位 Agent 空手飛離，資料留在 drop 工作檯；Cadi 左、drop 右，Spec 左、GP 右。
- B 0–6秒：完整彙整指示，拆入四個連續節點；6–8秒：drop 回應；8–9秒：比對資料。

A 尾、B 首維持相同站點、鏡頭側、光線方向、角色位置與資料配置；B 從已交接完成的狀態繼續。採穩定中景接續，沒有宣称只靠 seed 即可鎖定逐幀一致。生成後檢視 A 尾畫面：若需首幀錨定，將實際解碼尾幀接入支援的 `first_frame` 輸入，不追加成身分用 Picture 槽；使用帶重疊的 guide 時另依實際輸出裁切，維持淨長24秒。本次未提供影片或尾幀，未虛設 Video／Audio 參考。

聲音沿用 SEG-05 的112 BPM輕快器樂、低街區底聲、飛行與機械動作聲，對白時壓低配樂。A與B接縫保留一條連續音樂底，依生成結果剪接及短交叉淡化。drop 聲音設為清楚平穩、帶輕微電子共鳴；此為製作聲音安排，非既有聲音素材。

依實際節點設定15秒／9秒；manifest 的 frames 欄留空，避免將固定362幀誤套到9秒。節點幀數與可選時長以實際工作流為準。

## 驗證

本段使用 `cast-registry-v01.yaml` 驗證；主 registry 的 SEG-06 條目以 `prompt_registry` 指向此檔。

- A：14 passed、1 warning、0 failed；6891字元。
- B：12 passed、1 warning、0 failed；5877字元。
- 兩個 warning 均來自檢查器只辨識整數 beat，漏算含1.5／4.5／13.5秒的標記。另用支援小數的檢查逐段確認六個 beat 相接、無重疊或空隙，完整覆蓋15秒／9秒。
- 另外核對四句對白逐字一致、四張素材路徑存在、A／B上傳索引連續、B不含hana／hapa、主registry畫風逐字一致。
- 語速、角色飛離是否完成、口型、資料交付及A／B畫面連續性仍須成片驗收。
