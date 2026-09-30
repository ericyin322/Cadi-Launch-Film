# SEG-06 H3 生成說明 v05（新增 c 段）

2026-09-30；來源 `brief-v05.md`。A、B 沿用 v04 提示詞不變；新增 C。

| 段 | 檔案 | 模式 | 生成 | 正片取用 |
|---|---|---|---|---|
| A | `seg06-a-minimax-h3-prompt-v04.txt` | Ref2VA | 15 秒／362 幀、seed 7601 | 0–14 秒 |
| B | `seg06-b-minimax-h3-prompt-v04.txt` | Ref2VA | 15 秒／362 幀、seed 7601 | 0–10 秒 |
| C | `seg06-c-minimax-h3-prompt-v01.txt` | Ref2VA | 8 秒／193 幀、seed 7601 | 0–6 秒 |

C 上傳順序（`reference-manifest-v05.json`）：ref_image_0＝agent3-drop（`<Picture 1>`）→ ref_image_1＝純白房間（`<Picture 2>`）。Cadi、hapa、hana 不上傳、不提。

## 設計說明
- 單人特寫：固定機位、腰部以上中近景；背景為景深虛化的純白牆與地板反光。
- 殘像採「定格殘像疊加」：每個動作完成後留下半透明淡藍白光邊的同姿勢殘像停在空中（左、右、左上、右上），第 5–6 秒全部收回本體。
- 節奏：每個動作約 1 秒（動作本身瞬間卡位、四肢帶輕微動態模糊）；檢查器只接受整數秒 beat，故以 `[1s-2s]` 等整數區間表示。
- 無台詞、無 Cadi 聲音；聲音為運算聲／伺服／殘像玻璃音，配樂與 B 同為 112 BPM。

## 驗證（`cast-registry-v05.yaml`）
- A：16 通過／1 警告（五圖）／0 失敗；B：14 通過／0 警告／0 失敗；C：13 通過／0 警告／0 失敗（6,1xx 字元）。
- **registry v05 快照調整**：Cadi 的 summon_tokens 移除通用詞 `robot`。drop 的 canonical 逐字含 "service robot"，單人 drop 段不可能避開；其餘 Cadi 召喚字眼（cadi、mascot、plasma、flame head、chest core）仍檢查，C 內皆無。根目錄 registry 與 v04 快照未改。

影片未生成。若生成後殘像不夠明顯或動作太擠，可加大殘像不透明度描述，或把生成加長到 10 秒再取 0–8 秒放寬每個動作。
