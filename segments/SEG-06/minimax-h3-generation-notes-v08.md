# SEG-06 H3 生成說明 v08

C新版：`seg06-c-minimax-h3-prompt-v04.txt`，六區段全文可直接貼入現行本地 Ref2VA 工作流。A／B沿用v04。

- 模式 Ref2VA；9秒／217幀；seed 7601；16:9。
- 正片取0–7秒，7–9秒為尾部停留。SEG-06暫計14＋10＋7＝31秒，待全片校時。
- ref_image_0／Picture 1：`assets/characters/agent3-drop.png`，身分。
- ref_image_1／Picture 2：`assets/software/alotofplacement.png`，縮圖、橘框、灰色板面及高亮零件的視覺語彙。部分沿用：候選可換位，只有推薦轉綠；標題區作低對比圖形，不要求可讀文字。
- ref_image_2／Picture 3：`assets/environments/純白房間.png`，建築與光線。
- 不掛影片或音訊參考。無台詞；112 BPM活潑電子配樂。
- 使用者2026-10-13確認表演方向並直接要求H3，記為本次製作授權。Storyboard未重製，主劇本保留。

驗收：相同零件在候選內換位；三個候選可辨；先回頭、再微調、後開心；6秒前殘影收乾淨；僅一個推薦方案轉綠；手與面板不遮臉；7–9秒穩定。

影片未生成；間隙與光路為視覺示意，工程正確性與推薦品質未驗證。文字檢查見 `validation-v08.json`。
