# SEG-07｜H3 生成說明 v02

依 brief-v02 製作。使用者確認文字修訂後直接要求 A／B H3，依此授權製作；新版 Storyboard 尚未製作，不標記為已驗收。影片尚未生成。

本版依使用者要求同步Cadi紅黑配色：紅橙火焰、暖白焰心／眼光、深紅眼框、深灰機甲與紅色關節、暖白金橙胸核。v01完整保留。為符合7000字元上限，精簡重複的場景及配樂敘述；劇情、台詞、時間與動作不變。場景青藍補光及投影維持原設定。

## 提示詞與上傳順序

採專案既定 Ref2VA `<Picture N>`／`<Video N>` 語法，16:9，兩段 seed 7701。

| 項目 | A：14秒 | B：12秒 |
|---|---|---|
| 提示詞 | seg07-a-minimax-h3-prompt-v02.txt | seg07-b-minimax-h3-prompt-v02.txt |
| Picture 1／ref_image_0 | Cadi | 女主角 |
| Picture 2／ref_image_1 | drop | Cadi |
| Picture 3／ref_image_2 | 不上傳 | drop |
| Video 1／第一個影片插槽 | 零件落下影片：排列動作與完成布局 | 同一影片：僅結尾完成布局 |

圖片預設路徑：
- 女主角：`assets/characters/heroine-photo-reference-v02.png`
- Cadi：`assets/characters/cadi_red.png`
- drop：`assets/characters/agent3-drop.png`
- 影片：`assets/blender/cpu-motion-v07/01-scatter-rise-v07.mp4`

使用者可在生成時上傳這四份對應素材。A 女主角未出場，不上傳她的圖；B 的 drop 留在工作檯後右側。圖片只提供角色身分、比例及配色。影片提供零件動作及布局，不取其白底、預演材質、攝影機或聲音作成片基準；以上用途邊界已在模型提示詞以正向敘述指定。`.blend` 為動作原檔，不是 H3 上傳影片。

`reference-manifest-v02.json` 包含完整圖片及影片綁定；根目錄 manifest.csv 僅記圖片順序。registry 的 reference_videos 欄另記影片。

## 時間安排

- A 0–6秒：drop 延續 SEG06 比對 Spec／GP，保留黃色待確認標記；Cadi 在旁觀看。
- A 6–8秒：drop 展開水平立體投影。
- A 8–14秒：依6秒參考影片呈現散開、落下、逐步排好；末尾穩定停留。
- B 0–6秒：延續完整布局，攝影機緩退，零件保持就位。
- B 6–8秒：同側廣景帶出躺椅上的女主角；Cadi 轉身示意布局。
- B 8–11秒：Cadi 完整說出「這是最新版的placement，您覺得如何」。
- B 11–12秒：女主角觀看布局，銜接 SEG08。

合計26秒，維持02:20–02:46。A14＋B12是製作節奏安排；brief-v02原鏡頭25–26的內部分配調整為A末完成、B首展示，事件次序不變。台詞尚未配音實測。

## 畫面與聲音銜接

A尾與B首均為同側斜俯視完整布局：Cadi左、drop右，矩形長後緣位於畫面上方；右上暖光、左側青藍補光保持一致。B透過較廣畫面帶出女主角，保留她在躺椅上的姿勢接SEG08。

先生成A並檢視末幀，再生成B。若工作流支援首幀錨定，將A實際解碼末幀接至專用 first_frame；身分圖片與影片索引依上表保持。兩段相同seed及文字只能輔助一致性，不保證逐幀布局或角色位置相同。若使用重疊導引，剪去重複區間，使淨長維持26秒。

成片畫風逐字取自主registry project.visual_style；Cadi採用commit 724a701的根目錄紅焰規格，移除未出場女主角的身高比較句，兩段canonical逐字一致。聲音沿用SEG06的112 BPM輕快器樂、低街區底聲與輕微機械／投影聲；A全段無對白，B僅Cadi一句。參考影片不綁音訊。剪輯時用連續音樂底接合兩段。

時長依實際節點設定14秒／12秒，幀数留待工作流計算，不套用固定362幀。

## 驗證

- check_prompt.py：A 13 passed／0 warnings／0 failed；B 14 passed／0 warnings／0 failed。
- A 6814字元；B 6871字元。各六個連續beat，分別覆蓋14秒／12秒。
- 額外核對：Video 1宣告與用途、四份素材存在、指定台詞逐字一致、A無女主角引用、主registry畫風逐字一致。
- 角色、完整零件數量、排列位置、投影質感、口型與接縫仍待成片驗收。
