# SEG-12 MiniMax H3 A／B v03 使用說明（2026-09-24）

A／B v02 生成結果的三個問題已修正；C／D 仍用 v01（見 notes-v02）。seed 8201、Ref2VA、16:9。

| 段落 | 檔案 | 時長 | 上傳順序 |
|---|---|---:|---|
| A | `seg12-a-minimax-h3-prompt-v03.txt` | 12秒 | 1 heroine-photo-reference-v01.png／2 cadi_red.png／3 agent5-ray.png／4 Screenshot 2026-09-22 165319.png |
| B | `seg12-b-minimax-h3-prompt-v03.txt` | 13秒 | 1 heroine-photo-reference-v01.png／2 cadi_red.png／3 rib-not-yet-crop-v01.png／4 rib-done-crop-v01.png |

## 修正內容

1. **PCB 浮空／傾斜**：移除 `bottom view 3_1.png`，B 改用裁切圖（無板邊、無背景）；參考圖只管造型，機位改文字。兩段都寫明綠色基座是水平船塢地面、延伸出畫面四邊、地平線水平。
2. **B 多出工作桌**：裁掉左側記憶體／晶片等模組；刪除「左側小模組」描述；改寫為風扇四周空曠綠地；取消拉遠大廣角。
3. **Rib 長太高再變短**：網格一出現即是最終低矮尺寸（約殼體側壁高度），位置與尺寸固定，只由下而上填實成灰色金屬；刪除 extrude／grow upward／reach full height 等字眼。

## 驗收重點

- 地面：綠色板面與船塢地面同一平面、無板邊、無傾斜。
- B：畫面內無桌子；網格階段 Rib 高度不變；終態六根低矮 Rib。
- A、B 各 4 張圖，檢查 15 項通過、0 警告、0 失敗。影片未生成。
- C 仍掛原始 `bottom view- rib done.png`；若 C 生成後也出現板子傾斜，改用 `rib-done-crop-v01.png` 出 C v02。
