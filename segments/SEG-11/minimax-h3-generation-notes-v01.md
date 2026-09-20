# SEG-11 MiniMax H3 A／B v01 使用說明

依 2026-09-20 使用者直接要求生成 MiniMax H3 提示詞。劇情來源為 `screenplay/master-storyboard-v0.11.md` 與 `brief-v02.md`；Storyboard v01 的研究角色仍是舊版，本次授權記為直接要求 H3，不宣稱新版 Storyboard 已完成或確認。

## 可直接貼用的提示詞

| 段落 | 檔案 | 時長 | 內容 |
|---|---|---:|---|
| A | `seg11-a-minimax-h3-prompt-v01.txt` | 13秒 | Ray 交付模型資料；Finn 掃描四種限制、確認條件並啟動運算 |
| B | `seg11-b-minimax-h3-prompt-v01.txt` | 13秒 | Finn 篩選 Rib 並交還結果；Ray 送回中央航道；Cadi 完成組裝 |

合計26秒，對齊原 SEG-11 的 04:00–04:26 時槽。兩段皆為 Ref2VA、16:9、seed 8101；節點時長各設13秒，幀數依實際節點換算。

## 上傳順序

| 圖片／插槽 | A | B |
|---|---|---|
| Picture 1／ref_image_0 | `assets/characters/agent5-ray.png` | `assets/characters/cadi_red.png` |
| Picture 2／ref_image_1 | `assets/characters/agent4-finn.png` | `assets/characters/agent5-ray.png` |
| Picture 3／ref_image_2 | 不掛圖 | `assets/characters/agent4-finn.png` |

每張圖只供單一角色的身分、外形、比例與色系。A 只出現 Ray、Finn；B 出現 Cadi、Ray、Finn。未出場角色不上傳、不編索引、提示詞不提。研究所與工廠街區均使用文字場景；A 為純室內，只描述可見材質與照明；B 前半為研究所內景，後半回到中央航道並逐字套用共用工廠描述。畫風逐字取自根目錄 `project.visual_style`。

## 對白與聲音

- A／Ray：「外殼、鎖點、禁佈區和風道資料都在這裡，請計算可行 Rib。」
- A／Finn：「條件完整。避開 Connector 與風道，開始運算。」
- B／Cadi：「Rib 已組裝完成，避開 Connector、風道與禁佈區。」
- Ray 使用清楚、俐落、精準的年輕國語聲線；Finn 使用沉著、分析型、帶輕微電子質感的成年國語聲線；Cadi 延續清亮、俏皮且專業的童聲。
- 配樂留空；保留低量環境聲、運算聲、履帶／腳步、交接、拋接與組裝效果音。

## 銜接方式與驗收

1. A 承接 SEG-10 C 結尾 Ray 抱箱越過研究所門口的動勢；若已有實際 H3 成片，優先用解碼尾幀或短尾片導引，不把它編入角色 Picture 索引。
2. A 尾為運算核心開始工作；B 開頭直接延續同一核心與角色位置。固定 seed 只輔助一致性，不能取代實際邊界影格。
3. B 於6秒切回中央航道；研究所內景不寫街區物件，外景才套用完整共用工廠描述。
4. B 尾保持完成模型穩定，供 SEG-12 從模型後方繞向女主角；女主角本段不入鏡、不上傳參考圖。
5. 生成後核對三句對白逐字、Ray→Finn→Ray→Cadi 的資料匣唯一性、Rib 候選紅色淘汰／青藍保留、Cadi 紅焰持續燃燒與全部角色身分穩定。

本輪僅交付提示詞與配套；尚未生成 H3 影片或完成配音、嘴型及交界驗收。
