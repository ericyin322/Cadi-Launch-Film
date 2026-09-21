# SEG-08 MiniMax H3 生成說明 v01

2026-09-21。依 `brief-v02.md`（使用者授權修訂）製作，使用者直接要求先出 H3，Storyboard v01 已過時、新版尚未製作。

## 分段與時長

| 分段 | 對應鏡頭 | 秒數 | 模式 | seed |
|---|---|---:|---|---:|
| seg08-a | 鏡頭28＋鏡頭29 | 12 | Ref2VA | 7801 |
| seg08-b | 鏡頭29A＋鏡頭30 | 10 | Ref2VA | 7801 |

合計22秒，與 02:46–03:08 時槽一致。

- `seg08-a-minimax-h3-prompt-v01.txt`：Cadi 把整片發光布局平面托離工作檯、平移到漂浮躺椅前並微微傾斜；女主角坐起前傾端詳；食指在布局上方空中筆畫（不觸碰平面），低聲咕噥 DLG-20。
- `seg08-b-minimax-h3-prompt-v01.txt`：金黃亮顯的方形零件在平面上水平側移約一個自身寬度後停住並維持亮顯，其餘零件全程不動；切雙人鏡，女主角點頭說 DLG-21，Cadi 回 DLG-22。

## 台詞

| 編號 | 角色 | 內容 | 位置 |
|---|---|---|---|
| DLG-20 | 女主角 | 或許cpu往旁邊移動一點 | seg08-a 9–12秒，咕噥、低音量、句尾收弱 |
| DLG-21 | 女主角 | 好，使用這一版placement | seg08-b 5–7秒 |
| DLG-22 | Cadi | 好的，我來啟動Creo | seg08-b 7–10秒 |

DLG-23 已於 v0.15 停用，編號不重用。

## 參考上傳

依 `reference-manifest-v01.json`，兩段都是 `ref_image_0` = 女主角、`ref_image_1` = 紅焰 Cadi（依 registry priority 排序，heroine 10 在 cadi 20 之前）。

- seg08-a `<Video 1>`：`assets/blender/cpu-motion-v07/01-scatter-rise-v07.mp4`，只取結尾的完成布局當構圖依據。
- seg08-b `<Video 1>`：`assets/blender/cpu-motion-v07/02-cpu-move-highlight-v07.mp4`，只取「移動＋停住」段（約0.6–1.6秒）；提示詞的 retention 已寫明用到零件停住為止、之後停在新位置，不使用原片後段的回位。

## Absent Objects

本段 cast 只有 heroine 與 cadi。drop 在 SEG-07 排好布局，但本段不入鏡：不上傳參考圖、不編索引，提示詞（含 subject_definitions、retention_analysis、負面表列）完全沒有出現該名稱或任何指涉。工廠仍為純文字場景，不上傳參考圖。

## 驗證

`.agents/skills/h3-scene-prompt/scripts/check_prompt.py` 對兩段各執行一次，均為 13 項通過、0 警告、0 失敗；`project.visual_style` 逐字一致，heroine／cadi canonical 逐字一致，索引與 cast 相符。

影片尚未生成。
