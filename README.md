# Cadi Launch Film

五分鐘技術發表會影片專案。目標觀眾為上級、主管與展會來賓；核心訊息是：Cadi 能自主規劃、調度多個 Agent 與工程服務，RD 只需審核關鍵決策。

## 工作原則

- `screenplay/master-storyboard-v0.25.md` 是目前唯一劇情來源。
- 每個 `SEG-xx` 是可獨立修改、替換或重新生成的模組。
- 修改既有分段時建立新版本，不覆蓋已保留的圖片。
- 新增段落時可使用 `SEG-07A` 等暫時編號；確定全片節奏後再統一重編。
- Storyboard 僅用於鏡頭、位置與動作確認；最終影片為彩色。
- MiniMax H3 提示詞獨立存放於各 SEG 目錄，不與文字分鏡或 Storyboard 混寫。

## 主要入口

- [完整文字分鏡](screenplay/master-storyboard-v0.25.md)
- [已確認創作決策](screenplay/DECISIONS.md)
- [製作進度](PROGRESS.md)
- [機器可讀狀態](PROJECT_STATE.json)
- [資產索引](assets/ASSET_INDEX.md)
- [修改紀錄](CHANGELOG.md)

## 額外工作流：特寫鏡頭

- [工作流規格 v02](workflows/close-up/workflow-v02.md)：以臉部特寫呈現既有表情與對話，沿用 H3 格式。
- [製作卡範本](workflows/close-up/shot-card-template-v02.md)／[特寫索引 v03](workflows/close-up/index-v03.json)。
- 實際素材歸屬 `segments/SEG-xx/close-ups/CU-01/`；選定鏡頭後才建立，不搬移既有 A／B 提示詞。
- 用途已確認為補拍／替換素材，保留原時間槽。使用者會在每個 SEG 的新對話提供台詞；以該次逐字原文製作，不自動抽取舊分鏡台詞或回寫主劇本。SEG-04 首組 7 支提示詞待依 v02 改善：上傳背景參考、只留台詞、前後各一秒緩衝、單人臉部特寫。

## 版本命名

```text
storyboard-v01.png
storyboard-v02.png
minimax-h3-prompt-v01.md
minimax-h3-prompt-v02.md
```

版本增加代表保留上一版。不得直接覆蓋已確認版本。

## 虛擬工廠場景

共用英文描述：`assets/environments/virtual-factory-description-v02.txt`；套用規則：`assets/environments/virtual-factory-usage-v02.md`。SEG-04～12原則上使用純文字工廠場景；SEG-07／08 最新版本改用 `assets/environments/純白房間.png` 圖片場景參考，Placement 懸浮於房間中央。現行提示詞與上傳順序以根目錄 registry 及各段最新 manifest 為準。
