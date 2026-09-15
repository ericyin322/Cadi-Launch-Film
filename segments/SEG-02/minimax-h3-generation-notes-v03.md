# SEG-02｜MiniMax H3 生成說明 v03

本版只潤飾 seg02-a／seg02-b 提示詞本身，劇情、Storyboard v02、UI 原文、9＋12 秒切分、低鼓漸強與 seed 7201 全部維持不變。v02 原檔保留。影片與音樂仍未生成。

## 這版改了什麼（相對 v02）

1. **鏡內時間碼改為 `[0s-2s]` beat 標記**。v02 用 "From 00 to 02 seconds" 敘述，專案驗證器 `check_prompt.py` 判定為「內文沒有任何時間碼」而 FAIL，且與 SEG-01 v04 的寫法不一致。v03 兩段各 6 個 beat，驗證器已通過。
2. **補上 `<Subject 2>` 排除宣告**。v02 只宣告 `<Subject 1>`，Picture 2／3 沒有對應 Subject。v03 沿用 SEG-01 v04 寫法，明確把 Cadi 標成「不出場的既有身分綁定」，驗證器警告只剩既有的 Picture 3 保留槽。
3. **刪掉影像生成殘留句**。v02 的 "Render a single 16:9 image at a time" 是靜態生圖用語，對影片模型是雜訊，已移除；視覺風格改由開頭一句話建立（符合 ref-en 的 style opening 規定）。
4. **retention_analysis 分段獨立**。v02 的 A／B 保留分析完全相同，A 裡還留著 "Phone stays pocketed until B" 這種 B 專用註記。v03 改成各寫各的出場範圍：B 註明 [Shot 2] 只剩左手、袖口與手錶，[Shot 3] 女主角不入鏡。
5. **補上 A 的開門動作與閉合筆電**。v02 起手是「門是關的」卻直接 "rushes through the doorway"，模型可能讓人穿門；v03 明寫 the door swings open into the corridor。筆電也依分鏡補成 closed dark laptop，避免沿用 SEG-01 的開蓋狀態。
6. **鏡頭語彙改用官方詞表**。tilts down with small amplitude at slow speed、static shot、pulls out with small amplitude、the shot cuts to；B 的 "match-cut" 改為官方允許的 cuts to，並用文字說明版面位置對齊。
7. **負面表列重整**。A 補 no readable text（A 本來就不該出現任何字）、no open laptop、no camera move through the glass；B 改為 no readable text beyond the specified interface，並保留 no translated or shortened messages、no garbled or invented Chinese characters。兩段都保留 registry 規定的 Cadi 專屬負面詞。
8. **字數壓回上限內**。v02 為 6780／6969 字元，v03 在補完上述內容後仍壓在 6991／6998（上限 7000）。作法是把「剪輯用」的說明（21 秒連續配樂、分開生成無法保證相位）移回本說明文件，提示詞只留模型需要知道的部分。

## 驗證結果

`python check_prompt.py segments/SEG-02/seg02-x-minimax-h3-prompt-v03.txt --registry cast_registry.yaml --segment seg02-x`

- A／B 皆為 10 passed, 1 warning, 1 failed。
- 唯一 FAIL 是既有專案例外：registry cast 只有 heroine／cadi 兩張圖，提示詞依 DECISIONS 固定宣告到 `<Picture 3>`（保留槽、未綁圖、禁止入鏡）。驗證器不認識 `reserved_unbound_picture`，SEG-01 同樣會 FAIL。
- 唯一 WARN 也來自同一個保留槽（Picture 3 沒有對應 Subject）。
- 本機 `check_prompt.py` 在 Python 3.10／3.11 會因 f-string 內含反斜線而 SyntaxError（需 3.12+）。本次以修補後的副本執行，未更動原始腳本。

## 分段（未變）

| 分段 | 正片範圍 | 內容 | 生成長度 | 保留範圍 |
|---|---|---|---|---|
| seg02-a | 00:24–00:33 | 門外可見飛紙、衝出關門、背靠門、嘆氣撥髮、手錶震動 | 362 幀／15.083 秒 | 前 216 幀／9 秒 |
| seg02-b | 00:33–00:45 | 看錶、開手機、RF 郵件、滿版群組抱怨 | 362 幀／15.083 秒 | 前 288 幀／12 秒 |

MiniMaxH3ReferenceToVideo／Ref2VA，24 FPS，16:9，seed 7201。

## 圖片上傳順序（兩段相同）

1. ref_image_0／`<Picture 1>`：assets/characters/Gemini_Generated_Image_6rilce6rilce6ril.jpg
2. ref_image_1／`<Picture 2>`：assets/characters/cadi Design Sheet.jpg（本段禁止出場，含群組頭像與 app 圖示）

`<Picture 3>` 僅保留固定英文宣告，不掛第三張圖，也不用 Storyboard 補槽。

## 接段（未變）

A 保留段最後：背靠關閉的門、右上臂夾閉合筆電、左手撥髮完成停在耳旁、左腕錶亮起、眼睛剛睜開。B 以相同 65mm 右前方近景重建同一狀態接放低手腕。不重演逃離、嘆氣、撥髮或震動。若生成後接縫不符，先取 A 保留段最後一張解碼影格作 B 的端點輸入，不可拿 15.083 秒餘裕尾幀當剪輯邊界。

## 音樂與剪輯（提示詞未寫的部分）

- 正式剪輯鋪一條連續 21 秒鼓聲軌；分開生成的音樂無法保證節拍相位吻合，現場音在接縫短淡化。
- B 的訊息提示音在第 5、7、9 秒，腳步在第 11 秒先行。

## UI 原文與驗收（未變）

郵件主旨：RF需求變更需求／預覽：半小時後開會／群組：Placement 討論

- 半小時討論!?? 我圖都還沒看怎麼開會!?
- 我placement 昨天晚上才搞定
- 完蛋了怎麼辦!!

生成後檢查：右臂筆電不換手且維持閉合、左腕手錶一致、窗內飛紙不跑到走廊、門確實關上且背靠門、三則泡泡不捲走。中文字若生成錯誤，以後製 UI 圖層依上述原文補正，不改寫或縮短。
