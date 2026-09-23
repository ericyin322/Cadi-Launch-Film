# SEG-05 H3 生成說明 v06

2026-09-23；來源 `brief-v04.md`／`screenplay/master-storyboard-v0.23.md`。使用者直接要求更新 H3（Storyboard v02 仍過時）。v05 保留。

| 段 | 檔案 | 模式 | 生成 | 正片取用 |
|---|---|---|---|---|
| A | `seg05-a-minimax-h3-prompt-v06.txt` | Ref2VA | 15 秒／362 幀、seed 7501 | 0–14 秒 |
| B | `seg05-b-minimax-h3-prompt-v06.txt` | Ref2VA | 15 秒／362 幀、seed 7501 | 0–12 秒 |

上傳順序同 v05（見 `reference-manifest-v06.json`）：A＝cadi_red → agent2-hapa；B＝cadi_red → agent1-hana。

## 本版變更（相對 v05）

- A：hapa 不再預先在場。[Shot 2] 先建立左側掛 SPEC／HTTP 直式招牌的多層工坊建築；4–7 秒 Cadi 揮手，建築開口亮起，hapa 飛出並懸停在他面前，同時 Cadi 開始說話。
- A：DLG-10 後半改為「正確資訊標綠，更動資訊標黃。」
- B：hana 不再預先在場。[Shot 1] 先建立右側掛 GP 辨識直式招牌的建築；0–2 秒 Cadi 揮手，建築開口亮起，hana 飛出並懸停在航道入口面向他。
- B 為控制在 7000 字元內，精簡場景方位句、一句配樂提示與 hana 飄帶描述；動作、台詞、時間軸不變。
- 其餘（紅焰 Cadi、聲音統一句、工廠 v02、環境音效、15 秒緩衝）同 v05。

## 驗證（check_prompt.py，`cast-registry-v06.yaml`）

- A：13 passed／0 warn／0 fail（6786 字元）
- B：13 passed／0 warn／0 fail（6975 字元）

影片未生成。
