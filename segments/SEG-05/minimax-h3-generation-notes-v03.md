# SEG-05｜H3 生成說明 v03

驗證：A／B 各13項通過、0警告、0失敗；六個連續beat分別覆蓋14秒與12秒。已額外核對提示詞沒有女主角、躺椅、飲料或另一段Agent的引用，DLG-10–13字詞與順序完整保留。

使用 h3-prompt-writing；依使用者本次動作修訂及 brief v03。Storyboard v02 已過時，本次依直接要求製作提示詞，影片尚未生成。

| 提示詞 | 時長 | 上傳 Picture 1 / ref_image_0 | 上傳 Picture 2 / ref_image_1 |
|---|---:|---|---|
| seg05-a-minimax-h3-prompt-v03.txt | 14秒 | assets/characters/cadi Design Sheet.jpg | assets/characters/agent2-hapa.png |
| seg05-b-minimax-h3-prompt-v03.txt | 12秒 | assets/characters/cadi Design Sheet.jpg | assets/characters/agent1-hana.png |

兩段均為 Ref2VA、16:9、seed 7501；每段只上傳表列兩張。女主角、躺椅與飲料不出場，不掛圖也不在模型提示詞中提名。A沒有hana，B沒有hapa。圖片索引為各段本地索引，因此 Picture 2 隨段落更換。

A：0–4秒Cadi接管；4–11秒完整派工；11–12秒hapa回應；12–14秒hapa向左飛出畫面。B：0–6秒完整派工；6–7秒hana回應，7–8秒向右飛出畫面；8–12秒攝影機環繞Cadi約180度，停在其背後，準備前往下一站。保留原26秒時槽，語速及起飛節奏仍需成片驗收。

A尾接B首：Cadi左手收下、轉向右方。B末：Cadi背面、前傾懸停，北向航道向畫面深處延伸。環繞保持地平線水平、半徑穩定；「旋轉」是攝影機繞角色移動。

本版獨立驗證檔：cast-registry-v03.yaml。沿用主registry的畫風、身分及配色；僅移除Cadi canonical 中引用女主角身高的比較句，以遵守未出場物件不提名規則。主registry的其他段落canonical保留。檢查時使用本段registry路徑。

配樂沿用112 BPM輕快器樂，保留清楚國語對白、低環境聲及向左右移動的短促飛行聲；末鏡音樂稍微抬起。不新增台詞。依實際H3節點設定14秒／12秒，檢查器預設frames不作為實際生成幀數。
