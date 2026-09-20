# SEG-09 MiniMax H3 v01 使用說明

依使用者確認的Blender v06動作及直接要求製作H3；本次作為分段授權動作版本，正式劇本v0.8及舊Storyboard保留。Ref2VA，使用專案`<Picture N>`語法。

## 提示詞
- A：`seg09-a-minimax-h3-prompt-v01.txt`，13秒：彈指、夾胸、接住墜落風扇、承重回穩、加速搬運。
- B：`seg09-b-minimax-h3-prompt-v01.txt`，13秒：接續搬運、五組約同時落位、放手退開、升空俯瞰、Cadi下降至已放置好的風扇旁。
- 合計26秒。兩段共用seed 7901，16:9；幀數依實際節點的13秒設定處理。
- 聲音沿用預演：無聲、無台詞、未加配樂。

## 兩段相同上傳順序
1. Cadi：`assets/characters/cadi_red.png`
2. Creo Robot：`assets/characters/creo-robot-concept/creo-robot-concept-v01.png`
3. 接住風扇：`segments/SEG-09/references-v01/picture-03-fan-catch-v01.png`，v06第164幀。
4. 搬運與完整布局：`segments/SEG-09/references-v01/picture-04-carry-layout-wide-v01.png`，v06第396幀的動作狀態，以拉遠機位另行渲染；不是原影片直接截取的機位。
5. Cadi在已放置風扇旁：`segments/SEG-09/references-v01/picture-05-cadi-fan-placed-v01.png`，v06第604幀。

圖片1、2為角色外觀；圖片3–5只供動作姿態、尺度、布局及構圖。工廠材質和照明採共用文字場景的室內政策，成片畫風逐字使用根目錄visual_style。Cadi分段規格移除與未出場女主角的身高比較，其餘canonical保留。

## 接續與狀態
A末尾持續前進，B開頭接續同一運動。先生成A，使用實際A尾幀作B的首幀／接續導引（節點支援時使用獨立first_frame或短尾片段導引，五張reference索引維持原順序）。此接續素材獨立於五張參考圖；不要把靜態圖片4當成固定B首幀。若節點僅能獨立參考生成，兩段交界需後期核對動勢與構圖。

B的4–5秒（全段17–18秒）完成五組落位；5–7秒放手退至外側；最後2秒Cadi停在已放妥風扇旁。搬運中平面位置留空，同一零件連續移動，落位後保持固定。生成結果須檢視手部接觸、零件唯一性、布局與落位時間。

## 檢查
A/B各13項通過，0失敗，2項提示：使用者指定五圖超過檢查器軟建議四圖；圖片3–5是構圖錨點，依正式格式使用獨立Picture定義而非新增角色Subject。兩者均保留使用者指定配置。此交付為提示詞及參考圖片，尚未生成H3影片。
