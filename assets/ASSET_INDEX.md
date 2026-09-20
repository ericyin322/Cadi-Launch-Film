# 資產索引

- 2026-09-19：虛擬工廠（SEG-04～SEG-12）統一採 `assets/environments/virtual-factory-description-v01.txt` 的英文文字場景；使用方式見 `assets/environments/virtual-factory-usage-v01.md` 及根目錄 registry `project.virtual_factory`。工廠不上傳參考圖、不編圖片索引。場景建立運鏡與既有鏡頭運鏡分開套用；室內只描述當鏡可見內容。既有稿保留，更新另建新版。


- 2026-09-16：SEG04-B v03：新增工廠（Picture 3，僅場景建筑與空間布局）、流程圖（Picture 4，僅節點布局、連線、標籤與符號）。兩張圖片路徑留空於 segments/SEG-04/reference-paths-v03.yaml，由使用者自行處理；未檢視實際圖片，不能確認其內容與劇情一致。畫風仍以 registry visual_style 為準，角色身分由 Picture 1／2 提供。

SEG-02B v08 新增待提供資產：`software/phone-home-reference-v01.png`，綁定 `<Picture 2>`；用途為手機桌面（桌布、Teams icon 外觀／大小／位置），郵件通知另疊。群組三位同事使用各自生成的 profile 照片，與姓名及聲音固定配對；不沿用群組參考圖的既有人像身分。

| 檔案 | 用途 | 可參考 | 不可直接沿用 |
|---|---|---|---|
| `characters/agent5-ray.png` | SEG-10 Ray 身分；SEG-11 連續性延續，取代小花 | 角色外觀、比例與身分特徵 | 背景、文字、排版及參考圖畫風；成片畫風依 registry |
| `blender/cpu-motion-v07/01-scatter-rise-v07.mp4`、`01-scatter-rise-v07.blend` | SEG-07 零件排列動作參考 | 散開、灑落、逐步就位與平面布局 | 角色身分、白底預演材質與成片畫風 |
| `characters/agent3-drop.png` | SEG-06 drop 身分，取代小白；SEG-07開頭延續 | 白色水滴形頭部、藍眼、白色機身、黑色關節、藍色水滴胸核、比例及關節 | 背景、水花裝飾、文字、排版、多視角人物數量 |
| `characters/agent2-hapa.png` | SEG-05／06 hapa 身分；取代小明 | 白色機身、綠眼、葉片耳飾、綠葉胸徽、比例及關節 | 背景、文字、排版、多視角人物數量 |
| `characters/agent1-hana.png` | SEG-05／06 hana 身分；取代小華 | 白色機身、紅棕眼、花瓣耳飾、粉色飄帶、櫻花胸徽、比例及關節 | 背景、文字、排版、多視角人物數量 |
| `characters/heroine-photo-reference-v01.png` | MiniMax H3 女主角身分基準（2026-09-15 起取代設計表） | 寫實臉部、長直中分黑髮、米灰西裝與淺色上衣、真人質感 | 灰色棚拍背景 |
| `characters/Gemini_Generated_Image_6rilce6rilce6ril.jpg` | 女主角設計表；Storyboard 用。H3 不再上傳（插畫風會把成片拉成動畫） | 臉部、長直中分黑髮、正側背比例、米灰西裝與淺色寬褲、表情與專業氣質 | 設計表排版、文字、色票、物件圖示與白色背景 |
| `characters/cadi_red.png` | Cadi 現行身分與色系基準（2026-09-17 起；索引依當段出場角色排序） | 紅橙動態火焰、暖白焰心／眼光、深紅眼框、深灰機甲、紅色關節點綴、金橙暖白胸核、比例與表情 | 排版、標題、文字、色票、白色背景與多視角人物數量 |
| `characters/cadi Design Sheet.jpg` | 舊藍焰版歷史資產；既有 H3 引用保留 | 舊版回溯 | 不作新製作色系基準 |
| `characters/cadi-reference-v01.png` | 舊版 Cadi 參考；歷史保留 | 舊版回溯 | 不作新製作色系基準 |
| `characters/heroine-face-reference-v01.png` | 主角臉部基準 | 臉型、長直黑髮、氣質 | 原服裝、背景與光線 |
| `characters/heroine-outfit-reference-v01.png` | 主角服裝基準 | 西裝外套、淺色上衣、寬褲輪廓 | 原人物臉部與姿勢 |
| `software/creo-interface-reference-v01.png` | Creo 視覺基準 | 灰白介面、頂部功能區、模型樹與建模視窗 | 小字、網址與截圖內容 |
| `software/teams-ui-reference-v01.png` | seg02-b 專用 `<Picture 1>`／群組聊天介面基準（待放入） | header 配色與高度、標題與通話圖示位置、頭像欄、泡泡形狀與圓角、字級比例 | 原圖的範例訊息、人名、時間戳、未讀標記、真人頭像與側邊欄 |
| `style/storyboard-style-reference-v01.png` | Storyboard 畫風基準 | 黑白線稿、漫畫式角色、分格與景深 | 原劇情內容 |

所有外部暫存素材已複製到本專案，後續不再依賴 Downloads 或 Temp 路徑。
