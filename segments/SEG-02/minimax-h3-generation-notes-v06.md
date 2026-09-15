# SEG-02 生成說明 v06｜畫風召喚修正

- 最新提示詞：`seg02-a-minimax-h3-prompt-v05.txt`、`seg02-b-minimax-h3-prompt-v06.txt`。A v04、B v05 保留。劇情、時間軸、聲音與 seed 7201 完全不變。
- A：畫風開頭改為逐字複製 `cast_registry.yaml` 的 `project.visual_style`；刪除 retention 中「its drawing style … replaced」否定句，改成正向真人描述。
- A 上傳改為 `ref_image_0` = `assets/characters/heroine-photo-reference-v01.png`（設計表右下寫實棚拍裁切），不再掛插畫設計表。
- B：畫風開頭同樣改用 `visual_style`；頭像描述由 flat illustrated circles 改為 plain solid-color circles。上傳仍為 Teams UI 參考圖。
- 驗證：A 5090 字元、B 5044 字元，皆 12 passed／0 warn／0 fail（含新增的畫風檢查）。影片未生成。
