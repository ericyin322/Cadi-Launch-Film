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
