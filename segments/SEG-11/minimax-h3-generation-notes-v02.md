# SEG-11 MiniMax H3 A／B v02 使用說明

依 2026-09-20 使用者指定修改 A 段兩句台詞與資料內容，並重構 B 段為 Ray 帶回計算結果、回到 SEG-10 端詳風扇的場景、同一風扇長出一根 Rib、Cadi 回報完成、女主角開心點頭。v01 全數保留，本版是使用者指定的 H3 劇情覆寫；尚未回寫正式文字分鏡。

## 可直接貼用的提示詞

| 段落 | 檔案 | 時長 | 內容 |
|---|---|---:|---|
| A | `seg11-a-minimax-h3-prompt-v02.txt` | 13秒 | Ray 交付殼體厚度、Gap 距離及材質資料；Finn 確認並開始 AI 最佳化運算 |
| B | `seg11-b-minimax-h3-prompt-v02.txt` | 13秒 | Ray 帶結果回到同一風扇；單根結構 Rib 生長並鎖定；Cadi 回報，女主角開心點頭 |

合計26秒，維持 SEG-11 原時槽。兩段皆為 Ref2VA、16:9、seed 8101；節點時長各設13秒，幀數依實際節點換算。

## 上傳順序

| 圖片／插槽 | A | B |
|---|---|---|
| Picture 1／ref_image_0 | `assets/characters/agent5-ray.png` | `assets/characters/heroine-photo-reference-v01.png` |
| Picture 2／ref_image_1 | `assets/characters/agent4-finn.png` | `assets/characters/cadi_red.png` |
| Picture 3／ref_image_2 | 不掛圖 | `assets/characters/agent5-ray.png` |

A 只出現 Ray、Finn；B 只出現女主角、Cadi、Ray。Finn 在 B 不出場，因此不上傳、不編索引、提示詞不提。場景只用文字：A 是研究所內景；B 回到 SEG-10 的風扇檢查位置，延續同一風扇、位置、比例、光向與開口構圖，不使用工廠圖片。

## 指定台詞

- A／Ray：「殼體厚度、Gap距離、材質資料都在這裡，請計算可行 Rib。」
- A／Finn：「條件完整。開始AI最佳化運算。」
- B／Cadi：「根據計算結果自動生成Rib完成。」

台詞在提示詞中逐字保存；A 的空間資料同步改成殼體厚度、Gap 距離與材質三層。B 的「柱子」具體化為一根直立矩形結構 Rib：從風扇殼體內側單一基座開始，基座增厚、柱身向上延伸、邊緣鎖定、頂部短支撐接合，最後只留下單根完成件。

## 銜接與驗收

1. A 承接 SEG-10 C 的 Ray 抱箱入研究所；A 尾停在 Finn 啟動運算。
2. B 省略研究所內的完成畫面，直接從 Ray 已拿到結果、走回同一風扇開始；A／B 之間可用短暫聲音橋銜接。
3. B 必須維持 SEG-10 既有風扇已落位且固定，不得生成第二台風扇或移動原風扇。
4. Rib 必須從殼體內側單一固定點連續生長，完整呈現起點、柱身延伸、接合與停止；不得突然跳出完整成品。
5. 結尾順序固定：Rib 完成 → Cadi 說完整台詞 → 女主角開心點頭。影片生成後另驗配音、嘴型、角色身分與物件唯一性。

本輪僅更新提示詞與配套；尚未生成 H3 影片。
