# SEG-02｜MiniMax H3 生成說明 v04（seg02-b 掛 Teams UI 參考圖）

只改 seg02-b。seg02-a 維持 v03 不動。劇情、Storyboard v02、UI 原文、9＋12 秒切分、seed 7201、配樂方向都沒變。

## 需要你放的檔案

`assets/software/teams-ui-reference-v01.png`（目前尚未放入）。若你的檔案是 .jpg 或想用別的檔名，告訴我，我改 registry 與說明；路徑不一致時 ref_image 會掛錯。

## 圖片槽位（本段為專案例外）

| 上傳順序 | 標籤 | 檔案 | 用途 |
|---|---|---|---|
| ref_image_0 | `<Picture 1>` / `<Subject 1>` | Gemini_Generated_Image_6rilce6rilce6ril.jpg | 女主角身分 |
| ref_image_1 | `<Picture 2>` / `<Subject 2>` | cadi Design Sheet.jpg | Cadi 身分綁定（本段禁止出場） |
| ref_image_2 | `<Picture 3>` / `<Subject 3>` | assets/software/teams-ui-reference-v01.png | 群組聊天介面版面基準 |

依使用者 2026-09-14 決定，seg02-b 的第三槽由「虛擬工廠保留宣告」改綁 Teams UI 參考圖。理由是實體上傳只有三張，若照原規則把新圖標成 `<Picture 4>`，模型會把它對到 ref_image_2，也就是被當成第三槽的工廠。其他 SEG 的第三槽維持工廠保留宣告不變。seg02-a 仍是兩張圖＋未綁圖的保留宣告。

## 提示詞怎麼用這張圖

- `<Subject 3>` 綁 `<Picture 3>`，保留分析標 fully_preserved：header 配色與高度、標題位置、通話圖示、頭像欄、泡泡形狀、圓角、間距與字級比例。
- 明確禁止沿用參考圖自帶的內容：範例訊息、人名、時間戳、未讀標記、真人頭像、側邊欄。畫面上所有文字只能是專案指定的三則抱怨與標題。
- [Shot 2] 第 4.6 秒點的 app 圖示也改成取自 `<Picture 3>`，讓圖示與下一個鏡頭的滿版介面同源。
- 提示詞寫的是「完整沿用參考圖的 header／圖示／圓角／配色」，沒有逐字描述任何品牌商標。商標由你的參考圖本身帶入；若要像素精準，最後仍建議以後製 UI 圖層蓋上，AI 重畫商標通常會變形。
- 負面表列中原本的 `no virtual factory <Picture 3>` 改寫為 `no virtual factory or engineering city`，避免標籤與新用途衝突。

## 驗證

`python check_prompt.py segments/SEG-02/seg02-b-minimax-h3-prompt-v04.txt --registry cast_registry.yaml --segment seg02-b`
→ **12 passed, 0 warnings, 0 failed**（本專案目前唯一全綠的提示詞；第三槽補上實體圖後，原本的 cast 不符 FAIL 與 Picture 3 無 Subject 的 WARN 都消失）。字元數 6991／上限 7000。

seg02-a v03 維持 10 passed / 1 warn / 1 fail，兩者都是既有的 Picture 3 保留槽例外。

## 生成後檢查

除 v03 既有項目外，加查：三則泡泡的中文與專案原文逐字相同、沒有混入參考圖的範例訊息或人名、頭像不是真人照片、header 標題是「Placement 討論」、商標若變形則以後製圖層補正。
