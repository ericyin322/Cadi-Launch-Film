# SEG-12 MiniMax H3 A／B v02＋C／D v01 使用說明

來源 `screenplay/master-storyboard-v0.26.md`／`brief-v03.md`。v01 全部保留。四段皆 Ref2VA、16:9、seed 8201；幀數依實際秒數換算。

| 段落 | 檔案 | 時長 | 內容 |
|---|---|---:|---|
| A | `seg12-a-minimax-h3-prompt-v02.txt` | 12秒 | 承接 SEG-10 船塢；Ray 殘影送回結果交給 Cadi、離鏡；Cadi 說 DLG-32A |
| B | `seg12-b-minimax-h3-prompt-v02.txt` | 13秒 | 升至廣角；六根 Rib 青色網格→實體灰金屬；女主角看後滿意 |
| C | `seg12-c-minimax-h3-prompt-v01.txt` | 12秒 | 起身致謝、Cadi 回應、整理衣服（原 A v01 內容） |
| D | `seg12-d-minimax-h3-prompt-v01.txt` | 7秒 | 布局拉遠→辦公室電腦→起身、螢幕關閉（原 B v01，僅 Rib 描述更新） |

## 上傳順序

| 插槽 | A | B | C | D |
|---|---|---|---|---|
| Picture 1／ref_image_0 | heroine-photo-reference-v01.png | 同左 | 同左 | 同左 |
| Picture 2／ref_image_1 | cadi_red.png | cadi_red.png | cadi_red.png | — |
| Picture 3／ref_image_2 | agent5-ray.png | Screenshot 2026-09-22 165319.png | Screenshot 2026-09-22 165319.png | — |
| Picture 4／ref_image_3 | Screenshot 2026-09-22 165319.png | bottom view- rib not yet.png | bottom view- rib done.png | — |
| Picture 5／ref_image_4 | bottom view 3_1.png | bottom view- rib done.png | — | — |

角色圖在 `assets/characters/`，placement 圖在 `assets/placement/`。A、B 各五張，保留檢查器的五圖軟警告（每張都有實際出場用途）。

## 指定台詞

- A／Cadi：「已收到最佳 rib 資料，現在開始生成rib。」
- C／女主角：「這次的工作我非常滿意，謝謝」
- C／Cadi：「不客氣，下次需要幫忙我依然會在」

## 生成與驗收重點

1. A 開場要和 SEG-10 B 結尾同位：女主角蹲在兩風扇之間、右手在大型風扇頂板左上區，Cadi 在左肩後方。若 SEG-10 B 已生成，可用其尾幀做連續性檢查。
2. B 開頭女主角先收手，避免與左側 Rib 的生成位置重疊；檢查網格階段是否清楚可辨，再看實體化是否由下而上漸進，不是瞬間跳成實體。
3. B 結尾數 Rib：大型風扇頂板上應為六根（四根放射長條＋兩塊短方塊），小風扇保持平整。數量或位置偏掉時，優先重抽 seed，其次把 C 的 rib done 圖改為 B 的尾幀。
4. C 的六根 Rib 要與 B 結尾一致；D 不出現角色以外的機器人，開頭只有完整布局。
5. SEG-11 C v03（舊的 Ray 回程＋單根 Rib）已由本段取代，請勿再剪入。

本輪只建立提示詞與配套檔案，影片未生成。
