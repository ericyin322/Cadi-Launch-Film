# 修改紀錄

## 2026-09-11

- 新增 S03b 獨立純文字 prompt 與生成說明 v01，涵蓋鏡頭 11；沿用 S03a 角色描述、兩圖順序與 seed 7301，補入 registry 與 manifest，更新 SEG-03 為兩段測試提示詞備齊。

- 新增 SEG-03 的 S03a MiniMax H3 Ref2VA 測試提示詞 v01，覆蓋鏡頭 09–10；限定只有女主角與 Cadi 出場。
- 建立 `cast_registry.yaml` 與 `manifest.csv`，固定 S03a 的角色 canonical description、seed、362 frames 與兩張參考圖上傳順序。
- 同步更新 `PROGRESS.md` 與 `PROJECT_STATE.json`；SEG-03 Storyboard 仍維持待集中審查，S03b 尚待製作。

## 2026-09-09

- 建立 `Cadi-Launch-Film` 專案資料夾。
- 匯入完整文字分鏡 v0.2。
- 匯入 SEG-01～SEG-13 Storyboard v01。
- 匯入 Cadi、主角臉部、主角服裝、Creo 與 Storyboard 畫風參考圖。
- 將 SEG-04 MiniMax H3 提示詞放回對應分段。
- 將舊版 MiniMax T2V 與 Seedance 文件移至 `archive/legacy-prompts`。
- 建立進度表、資產索引、機器可讀狀態與未來工作規則。
- 確立所有未來 MiniMax H3 提示詞的 Cadi 火焰規則：使用持續燃燒、具流體火焰動態的非固體青藍電漿描述，並明確排除果凍、橡膠與實心玻璃質感。
- 確立 MiniMax H3 圖片標籤規則：所有提示詞固定使用 `<Picture 1>` 綁定女主角、`<Picture 2>` 綁定 Cadi，兩者皆不得省略；其他圖片參考由 `<Picture 3>` 起編號。
- 新增 SEG-01 MiniMax H3 測試提示詞 v01：將原 24 秒內容拆成兩個各 15 秒的 Ref2VA 生成單元，並以 5 幀尾段 guide 規劃連續接合；維持 Storyboard 待審狀態。
- 新增 SEG-01 MiniMax H3 測試提示詞 v02：固定使用指定女主角設計表作 `<Picture 1>`、Cadi Design Sheet 作 `<Picture 2>`，並在兩段 prompt 中逐字加入指定的三段 `subject_definitions`。
