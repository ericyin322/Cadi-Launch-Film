# SEG-03 A／B 生成說明 v02

來源：`screenplay/master-storyboard-v0.8.md` SEG-03（鏡頭09–11，21秒）。使用者 2026-09-15 直接要求生成；新版 Storyboard 尚未製作／確認（同 SEG-01、SEG-02 的使用者授權例外）。S03a／S03b v01 保留不動。

## 檔案與剪輯

| 段 | 檔案 | 內容 | 正片取用 |
|---|---|---|---|
| A | `seg03-a-minimax-h3-prompt-v02.txt` | 鏡頭09–10：挪椅坐下、喚醒螢幕「Hi，Cadi。」、Cadi 螢幕內問候、Lisa 不耐煩交代信件、Outlook icon、0.5秒思考停頓 | 0–9.5 秒 |
| B | `seg03-b-minimax-h3-prompt-v02.txt` | 鏡頭11：Cadi 長句建議（鏡頭退至肩後）、Lisa 點頭「讓我們開始吧。」、胸口光擴張、青藍光掃鏡 | 0–11.5 秒 |

合計 21 秒。各生成 15 秒／362 幀、seed 7301；A 尾段 10–15 秒為 Cadi 靜候、B 尾段 12–15 秒為滿版青藍光，供剪輯緩衝與接 SEG-04。

## 上傳順序（兩段相同）

1. `<Picture 1>`／`ref_image_0`：`assets/characters/heroine-photo-reference-v01.png`
2. `<Picture 2>`／`ref_image_1`：`assets/characters/cadi Design Sheet.jpg`

## 時間表

- A：0–2 秒挪椅坐下｜2.0 喚醒｜2.6–3.4 「Hi, Cadi.」(S1)｜3.6 火焰點燃 Cadi 現身｜4.1–5.9 Cadi 問候 (S2)｜6.1–7.9 Lisa 不耐煩 (S1)｜8.1 Outlook icon｜8.5–9.0 完全靜止停頓｜9.0 看回女主角
- B：0.2–8.6 Cadi 長句 (S1)｜8.8 切女主角｜9.1–10.2 「讓我們開始吧。」(S2)｜10.4 胸口光擴張｜11.5 光鋪滿畫面

H3 規則要求 `(Sx)` 依單支影片發聲順序編號，故 A 中女主角為 S1、B 中 Cadi 為 S1。

## 風險與假設（生成後需驗收）

1. **Cadi 長句時長**：DLG-06B 約 65 字，壓在 8.4 秒內需約每秒 7–8 字的輕快語速。若生成後被截斷或過快，選項：B 延至 12.5 秒並把 A 壓到 8.5 秒，或請使用者授權精簡台詞（未經授權不改）。
2. **筆電**：分鏡09 已刪去筆電接工作站動作，提示詞不提筆電（提到就會被畫出來）；與 SEG-02 結尾右臂夾筆電的銜接靠剪輯處理。
3. **Cadi 參考圖為插畫設計表**：registry 仍綁 `cadi Design Sheet.jpg`。Cadi 在螢幕內出場，插畫感影響較小，但若辦公室實景被拉向插畫質感，應先製作 Cadi 的寫實 CG 參考圖再重生成。
4. **配樂**：v0.8 未指定本段配樂；暫定 SEG-02 D 小調低鼓在 A 前 2 秒收尾，Cadi 現身轉 D 大調合成器琶音，B 收尾隨光掃鏡上揚。可依需求改。
5. **Outlook icon**：以提示詞生成品牌圖示，形狀可能不準，必要時後製覆蓋。

## 驗證

`check_prompt.py`：A、B 皆 13 passed／0 warn／0 fail（A 7000 字元上限內）。影片未生成。
