# SEG-12 C H3 v03 使用說明（2026-10-14）

僅 C 升版；A v03、B v04、D v02 保留。C v02 與其他歷史檔不覆蓋。沿用 C v02 已授權內容，劇情、台詞、12 秒時序、seed 8201、16:9 與最後一秒白光轉場均不變。

上傳順序：
1. `segments/SEG-12/b-ending-ref.png` → `<Picture 1>`／`ref_image_0`，維持 B 尾幀首幀、構圖、站位、比例與船塢。
2. `assets/characters/cadi_red.png` → `<Picture 2>`／`ref_image_1`，補強首幀中同一位 Cadi 的身分、紅焰、眼睛、機甲與胸核。

使用 `seg12-c-minimax-h3-prompt-v03.txt`、`cast-registry-v06.yaml`、`reference-manifest-v06.json`。角色圖僅綁定既有 Cadi，初始位置與場景大小仍以首幀為準。畫風逐字取根目錄 registry。

先前 B 曾因額外 Cadi 圖產生重複角色；本版將兩圖明確綁定同一位 Cadi，仍須生成後確認只有一位 Cadi，並檢查首幀連續性、紅焰外觀及白光轉場。影片尚未生成。
