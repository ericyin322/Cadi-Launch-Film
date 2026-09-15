# 修改紀錄

## 2026-09-15

- 使用者實測發現：MiniMax H3 的文字條件沒有否定運算子，只要不該出場的物件出現在 `<Subject>` / `<Picture>` 標籤或提示詞裡（含 no / excluded / absent 等否定句），模型就會把它畫進畫面；Ref2VA 連上傳參考圖本身都是召喚。
- `.agents/skills/h3-scene-prompt/SKILL.md` 新增「Absent Objects」硬規則：不出場者不上傳圖、不編索引、全文不提名；負面表列只准放畫面瑕疵與鏡頭屬性；跨段一致性改由固定 seed ＋ 出場段落逐字重用 canonical 維持。
- `check_prompt.py` 新增 `check_summoning`：抓排除／保留宣告句型、與參考標籤同句的否定、以及不在 cast 卻被提名的 registry 資產（FAIL），並對負面表列裡的物件名詞提出 WARN；順手修掉在 Python 3.10 會 SyntaxError 的 f-string。
- `cast_registry.yaml` 移除 `visible_cast` 與 `reserved_unbound_picture`，`cast` 一律等於實際出場；資產新增 `summon_tokens` 供反向比對。`assets/segment_prompt.template.txt` 同步改寫指引。
- 既有提示詞尚未重做：seg02-a v03（7 FAIL）、seg02-b v04（6 FAIL）、SEG-01 a／b v04、SEG-03 S03b v01 均帶有排除宣告，需另開新版清除。

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


## 2026-09-14｜SEG-02 H3 v02

- 依更新後 MiniMax H3 技能重新產生 A／B 六區段提示詞及生成說明 v02；補強角色保留分析、鏡頭內時間與聲音同步，保留固定圖片宣告的專案例外。
- 維持已確認劇情、Storyboard v02、9＋12 秒、低鼓漸強與 UI 原文。v01 保留；更新 registry、進度與狀態。manifest 生成參數未變；未生成影片。


## 2026-09-14｜SEG-02 H3 v03（潤飾）

- 只潤飾提示詞，不動劇情、Storyboard v02、UI 原文、9＋12 秒切分與 seed 7201。v02 原檔保留。
- 鏡內時間改為 `[0s-2s]` beat 標記（修正 v02 在 check_prompt.py 的「無時間碼」FAIL，並與 SEG-01 v04 一致）；補 `<Subject 2>` 排除宣告；刪除靜態生圖殘留句；A／B 的 retention_analysis 各自獨立。
- 補 A 的開門動作與閉合筆電、改用官方鏡頭語彙與 cuts to、重整兩段負面表列；把剪輯用說明移回生成說明，字元數壓在 6991／6998（上限 7000）。
- 新增 minimax-h3-generation-notes-v03.md；更新 registry 提示詞路徑、PROGRESS 與 PROJECT_STATE。影片與音樂未生成。


## 2026-09-14｜SEG-02 H3 v04（seg02-b 掛 Teams UI 參考圖）

- 依使用者決定，seg02-b 的 `<Picture 3>` 由「虛擬工廠保留宣告」改綁 Teams UI 參考圖並新增 `<Subject 3>`；其他 SEG 與 seg02-a 的第三槽規則不變。
- 新增介面保留分析（header、圖示、頭像欄、泡泡形狀、圓角、字級比例 fully_preserved），並明確禁止沿用參考圖自帶的範例訊息、人名、時間戳、未讀標記與真人頭像；[Shot 2] 的 app 圖示改為取自同一張圖。
- registry 新增 teams_ui 資產（priority 30，assets/software/teams-ui-reference-v01.png），seg02-b cast 改為三張圖並移除 reserved_unbound_picture；同步更新 ASSET_INDEX。
- 驗證：seg02-b v04 為 12 passed / 0 warnings / 0 failed，字元數 6991。參考圖檔案尚未放入，影片與音樂未生成。
