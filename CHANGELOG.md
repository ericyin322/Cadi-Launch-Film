# 修改紀錄

## 2026-09-14

- SEG-01 A／B 提示詞升至 v04：加入史詩管弦配樂、慢速滑軌與局部半速動作；v03 保留，更新製作狀態與決策。

- 依使用者指示完成 SEG-01 的 seg01-a／seg01-b H3 v03 獨立純文字提示詞與生成說明；各 362 幀，規劃剪為 11＋13 秒。更新 registry、manifest、進度與狀態，舊提示詞保留，未生成影片。

- 使用內建 imagegen 完成 SEG-01 Storyboard v02 四格黑白圖，附生成提示詞與鏡頭說明；圖像待使用者確認，保留 v01，尚未製作新版 H3 提示詞。

- 經使用者授權，新增正式文字分鏡 v0.3，保留 v0.2；僅改寫 SEG-01 及其事件、連續性與索引記錄，SEG-02～13 劇情維持原文。
- SEG-01 改為客戶爭吵、文件飛散的失控會議；鏡頭先呈現環境，再找到角落的主角，透過退椅撞牆與默默整理落紙呈現受困與疲勞。
- 保留 24 秒時長、四個鏡頭編號、既有 CAE 需求與主角承接台詞；離場椅子動線改為避開牆面，接續 SEG-02。
- 同步更新 README、AGENTS、DECISIONS、PROGRESS 與 PROJECT_STATE 的來源及狀態；SEG-01 Storyboard v01 標示需依新版重製，未製作新圖或 H3 提示詞。

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





## 2026-09-14｜SEG-02 修改

- 新增文字分鏡 v0.4 與 SEG-02 brief-v02；僅更新 SEG-02 劇情、事件與連續性記錄。保留 21 秒時長及既有鏡頭 05–08 編號。
- 新版六格 Storyboard 表現門外飛紙、衝出關門、背靠門嘆氣撥髮、手錶震動、RF 變更郵件及同事群組抱怨。舊版保留；新版待使用者審查，H3 待製作。
- 同步更新專案入口、決策、進度及機器可讀狀態。


## 2026-09-14｜SEG-02 H3 提示詞

- 使用者確認 Storyboard v02；新增 seg02-a／seg02-b MiniMax H3 v01 純文字提示詞與生成說明，保留文字劇情。
- 配樂以低沉鼓聲逐漸增強、加密為主，群組抱怨時推高緊張感；分段正片 9＋12 秒，各生成 362 幀。
- 同步更新 registry、manifest、PROGRESS、PROJECT_STATE 與決策；提示詞已驗證並記錄第三槽保留宣告例外，影片與音樂未生成。
