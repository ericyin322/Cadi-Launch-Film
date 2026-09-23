# SEG-05 H3 生成說明 v05

2026-09-23；來源 `brief-v03.md`／`screenplay/master-storyboard-v0.22.md`。使用者直接要求本版 H3，授權略過已過時的 Storyboard v02。v04 以前檔案保留。

| 段 | 檔案 | 模式 | 生成 | 正片取用 |
|---|---|---|---|---|
| A | `seg05-a-minimax-h3-prompt-v05.txt` | Ref2VA | 15 秒／362 幀、seed 7501 | 0–14 秒 |
| B | `seg05-b-minimax-h3-prompt-v05.txt` | Ref2VA | 15 秒／362 幀、seed 7501 | 0–12 秒 |

正片合計 26 秒，符合原時槽。A 14–15 秒、B 12–15 秒為穩定停留緩衝，不進正片。

## 上傳順序

- A：`ref_image_0`＝`assets/characters/cadi_red.png`（Picture 1）；`ref_image_1`＝`assets/characters/agent2-hapa.png`（Picture 2）
- B：`ref_image_0`＝`assets/characters/cadi_red.png`（Picture 1）；`ref_image_1`＝`assets/characters/agent1-hana.png`（Picture 2）

## 本版變更（相對 v04）

- Cadi 全段紅焰：canonical／retention 逐字取根目錄 registry；只正向描述紅焰，不提舊色。
- Cadi 聲音逐字統一為 `in a bright, playful yet professional childlike Mandarin voice`；接續句寫「in the same voice」。hapa、hana 聲音沿用 v04。
- 工廠描述改用 v02（移除地名）。
- 改為 15 秒生成加尾段停留緩衝（A 14–15、B 12–15 秒）；其餘時間軸、台詞、動作不變。
- 聲音設計保留環境音效（工廠底噪、落地聲、飛行 whoosh），B 尾段航道氣流延續到 SEG-06 起飛聲橋。
- 女主角不出場：Cadi canonical 刪去「以女主角上半身為基準的身高」一句，避免召喚女主角（Absent Objects；分段 registry 快照已同步）。

## 驗證（check_prompt.py，`cast-registry-v05.yaml`）

- A：13 passed／0 warn／0 fail（6595 字元）
- B：13 passed／0 warn／0 fail（6985 字元）

影片未生成。
