# SEG-06 H3 生成說明 v07（c 段）

2026-09-30；來源 `brief-v07.md`。A、B 沿用 v04；C 升 v03（v01、v02 保留）。

| 段 | 檔案 | 模式 | 生成 | 正片取用 |
|---|---|---|---|---|
| A | `seg06-a-minimax-h3-prompt-v04.txt` | Ref2VA | 15 秒／362 幀、seed 7601 | 0–14 秒 |
| B | `seg06-b-minimax-h3-prompt-v04.txt` | Ref2VA | 15 秒／362 幀、seed 7601 | 0–10 秒 |
| C | `seg06-c-minimax-h3-prompt-v03.txt` | Ref2VA | 9 秒／217 幀、seed 7601 | 0–7 秒 |

C 上傳順序（`reference-manifest-v07.json`）：ref_image_0＝agent3-drop（`<Picture 1>`）→ ref_image_1＝`assets/software/alotofplacement.png`（`<Picture 2>`，資料牆外觀）→ ref_image_2＝純白房間（`<Picture 3>`）。

## 本版變更（相對 C v02）
- 資料素材：新增 registry 資產 `placement_candidates`（priority 110，角色 data_panel_reference），canonical 描述參考圖的 5×2 縮圖、橘框、灰色板面佈局、橘色高亮零件、run 標題。三面牆各延伸為數十張縮圖；橘 → 翠綠。
- 殘影：移動改為「五個等距逐個變淡的頻閃式複影」；豁然開朗時兩個殘像化為光流衝入本體並消散成火花；第 6 秒結束前明確只剩一個實體 drop，之後每個 beat 都寫單一 drop、乾淨地板。
- 負面表列移除 `no readable text`（參考圖含小字 run 標題，避免相衝）。
- 字數壓縮至 6,974（上限 7000）。

## 驗證（`cast-registry-v07.yaml`）
- C v03：14 通過／0 警告／0 失敗。v07 快照沿用對 Cadi 召喚詞 `robot` 的調整（drop canonical 逐字含 service robot）。
- 根目錄 `cast_registry.yaml` 新增 `placement_candidates` 資產並更新 seg06-c；`assets/ASSET_INDEX.md` 補登參考圖。

## 生成風險
- 模型可能只讓部分縮圖變綠；參考圖小字 run 標題可能生成亂碼。
- 若殘影仍殘留：下一版可把定格殘像拿掉，只保留移動時的頻閃複影，並把收回提前到第 5 秒。

影片未生成。
