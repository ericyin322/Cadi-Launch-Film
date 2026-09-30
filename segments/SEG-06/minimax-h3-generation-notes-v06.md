# SEG-06 H3 生成說明 v06（c 段改版）

2026-09-30；來源 `brief-v06.md`。A、B 沿用 v04；C 由 v01 升 v02（v01 保留）。

| 段 | 檔案 | 模式 | 生成 | 正片取用 |
|---|---|---|---|---|
| A | `seg06-a-minimax-h3-prompt-v04.txt` | Ref2VA | 15 秒／362 幀、seed 7601 | 0–14 秒 |
| B | `seg06-b-minimax-h3-prompt-v04.txt` | Ref2VA | 15 秒／362 幀、seed 7601 | 0–10 秒 |
| C | `seg06-c-minimax-h3-prompt-v02.txt` | Ref2VA | 9 秒／217 幀、seed 7601 | 0–7 秒 |

C 上傳順序（`reference-manifest-v06.json`）：ref_image_0＝agent3-drop（`<Picture 1>`）→ ref_image_1＝純白房間（`<Picture 2>`）。資料面板不上傳圖，僅以文字描述（皆為抽象標記、無可讀文字）。

## 本版變更（相對 C v01）
- 由 drop 原地擺姿勢改為在三面資料面板間高速滑步；殘影由移動拖出並在 A／B 前留定格殘像，豁然開朗時收回。
- 新增三面抽象面板與顏色語意：琥珀黃標記 → 翠綠（自左向右掃過）。
- 鏡位由腰部以上中近景改為全身中廣角，固定機位。
- 生成 8 → 9 秒、取用 0–6 → 0–7 秒。
- 動作：A 思考、B 搖頭、C 托腮停一秒、豁然開朗；不再有抓頭與跳起。

## 驗證（`cast-registry-v06.yaml`）
- C v02：13 通過／0 警告／0 失敗（6,724 字元）。v06 快照沿用 v05 對 Cadi 召喚詞 `robot` 的調整（drop canonical 逐字含 service robot）。

## 生成風險
- 「資料全部轉綠」可能被模型只做局部變色；若出現，可在 6–7 秒加強「every mark on all three panels」。
- 面板可能出現亂碼文字；已用 no readable text 壓制，並將內容限定為抽象標記。

影片未生成。
