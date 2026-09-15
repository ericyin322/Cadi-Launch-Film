# SEG-02 MiniMax H3 生成說明 v07

## 最新提示詞與參考圖

| 分段 | 提示詞 | 唯一上傳圖片（ref_image_0／Picture 1） | 正片取用 |
|---|---|---|---|
| A | `seg02-a-minimax-h3-prompt-v06.txt` | `assets/characters/heroine-photo-reference-v01.png` | 前 9 秒 |
| B | `seg02-b-minimax-h3-prompt-v07.txt` | `assets/software/teams-ui-reference-v01.png`（檔案尚缺） | 前 12 秒 |

使用專案既有 Ref2VA 與 `<Picture N>`／`<Subject N>` 配對語法。兩段各沿用 362 幀、seed 7201、16:9；提示詞敘述至 15 秒，其餘為生成尾端。這是專案既有設定，未另行驗證目前安裝節點的版本限制。

## 本次確認的規則

- 已閱讀專案 H3 skill、其 full-reference 指南，以及 minimaxh3-prompt-guide 與 prompt-patterns。
- 劇情只取 `screenplay/master-storyboard-v0.7.md` 鏡頭 05–08；保留 9＋12 秒、郵件及三則訊息原文。
- `detailed_description` 開頭逐字使用 registry 的 `project.visual_style`，角色／介面 canonical 亦逐字保留。
- A 只綁女主角寫實圖；B 只綁 Teams UI。未出場資產不宣告、不上傳、不保留索引。
- 提示詞六區段使用英文，畫面文字維持原繁體中文；剪輯、上傳與驗收說明僅放本文件。
- 新 Storyboard v03 尚未製作／確認；依使用者本次直接要求重製提示詞，未更動其確認狀態。

## 銜接與聲音

- A：0–4 秒手錶亮起震動與皺眉；4–9 秒掏手機、亮屏解鎖。鏡頭緩慢繞至左肩旁，9 秒接到已亮起且顯示通知卡的手機。9–15 秒是備用尾段，正片不採用。
- B：開頭通知卡已就位，先穩定顯示「RF需求變更需求」「半小時後開會」；4.6 秒點 Teams，5 秒依手機介面位置切滿版 UI。三則訊息於 5／7／9 秒出現並持續保留；10.5 秒起腳步聲提前銜接下一段。12–15 秒是備用尾段。
- A 第 1 秒震動帶入低鼓；兩段維持 72 BPM、D 小調、低鼓／低 tom／次低音漸強。實際剪接應以 A 第 9 秒接 B 第 0 秒校對畫面及音樂，固定 seed 無法保證逐幀或音訊相位一致。
- 滿版 UI 期間以腳步聲銜接；收手機與攜帶筆電沿用文字分鏡的畫外連續性，不另增鏡頭。

## 驗證與待辦

- A v06：5151 字元，12 passed／0 warnings／0 failed。
- B v07：5081 字元，12 passed／0 warnings／0 failed。
- 已確認女主角圖存在；Teams 圖尚缺，因此 B 的文字結構通過不代表素材已齊。補圖後須確認版面符合 registry 定義。
- 影片及音樂尚未生成。生成後需逐字驗收郵件、標題及三則群組訊息；錯字可於滿版 UI 鏡頭以後製文字修正。
- 歷史索引曾指向 A v05／B v06，但本次檢查未找到實體檔。直接遞增為 A v06／B v07，不補寫或覆蓋歷史版本。
