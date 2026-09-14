# SEG-01｜H3 生成說明 v03

依正式劇情 v0.3、Storyboard v02 製作。使用者看過圖後指示生成提示詞，據此進入 H3 製作；尚未實際生成或驗收影片。v01、v02 測試稿均保留。

## 分段與參數

| 分段 | 提示詞檔 | 覆蓋 | 生成 | 建議正片 |
|---|---|---|---|---|
| seg01-a | seg01-a-minimax-h3-prompt-v03.txt | 鏡頭 01–02：失控會議、找到角落 | 362 幀／15.083 秒 | 前 11 秒／264 幀 |
| seg01-b | seg01-b-minimax-h3-prompt-v03.txt | 鏡頭 03–04：撞牆、整理文件與承接 | 362 幀／15.083 秒 | 前 13 秒／312 幀 |

- 模式：本機 MiniMaxH3ReferenceToVideo／Ref2VA，24 FPS，16:9；同模型、解析度與 seed 7101。Seed 為本次製作設定，不保證構圖一致。
- A 尾端 98 幀、B 尾端 50 幀設為可裁切餘裕；保留合計 576 幀＝24 秒。以實際生成的動作與語音完成點調整剪點，不能直接截斷台詞。
- A 最後正片姿態和餘裕段相同：主角在右側牆角縮坐，雙手停在筆電旁，椅背尚未碰牆。B 以同姿態開場，再偏頭與退椅。兩段靠文字狀態描述銜接，不宣稱逐幀吻合；不需要傳入首尾幀或 guide。
- 彩色現實辦公室、冷灰環境、自然膚色；黑白 Storyboard 僅作離線構圖依據，不作影片的色彩參考，不上傳四格圖。

## 圖片上傳順序

1. ref_image_0／<Picture 1>：assets/characters/Gemini_Generated_Image_6rilce6rilce6ril.jpg。女主角身分、髮型、服裝；不取用設計表版面。
2. ref_image_1／<Picture 2>：assets/characters/cadi Design Sheet.jpg。依專案固定規則保留；Cadi 在本段明確禁止出場。

<Picture 3> 工廠的實體資產尚未指定。本次依 DECISIONS 保留三段固定英文宣告，但另外明寫第三張圖未提供、未使用，工廠禁止入鏡。不要用其他圖片補位，也不要將 Storyboard 填入第三槽。此為既有專案宣告規則與「只宣告實際上傳圖片」慣例之間的明確例外；不能把標籤檢查通過理解成第三張圖已就緒。未新增 <Picture 4>。

## 聲音與驗收

- A 保留 Baseline／材料與 A、B 按壓點兩句，句尾交疊；B 保留 Bellini Drop 需求及主角完整承接台詞。客戶互相爭吵，其他聲音保持模糊，不增寫新的可辨識要求。
- 若中文或英文術語生成不準、台詞超出視覺時窗，後製配置原文配音；保留原台詞，不以加速整段影片解決。
- 檢查客戶沒有五官、主角沒有加入爭吵、椅背碰牆後不穿牆、紙張確實落在鍵盤且被取走、文件疊放與筆記本閉合順序正確。B 結束仍坐著，留待 SEG-02 起身。
- 固定兩段共享環境聲底，接縫短交叉淡化；不重複任何台詞。不生成配樂。

## 驗證依據

使用專案 check_prompt.py 驗證六區段、時間碼、索引宣告、負面限制與 7000 字元上限。另比對 v02 的三段 subject_definitions 原文及 registry 的女主角／Cadi canonical description。

362＝17×21＋5。24 FPS 及幀格由 [ComfyUI 官方 H3 節點原始碼](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_minimax_h3.py)核對；未檢查使用者實際安裝版本。
