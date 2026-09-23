# SEG-06 H3 生成說明 v04

2026-09-23；來源 `brief-v04.md`／`screenplay/master-storyboard-v0.24.md`。使用者直接要求（Storyboard v02 已過時）。v03 保留。

| 段 | 檔案 | 模式 | 生成 | 正片取用 |
|---|---|---|---|---|
| A | `seg06-a-minimax-h3-prompt-v04.txt` | Ref2VA | 15 秒／362 幀、seed 7601 | 0–14 秒 |
| B | `seg06-b-minimax-h3-prompt-v04.txt` | Ref2VA | 15 秒／362 幀、seed 7601 | 0–10 秒 |

上傳順序（`reference-manifest-v04.json`）：A＝cadi_red → agent3-drop → agent2-hapa → agent1-hana → 純白房間；B＝cadi_red → agent3-drop → 純白房間。

## 本版變更（相對 v03）
- 場景：工廠街區站點改為純白房間（實際上傳）；移除工作台／櫃檯，資料全程浮空，Spec 在 drop 畫面左側、GP 在右側，銜接 SEG-07 A v07。
- A 開場：Cadi 背後跟拍高速前飛，一開始即處於白／淡銀殘影光軌中，0–2 秒快速閃換後定格為純白房間。不使用工廠文字描述。
- hapa／hana 由畫面左緣外飛入、交付後由左緣飛離（房間無門）。
- Cadi 紅焰（根目錄 canonical）；Cadi 台詞聲音逐字「in a bright, playful yet professional childlike Mandarin voice」（B 首句，後續句為 in the same voice）。
- 燈光描述改為室內（hapa／hana／drop retention 的 district lighting → indoor lighting）。
- 時長：A 15（原 15）、B 15（原 9）；尾段為停留緩衝，正片合計 24 秒不變。台詞 DLG-14–17 逐字不變。

## 驗證（check_prompt.py，`cast-registry-v04.yaml`）
- A：16 passed／1 warn（五圖軟警告）／0 fail（6969 字元）
- B：14 passed／0 warn／0 fail（6951 字元）
- 另以根目錄 registry 所有資產 summon_tokens 掃描，兩段皆無未出場物件字眼。

影片未生成。
