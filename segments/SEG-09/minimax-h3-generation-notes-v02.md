# SEG-09 MiniMax H3 v02 使用說明

本版依使用者 2026-09-22 指示更新場景轉換及參考影片用途。原 v01 提示詞、registry、manifest、生成說明、Blender 工程與 MP4 均保留。

## 提示詞與時長

- A：`seg09-a-minimax-h3-prompt-v02.txt`，13 秒。Cadi 在純白房間彈指，鏡頭快速向右轉並在動態模糊中切換；當 Creo Robot 進入清晰畫面時，已置身 Creo 船塢。接著完成夾胸亮相、接住風扇、承重回穩與開始搬運。
- B：`seg09-b-minimax-h3-prompt-v02.txt`，13 秒。承接船塢搬運，完成五組協同落位、放手退開、升空俯瞰及 Cadi 下降至已放妥的右側風扇旁。
- 合計 26 秒，seed 7901，16:9；無台詞、無配樂、無聲。

## A 上傳順序

1. `<Picture 1>` Cadi：`assets/characters/cadi_red.png`
2. `<Picture 2>` Creo Robot：`assets/characters/creo-robot-concept/creo-robot-concept-v01.png`
3. `<Picture 3>` 純白房間：`assets/environments/純白房間.png`
4. `<Video 1>` 動作預演前半：`segments/SEG-09/reference-videos-v02/seg09-a-motion-reference-v02.mp4`，13 秒，源自原 MP4 的 0–13 秒，只作弱動作／運鏡參考。

## B 上傳順序

1. `<Picture 1>` Cadi：`assets/characters/cadi_red.png`
2. `<Picture 2>` Creo Robot：`assets/characters/creo-robot-concept/creo-robot-concept-v01.png`
3. `<Video 1>` 動作預演後半：`segments/SEG-09/reference-videos-v02/seg09-b-motion-reference-v02.mp4`，13 秒，源自原 MP4 的 13–26 秒，只作弱動作／運鏡參考。

## 參考影片邊界

`<Video 1>` 僅保留動作順序、節奏、承重回穩、五條搬運路線、手部接觸、落位時序、升降運鏡與最後下降弧線。影片不作直接剪輯、不延續其畫面材質，也不複製其聲音。目標角色外觀由 Picture 1／2 鎖定；A 的開場環境由 Picture 3 鎖定；船塢由提示詞內的正向材質、結構、照明與空間描述建立。

v01 的三張 Blender 構圖圖不再上傳，因為它們會額外強化預演畫面。這次不修改 `.blend`：即使重烘成其他底色，影片仍會提供一個可被模型仿效的背景；把影片降為時間與動作的弱參考、同時移除背景截圖，較符合本次目標。

## 生成與驗收

先生成 A，再生成 B。若節點支援首幀接續，取 A 的實際尾幀作 B 的首幀導引；不要新增不存在於 B 的純白房間參考。驗收重點：

- 0–2 秒 Cadi 明確位於純白房間。
- 轉鏡後第一次看清 Creo Robot 時，背景已是船塢；Creo Robot 不在白色房間亮相。
- 影片背景未主導目標畫面；船塢為寫實白灰金屬、綠色結構點綴、暖工業燈與柔和青色地面反光。
- 同一零件從搬運連續到落位；搬運期間對應位置空白，落位後無複本。
- 五組零件在 B 的 4–5 秒內完成接觸；5–7 秒放手退開；結尾 Cadi 停在已放妥風扇旁。
