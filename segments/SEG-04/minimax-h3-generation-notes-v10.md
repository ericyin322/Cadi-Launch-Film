# SEG-04 H3 生成說明 v10

2026-09-23；依使用者指示 A 改為 Ref2VA，沿用 B 的角色參考圖。B v08、C v03 不變；舊版保留。

| 段 | 檔案 | 模式 | 生成 | 正片取用 |
|---|---|---|---|---|
| A | `seg04-a-minimax-h3-prompt-v05.txt` | Ref2VA | 15 秒／362 幀、seed 7401 | 0–10.0 秒 |
| B | `seg04-b-minimax-h3-prompt-v08.txt` | Ref2VA | 8 秒 | 0–8 秒 |
| C | `seg04-c-minimax-h3-prompt-v03.txt` | Ref2VA | 15 秒 | 0–15 秒 |

## A 上傳順序

1. `<Picture 1>`／`ref_image_0`：`assets/characters/heroine-photo-reference-v01.png`
2. `<Picture 2>`／`ref_image_1`：`assets/characters/cadi_red.png`

B 的 Picture 3 流程圖不在 A 出場，依 Absent Objects 規則不上傳、不編索引。工廠仍為純文字。

## A v05 內容

- 六區段格式（同 B）：subject_definitions／summary／retention_analysis／detailed_description／overall_soundscape／non_diegetic_music；canonical 逐字取 registry。
- 時間段：0–1 全白＋四周紅橙火焰狀光效｜1–5 紅橙掃光退去、工廠揭示、Cadi 飛出｜5–10 環繞、響指、躺椅／遮陽傘／飲料依序出現、女主坐下｜10–12 鏡頭停穩、Cadi 抬手｜12–15 穩定停留（緩衝）。
- 角色 retention 標註自 1 秒起（0–1 秒為全白畫面）。

## 驗證

`check_prompt.py`（cast-registry-v10.yaml）：A 13 passed／0 warn／0 fail（6948 字元）；B、C 各 14 passed／0 fail。影片未生成。
