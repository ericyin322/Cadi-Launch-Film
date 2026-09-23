# SEG-04 H3 生成說明 v09

2026-09-23；依使用者要求將 A 改依最新規則撰寫。B v08、C v03 不變；v08 以前檔案保留。

| 段 | 檔案 | 模式 | 生成 | 正片取用 |
|---|---|---|---|---|
| A | `seg04-a-minimax-h3-prompt-v04.txt` | T2VA | 15 秒／362 幀、seed 7401 | 0–10.0 秒 |
| B | `seg04-b-minimax-h3-prompt-v08.txt` | Ref2VA | 8 秒 | 0–8 秒 |
| C | `seg04-c-minimax-h3-prompt-v03.txt` | Ref2VA | 15 秒 | 0–15 秒 |

## A v04 變更

- 補齊 integrated 格式區段：`subject_definitions`、`retention_analysis`、`integrated_multimodal_description`、`overall_soundscape`、`non_diegetic_music`。
- 女主角與 Cadi 以根目錄 registry canonical 逐字定義，retention 逐字取 registry；純文字模式，不上傳圖片、不使用 Picture／Subject 標籤。
- 畫風 `project.visual_style` 逐字放在 [Shot 1] 開頭，接工廠描述 v02。
- 依 15 秒／362 幀生成規則改為 5 個時間段：0–1 全白＋四周紅橙火焰狀光效｜1–5 紅橙掃光退去、工廠揭示、Cadi 飛出｜5–10 環繞、響指、躺椅／遮陽傘／飲料依序出現、女主坐下｜10–12 鏡頭停穩、Cadi 雙手抬到胸前準備展示｜12–15 穩定構圖停留（剪輯緩衝，銜接 B 開頭展開雙手）。
- 移除內文「ten-second」秒數字樣；新增 `Negative constraints:` 區塊並加入 Cadi 專屬負面詞。

## 驗證（check_prompt.py，cast-registry-v09.yaml）

- A：8 passed／2 warn／0 fail（6725 字元）。警告為 (1) 純文字模式無 Picture 標籤（預期）；(2) `no solid glass surface` 為 registry 規定的 Cadi 專屬負面詞，B、C 同樣使用，保留。
- B、C：各 14 passed／0 warn／0 fail。
- 影片未生成。SEG-04 正片 A10＋B8＋C15＝33 秒，全片校時待處理。
