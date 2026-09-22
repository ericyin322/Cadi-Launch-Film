# SEG-08 MiniMax H3 生成說明 v04

2026-09-21。依 `brief-v04.md`（使用者授權修訂）製作；A 段更新桌面布局與女主角動作，B v02 保持不變。Storyboard v01 已過時、新版尚未製作。

## 分段與時長

| 分段 | 對應鏡頭 | 秒數 | 模式 | seed |
|---|---|---:|---|---:|
| seg08-a | 鏡頭28＋鏡頭29 | 13 | Ref2VA | 7801 |
| seg08-b | 鏡頭29A＋鏡頭30 | 10 | Ref2VA | 7801 |

合計23秒；原剪輯時槽 02:46–03:08 為22秒，多出的1秒待剪輯校時。

- `seg08-a-minimax-h3-prompt-v04.txt`：Placement 全程平放於工作桌面，Cadi 懸停在右側、雙手自然垂放，不拿布局。0–6秒女主角神情認真地端詳 Placement；6–8秒抬起右手，以食指指向 CPU，手只做小幅度移動；8–12秒維持指向並低聲咕噥 DLG-20；12–13秒放下手、挺直上半身，恢復直立站姿。布局由 `<Picture 3>` 鎖定。
- `seg08-b-minimax-h3-prompt-v02.txt`：金黃亮顯的方形零件在平面上水平側移約一個自身寬度後停住並維持亮顯，其餘零件全程不動；切雙人鏡，女主角保持站姿，點頭說 DLG-21，Cadi 回 DLG-22。

## 台詞

| 編號 | 角色 | 內容 | 位置 |
|---|---|---|---|
| DLG-20 | 女主角 | 或許cpu往旁邊移動一點 | seg08-a 8–12秒，咕噥、低音量；12–13秒放下手並恢復直立站姿 |
| DLG-21 | 女主角 | 好，使用這一版placement | seg08-b 5–7秒 |
| DLG-22 | Cadi | 好的，我來啟動Creo | seg08-b 7–10秒 |

DLG-23 已於 v0.15 停用，編號不重用。

## 參考上傳

依 `reference-manifest-v04.json`：

- seg08-a：`ref_image_0` = 女主角、`ref_image_1` = 紅焰 Cadi、`ref_image_2` = `assets/placement/placement_2D.png`。`<Picture 3>` 只負責鎖定完整布局的零件身分、相對比例、間距、位置、輪廓、配色分組與矩形平面方向；A 段不再上傳或引用 `<Video 1>`。
- seg08-b：維持 v02，`ref_image_0` = 女主角、`ref_image_1` = 紅焰 Cadi。
- seg08-b `<Video 1>`：`assets/blender/cpu-motion-v07/02-cpu-move-highlight-v07.mp4`，只取「移動＋停住」段（約0.6–1.6秒）；提示詞的 retention 已寫明用到零件停住為止、之後停在新位置，不使用原片後段的回位。

工廠採 `virtual-factory-description-v02.txt` 純文字場景。

## Absent Objects

本段 cast 只有 heroine 與 cadi。drop 在 SEG-07 排好布局，但本段不入鏡：不上傳參考圖、不編索引，提示詞（含 subject_definitions、retention_analysis、負面表列）完全沒有出現該名稱或任何指涉。工廠仍為純文字場景，不上傳參考圖。

## 驗證

`.agents/skills/h3-scene-prompt/scripts/check_prompt.py` 驗證結果：A v04 為14項通過、0警告、0失敗；B v02 以 v04 registry 複驗為13項通過、0警告、0失敗。`project.visual_style`、heroine／cadi／layout_ref canonical、圖片索引與 cast 均一致。

影片尚未生成。
