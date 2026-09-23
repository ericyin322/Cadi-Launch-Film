# SEG-04 H3 生成說明 v08

2026-09-23；來源 `brief-v05.md`。v07 以前檔案保留。

| 段 | 檔案 | 模式 | 秒數 | 本版變更 |
|---|---|---|---|---|
| A | `seg04-a-minimax-h3-prompt-v03.txt` | T2VA | 10 | 0–1 秒全白＋四周紅橙火焰狀光效；1 秒起紅橙掃光退去（原青色傳送光）；原動作順延為 1–5／5–10 秒 |
| B | `seg04-b-minimax-h3-prompt-v08.txt` | Ref2VA | 8 | Cadi 聲音統一 |
| C | `seg04-c-minimax-h3-prompt-v03.txt` | Ref2VA | 15 | Cadi 聲音統一 |

- Cadi 聲音：`in a bright, playful yet professional childlike Mandarin voice`（逐字）。A 無台詞。
- Cadi 紅焰 canonical 逐字取自根目錄 registry；Picture 2 = `assets/characters/cadi_red.png`。
- 工廠描述 v02（無地名）；流程圖、按鈕、資料光軌的 cyan 屬介面／工廠色，未改。
- 上傳順序見 `reference-manifest-v08.json`；registry 快照 `cast-registry-v08.yaml`。Picture 3 流程圖仍待提供。
- 時長：A10＋B8＋C15＝33 秒（原排程 24 秒），全片校時仍待處理。

## 驗證（check_prompt.py，cast-registry-v08.yaml）

- B：14 passed／0 warn／0 fail（6946 字元）
- C：14 passed／0 warn／0 fail（6993 字元）
- A：5 passed／2 warn／2 fail。FAIL 為檢查器以 Ref2VA 區段與 362 幀（15 秒）假設檢查 T2VA 的既有限制（v02 同樣 3 fail）；A 為 10 秒 T2VA，實際生成請設 10 秒。
