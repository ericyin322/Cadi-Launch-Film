# SEG-04 B｜H3 生成說明 v02

來源：`screenplay/master-storyboard-v0.8.md` SEG-04 節點14–15；`storyboard-v01.png` 已確認。本次僅製作 B，舊版合併提示詞與 A 保留。

## 提示詞與參考圖

可直接貼用：`seg04-b-minimax-h3-prompt-v02.txt`。採 Ref2VA 六區段格式及本專案 `<Picture N>` 語法。

1. `<Picture 1>`／`ref_image_0`：`assets/characters/heroine-photo-reference-v01.png`，女主角身分與服裝。
2. `<Picture 2>`／`ref_image_1`：`assets/characters/cadi Design Sheet.jpg`，Cadi 身分與比例。

只掛這兩張身分圖。場景依文字描述；沒有已指定的工廠參考圖，不建立圖片槽。黑白 Storyboard 僅供人工核對構圖，不上傳。畫風逐字使用 registry 的 `project.visual_style`。

## 時長與內容

- 沿用既有 A 9秒＋B 15秒的剪輯配置，B 約對應全片 01:15–01:30；開頭1秒承接坐定及抬手，01:16起呈交計畫。
- 16:9；沿用專案362幀／24fps設定，約15.083秒，正片使用15秒；多出影格作尾端餘裕。
- B seed：7401，為本次製作設定；固定 seed 不保證跨段身分或場景完全一致。
- 0–1秒：延續抬手，流程圖展開。
- 1–11秒：Cadi 完整說出 DLG-08；Spec 與 GP 同時亮起，之後依序彙整、Placement、Creo、Fan、Rib。
- 11–13秒：女主角看完計畫、右手持杯吸一口飲料。
- 13–15秒：DLG-09「核准。」、左手按核准印記，化成左右兩道資料光軌。
- 配樂沿用本段舊稿 N/A；保留工廠環境聲、投影聲、吸飲料聲及核准聲。

## 連續性與驗收

B 內維持單鏡頭。A 舊稿是純文字版本，尚不能據此保證整個 SEG-04 的一鏡到底。正式製作時須以 A 實際取用的邊界影格核對鏡位、焦距、角色位置、左右手、杯子、遮陽傘及背景幾何；本版暫用35mm與緩慢順時針繞攝作接續假設。若需精確接續，應以實際解碼邊界影格走支援首幀的工作流，再按該模式調整提示詞；不把首幀塞入角色身分圖槽。影片及邊界素材未在本次生成。

Cadi 完整長台詞排入10秒，尚未配音實測。驗收英文技術名詞、完整句尾與嘴型；若超時，先處理配音及剪輯時長，不擅自刪詞。流程圖文字以劇本原文為準；若生成字形不準，以追蹤圖層補正。

## 檢查結果

`check_prompt.py --registry cast_registry.yaml --segment seg04-b`：13 passed、0 warnings、0 failed；6879字元。兩句台詞與 v0.8 原文一致。此為提示詞靜態檢查，影片尚未驗收。
