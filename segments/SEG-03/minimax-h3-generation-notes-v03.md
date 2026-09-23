# SEG-03 A／B 生成說明 v03

來源：`screenplay/master-storyboard-v0.22.md` SEG-03（鏡頭09–11，21秒）與 `brief-v03.md`。使用者 2026-09-23 直接要求生成；新版 Storyboard 尚未製作／確認（沿用使用者授權例外）。A／B v02 保留不動。

## 檔案與剪輯

| 段 | 檔案 | 內容 | 正片取用 |
|---|---|---|---|
| A | `seg03-a-minimax-h3-prompt-v03.txt` | 鏡頭09–10：挪椅坐下、「Hi, Cadi.」、紅焰 Cadi 螢幕內問候、Lisa「接到一個棘手的任務，你看一下。」、Outlook icon、讀郵件、驚訝表情、0.5 秒思考停頓 | 0–11.0 秒 |
| B | `seg03-b-minimax-h3-prompt-v03.txt` | 鏡頭11：Cadi 建議（鏡頭退至肩後）、Lisa 點頭「讓我們開始吧。」、胸核擴張、紅橙暖光掃鏡 | 0–10.0 秒 |

合計 21 秒；各生成 15 秒／362 幀、seed 7301。A 11–15 秒為 Cadi 靜候、B 10–15 秒為滿版暖金白光，供剪輯緩衝與接 SEG-04。

## 上傳順序（兩段相同）

1. `<Picture 1>`／`ref_image_0`：`assets/characters/heroine-photo-reference-v01.png`
2. `<Picture 2>`／`ref_image_1`：`assets/characters/cadi_red.png`（取代 v02 的 `cadi Design Sheet.jpg`）

## 時間表

- A：0–2 挪椅坐下｜2.0 喚醒｜2.6–3.4 「Hi, Cadi.」(S1)｜3.6 紅焰點燃 Cadi 現身｜4.1–5.9 Cadi 問候 (S2)｜6.1–7.6 Lisa 不耐煩 (S1)｜8.1 Outlook icon｜8.2–9.0 眼睛左右掃讀｜9.0–9.6 驚訝（睜眼、張嘴、後仰、火焰竄高）｜9.7 托腮｜10.0–10.5 完全靜止停頓｜10.5 看回女主角
- B：0.2–7.0 Cadi 長句 (S1)｜7.2 切女主角｜7.3 點頭｜7.5–8.6 「讓我們開始吧。」(S2)｜8.8 切螢幕、胸核擴張｜10.0 光鋪滿畫面

## 本版變更

- Cadi 改用根目錄 registry 的紅焰 canonical（逐字），螢幕光、臉部補光、光掃鏡改為紅橙／暖金白。
- Cadi 兩句台詞聲音描述逐字統一為 `in a bright, playful yet professional childlike Mandarin voice`。
- DLG-06A、DLG-06B 依 v0.22；DLG-06B 約 49 字、6.8 秒（每秒約 7 字），比 v02 寬鬆。
- 為壓在 7000 字元內，retention 採精簡版（同 SEG-10 v04 作法），canonical 仍逐字。

## 風險

1. 驚訝表情只有約 0.6 秒，若不明顯可把 9.0–9.6 延長並將停頓順延，A 取用至 11.5 秒、B 改取 9.5 秒。
2. Outlook icon 為生成品牌圖示，形狀可能不準，必要時後製覆蓋。
3. 提示詞不提筆電；與 SEG-02 結尾夾筆電的銜接靠剪輯。
4. 配樂仍為暫定（D 小調低鼓收尾 → D 大調琶音）。

## 驗證

`check_prompt.py`（`cast-registry-v03.yaml`）：A 13 passed／0 warn／0 fail（6962 字元）；B 13 passed／0 warn／0 fail（6662 字元）。影片未生成。
