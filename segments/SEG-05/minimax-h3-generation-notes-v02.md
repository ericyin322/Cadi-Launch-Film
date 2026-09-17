# SEG-05｜H3 生成說明 v02

## 檢查結果

A：13項通過、1項警告、0項失敗；B：14項通過、1項警告、0項失敗。警告為檢查器未計入小數秒 beat；人工核對各六個連續節點，分別覆蓋14秒與12秒。角色索引、canonical、逐字畫風與字數上限均通過。影片尚待生成驗收。

依 2026-09-17 人物修訂與 `brief-v02.md` 更新既有提示詞。A v02：14秒；B v02：12秒。DLG-10、12 的稱呼分別改為 hapa、hana，其餘台詞與鏡頭時序保留。舊版保留，影片未生成；Storyboard v01 角色外形待更新。

## 參考圖上傳順序

| 圖片索引 | A v02 | B v02 | 用途 |
|---|---|---|---|
| Picture 1 / ref_image_0 | `assets/characters/heroine-photo-reference-v01.png` | 同左 | 女主角身分 |
| Picture 2 / ref_image_1 | `assets/characters/cadi Design Sheet.jpg` | 同左 | Cadi 身分 |
| Picture 3 / ref_image_2 | `assets/characters/agent2-hapa.png` | 同左 | hapa 身分 |
| Picture 4 / ref_image_3 | — | `assets/characters/agent1-hana.png` | hana 身分 |

兩張新增參考圖已檢視。只採角色外形、比例、配色與特徵；不採圖中文字、背景、排版及多視角人物數量。成片画風逐字採 registry visual_style。A 只出現 hapa；B 的第二鏡 hapa 與 hana 同時作業。聲線沿用 v01 製作設定，尚待影片驗收。

## 銜接與生成設定

A終點：hapa說完，Cadi左手放下、視線轉右。B開頭：接續轉右並揮右手。兩段保持左側SPEC／HTTP、右側GP辨識、中央南往北航道；主角躺椅留在中央中景。

這版為兩支獨立 Ref2VA 提示詞，固定 seed 不保證逐幀或角色一致。先生成 A，驗收後以其尾端姿勢對照 B。若需要精確首幀銜接，使用實際解碼尾幀接入工作流的 first_frame；一般語意參考插槽不等於首幀約束。改用首幀模式時另製對應提示詞版本。

時長依實際節點設定為14秒與12秒；未檢視本機H3節點，本次不宣稱特定幀數已驗證。檢查器輸出的362是專案預設值，不是兩支影片應填的幀數，也不代表時長通過驗證。

配樂沿用前段的輕快方向，112 BPM撥弦合成器、低音與輕電子節奏為製作安排；本段保留機械、掃描與運算音，依主分鏡05→06聲音銜接。前段「無效果音」為SEG04局部要求。最終剪輯用同一條連續音樂底，B結尾保留雙站運算聲銜接SEG06；未修改SEG06。

