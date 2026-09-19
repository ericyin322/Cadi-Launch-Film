# SEG-06 MiniMax H3 生成說明 v03

2026-09-19；依使用者要求重新讀取工廠文字描述並更新 DLG-14。

- A：`seg06-a-minimax-h3-prompt-v03.txt`，15秒；Picture 1 Cadi、Picture 2 drop、Picture 3 hapa、Picture 4 hana。
- B：`seg06-b-minimax-h3-prompt-v03.txt`，9秒；Picture 1 Cadi、Picture 2 drop。
- Ref2VA；seed 7601；上傳檔案見 `reference-manifest-v03.json`，規格快照見 `cast-registry-v03.yaml`。
- hapa 完整台詞：「最新 Spec 已取得。固有項目標綠，新增參數已標黃。」其他三句台詞保留。
- A／B 卡片語意統一為固有項目綠色、新增參數黃色；不再指定兩張黃色卡片。Cadi 原有衝突處理指示保留。
- 工廠來源：`assets/environments/virtual-factory-description-v01.txt`，採用本次讀取內容；場景段落與既有 v02 相同。畫風逐字使用根目錄 registry；工廠不掛圖片，建立鏡頭運鏡句依使用規則與本段原運鏡分開。
- 兩段延續 Cadi 左、drop 右、Spec 左、GP 右的交接構圖。配樂沿用112 BPM。維持24秒，配音仍待實測。
- Cadi 使用根目錄紅焰規格；延續本段不含女主角身高比較句的出場設定。
- 文字修訂依 `brief-v03.md`；歷史提示詞、brief與主分鏡保留。影片未生成。

驗證：A 14項、B 12項通過，0失敗；各1項為檢查器未計入小數時間節點的既有警告。另以支援小數的檢查確認兩段各6個連續節點、總長15／9秒；台詞、畫風與場景逐字比對通過，SEG-06全部歷史檔案雜湊不變。
