# SEG-12 MiniMax H3 C v02／D v02 使用說明（2026-09-24）

來源 `screenplay/master-storyboard-v0.27.md`。A v03、B v04 不變；C v01／D v01 保留。seed 8201、16:9。

| 段落 | 檔案 | 時長 | 上傳順序 |
|---|---|---:|---|
| C | `seg12-c-minimax-h3-prompt-v02.txt` | 12秒 | 1 `segments/SEG-12/b-ending-ref.png`（B 尾幀＝首幀） |
| D | `seg12-d-minimax-h3-prompt-v02.txt` | 8秒 | 1 `assets/characters/heroine-photo-reference-v01.png`／2 `assets/placement/placement-creo-final.png`（螢幕內容） |

## C 段

- 以 B 尾幀開場，只掛這一張；不另掛女主角與 Cadi 身分圖（同 B v04 的做法，避免重複角色）。
- 女主角起身時鏡頭原地微微上仰保住臉部，不換機位；5–6 秒只沿同軸稍微推近。
- 台詞與動作不變：2–5 秒女主角致謝、6–9 秒 Cadi 回應、9–11 秒整理外套。
- 11–12 秒：Cadi 胸核爆出白光，一秒內鋪滿畫面，白光前緣帶紅橙火焰與餘燼，12 秒全白。

## D 段（7→8 秒）

- 0–1 秒：接 C 的全白畫面，四邊火焰邊緣。
- 1–2 秒：白光帶火焰邊緣向四周退去，露出電腦螢幕特寫，螢幕顯示 placement-creo-final.png。
- 2–8 秒：拉遠成辦公室 → 女主角後方 → 起身 → 螢幕關閉 → 停留。

## 驗收

- C：只有一個 Cadi、一位女主角；白光在最後一秒完成，邊緣看得到火焰。
- D：白光退去後的螢幕畫面要與 placement-creo-final.png 一致。
- C 12 項、D 13 項通過，均 0 警告、0 失敗。影片未生成。全段合計 45 秒，待校時。
