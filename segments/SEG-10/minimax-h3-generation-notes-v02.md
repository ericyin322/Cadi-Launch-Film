# SEG-10 MiniMax H3 A／B v02 使用說明

依 2026-09-23 使用者直接要求生成 H3 提示詞，授權略過新版 Storyboard 尚未製作／確認的限制。劇情來源為 `screenplay/master-storyboard-v0.21.md` 與 `brief-v03.md`；舊版 A／B／C v01 保留。

## 生成單元

| 段落 | 檔案 | 時長 | 內容 |
|---|---|---:|---|
| A | `seg10-a-minimax-h3-prompt-v02.txt` | 13秒 | Creo 船塢內走到風扇旁、蹲下端詳、觸摸頂部、說強度不足 |
| B | `seg10-b-minimax-h3-prompt-v02.txt` | 13秒 | Cadi 啟動服務；Ray 殘影進場、敬禮、接資料、殘影離鏡 |

合計 26 秒，對齊 SEG-10 原時槽。兩段 seed 均為 8001，16:9，Ref2VA。

## 上傳順序

### A

1. `<Picture 1>`／`ref_image_0`：`assets/characters/heroine-photo-reference-v01.png`
2. `<Picture 2>`／`ref_image_1`：`assets/placement/Screenshot 2026-09-22 165319.png`

### B

1. `<Picture 1>`／`ref_image_0`：`assets/characters/heroine-photo-reference-v01.png`
2. `<Picture 2>`／`ref_image_1`：`assets/characters/cadi_red.png`
3. `<Picture 3>`／`ref_image_2`：`assets/characters/agent5-ray.png`
4. `<Picture 4>`／`ref_image_3`：`assets/placement/Screenshot 2026-09-22 165319.png`

指定 placement 圖在兩段都實際上傳，用於風扇形狀、人物比例與局部 placement 位置。船塢採文字建立，不掛場景圖。

## 對白與連續性

- A：女主角「這個風扇的強度不足」。
- B：Cadi「我來啟動風扇Rib AI 最佳化服務」。
- A 結尾女主角維持蹲姿、手在風扇頂部；B 從相同姿勢、同一風扇與同一光向開始。
- B 結尾 Ray 攜帶發光資料膠囊向 Rib 研究所方向高速離鏡，供 SEG-11 銜接。

## 驗收重點

1. A、B 地點皆為 Creo 船塢室內。
2. 風扇須維持指定圖的大型右上風扇外形：圓角外殼、直線內緣、頂部同心圓、中央凸起圓蓋與薄層側壁。
3. 女主角相對風扇的尺度須接近指定圖所示比例。
4. 兩句對白逐字、說話者與嘴型正確。
5. Ray 先以殘影進場，急停後清楚敬禮；接過資料後再以殘影離鏡。進場與離場各發生一次。
6. 紅焰 Cadi 持續燃燒且保持非固體火焰動態。

本輪僅交付提示詞與配套文件，尚未生成 H3 影片。
