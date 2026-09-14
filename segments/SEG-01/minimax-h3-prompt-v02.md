# 《半小時之內》SEG-01｜MiniMax H3 測試提示詞 v02

## 測試目的與生成規格

- 狀態：測試版；SEG-01 Storyboard v01 尚待集中審查，不視為正式 H3 完成版。
- 模型：MiniMax H3
- 模式：Ref2VA／本機 `MiniMaxH3ReferenceToVideo`
- 畫幅：16:9
- 幀率：24 FPS
- 原始劇情長度：24 秒
- 測試生成：H3-01A 15 秒＋H3-01B 15 秒；生成後剪輯至原定 24 秒。
- 連續方式：H3-01B 接收 H3-01A 實際輸出的末尾 5 幀作 opening guide；接合後移除 H3-01B 重複的前 5 幀。
- 音訊：H3 原生中文對白與會議室聲景；配樂後製統一鋪設。

## 圖片綁定

1. `<Picture 1>`＝`C:\Users\u\Documents\Codex\Cadi-Launch-Film\assets\characters\Gemini_Generated_Image_6rilce6rilce6ril.jpg`：女主角唯一身分、髮型、服裝、比例與氣質基準；不沿用設計表的排版、文字、色票、物件圖示或白色背景。
2. `<Picture 2>`＝`C:\Users\u\Documents\Codex\Cadi-Launch-Film\assets\characters\cadi Design Sheet.jpg`：Cadi 唯一身分、正側背比例、火焰頭、表情、深藍機器身體與胸口光核基準；不沿用設計表的排版、標題、中文字或白色背景。依專案規則必須綁定，但 Cadi 不得出現在 SEG-01 畫面。
3. `<Picture 3>`＝虛擬工廠；使用者尚未指定實體圖片路徑。本版逐字保留固定宣告，但 SEG-01 位於現實會議室，虛擬工廠不得入鏡；正式接線前仍需補上對應圖片。

`segments/SEG-01/storyboard-v01.png` 僅作提示詞撰寫時的離線構圖依據，不占用 `<Picture i>` 編號，也不接入 H3 參考圖片節點。

---

## H3-01A｜建立空間、要求疊加｜15 秒

```text
subject_definitions:
<Picture 1> is the female protagonist, a 20-something East Asian female mechanical R&D engineer. She has long, straight, center-parted black hair and wears a tailored taupe-gray blazer, an ivory crew-neck top, and loose light-colored trousers. She is professional, composed, and places a high value on immaculate grooming.
<Picture 2> is Cadi, a small flying robot mascot. Its head is composed of actively burning, ethereal cyan-blue plasma fire that continuously flickers, dances, and undulates with rising wisps and subtle luminous embers (an energetic plasma flame, completely non-solid, with zero gelatinous or jelly-like surface tension). Within the dynamic flame sit two oversized oval cyan eyes and a tiny mouth, atop a dark navy segmented robot body and a glowing circular cyan chest core. Its height is approximately half of the female protagonist's upper body.
<Picture 3> is the virtual factory, a near-future engineering city inspired by the street aesthetics of Taiwan and Hong Kong. It features a southern entrance observation deck, a central north-south floating transit lane, engineering service buildings lining both sides, warm vertical neon shapes, and cyan data light rails.

summary:
Create a 15-second live-action cinematic technology-brand video covering SEG-01 Shots 01 and 02: establish a cold gray external-client CAE review meeting, then show additional baseline, material-comparison, and two-point strength-ranking requests accumulating. Preserve the story events and dialogue exactly. Cadi <Picture 2> does not appear.

retention_analysis:
The female protagonist <Picture 1>: fully_preserved — preserve facial identity, long straight center-parted black hair, tailored taupe-gray blazer, ivory crew-neck top, loose light-colored trousers, body proportions, composed fatigue, and immaculate grooming. Do not copy the design-sheet layout, labels, accessory samples, or white background.
Cadi <Picture 2>: identity_reference_only — keep the required project binding, but render no Cadi, no blue flame, no robot, no mascot, and no cyan chest core in this segment.
<Picture 3>: environment_definition_only — preserve the required declaration, but render no virtual factory, observation deck, floating transit lane, engineering buildings, neon shapes, or cyan data rails in SEG-01.

detailed_description:
[Shot 1] Live-action cinematic technology brand film, 16:9, cool desaturated gray palette with natural skin tones and controlled projection highlights. A long conference table recedes like a corridor toward a large wall projection screen. The female protagonist <Picture 1> sits upright in the near-right foreground with an open notebook and pen. Preserve her exact face, long center-parted black hair, tailored taupe-gray blazer, ivory crew-neck top, and loose light-colored trousers from <Picture 1>. Several external clients sit farther down the table as anonymous dark backlit contours with absolutely no facial features. The projection shows a clean engineering layout for a mechanical top-compression CAE review: a simplified product geometry, two compression locations, and reserved title space for later compositing. A wall clock approaches the hour. The camera uses a 35mm wide view and slowly pushes forward along the table toward the female protagonist <Picture 1>, with small amplitude and steady speed. No one speaks during the first six seconds.

[Shot 2] At 00:06.000, cut to a 50mm over-the-table medium-wide composition. One featureless client silhouette extends a hand into the projector beam and points toward the engineering screen. A second baseline panel appears beside the first; two material swatches replace one another; simplified A-versus-B strength bars visibly exchange their high-low ranking. Keep all diagrams readable as shapes and color relationships, but reserve exact technical labels for post-production and generate no garbled text. An adult client voice (S1), businesslike and demanding, says in Mandarin Chinese: <d>[Chinese] Top Compression 請增加一組 Baseline，材料也換一版比較。</d> A second adult client voice (S2) follows without overlap: <d>[Chinese] A、B 兩個按壓點的強度排序，都請分開列清楚。</d> The female protagonist <Picture 1> remains upright at screen right, looks from the pointing hand to the newly added diagrams, and writes concise notes without interrupting. End on a stable composition with the client's hand still near the projection, both comparison panels visible, and the female protagonist <Picture 1> in the near-right foreground. No Cadi <Picture 2>, no virtual factory <Picture 3>, no visible faces on clients, no extra protagonist, no mirrored room, no deformed hands, no unreadable generated text, no subtitles, no logos, no design-sheet layouts, and no storyboard panel borders.

overall_soundscape:
A low projector-fan whir and steady air-conditioning hum compress the room. Soft pen strokes, restrained paper movement, and one quiet chair creak sit below the two client voices. Keep the room tone continuous across the internal cut and leave a short clean ambience tail after the second line.

non_diegetic_music:
N/A. Add the continuous score only in post-production.
```

**尾幀要求：** 客戶的手仍靠近投影光束；Baseline、材料比較與 A／B 排序圖同時可見；女主角 `<Picture 1>` 位於近景右側持筆記錄，準備接到疲憊表情中近景。

---

## H3-01B｜疲憊進入表情、被迫承接｜15 秒

```text
subject_definitions:
<Picture 1> is the female protagonist, a 20-something East Asian female mechanical R&D engineer. She has long, straight, center-parted black hair and wears a tailored taupe-gray blazer, an ivory crew-neck top, and loose light-colored trousers. She is professional, composed, and places a high value on immaculate grooming.
<Picture 2> is Cadi, a small flying robot mascot. Its head is composed of actively burning, ethereal cyan-blue plasma fire that continuously flickers, dances, and undulates with rising wisps and subtle luminous embers (an energetic plasma flame, completely non-solid, with zero gelatinous or jelly-like surface tension). Within the dynamic flame sit two oversized oval cyan eyes and a tiny mouth, atop a dark navy segmented robot body and a glowing circular cyan chest core. Its height is approximately half of the female protagonist's upper body.
<Picture 3> is the virtual factory, a near-future engineering city inspired by the street aesthetics of Taiwan and Hong Kong. It features a southern entrance observation deck, a central north-south floating transit lane, engineering service buildings lining both sides, warm vertical neon shapes, and cyan data light rails.

summary:
Create a 15-second live-action cinematic technology-brand continuation covering SEG-01 Shots 03 and 04: a third CAE request adds three drop-analysis corners and delivery times; the female protagonist <Picture 1> briefly reveals fatigue, restores her professional composure, and accepts the work with the exact dialogue. Cadi <Picture 2> does not appear.

retention_analysis:
The female protagonist <Picture 1>: fully_preserved — preserve the same face, long center-parted black hair, tailored taupe-gray blazer, ivory crew-neck top, loose light-colored trousers, seated position, screen direction, controlled fatigue, and professional demeanor from H3-01A. Do not copy the design-sheet layout, labels, accessory samples, or white background.
Cadi <Picture 2>: identity_reference_only — keep the required project binding, but render no Cadi, no blue flame, no robot, no mascot, and no cyan chest core in this segment.
<Picture 3>: environment_definition_only — preserve the required declaration, but render no virtual factory, observation deck, floating transit lane, engineering buildings, neon shapes, or cyan data rails in SEG-01.

detailed_description:
[Shot 1] Continue directly from the supplied five-frame opening guide from H3-01A without resetting pose, pen position, room geometry, projection brightness, camera axis, lighting, or color temperature. The female protagonist <Picture 1> is already seated at the near-right side of the same conference table and is already finishing the previous note. Preserve her exact face, long center-parted black hair, tailored taupe-gray blazer, ivory crew-neck top, and loose light-colored trousers from <Picture 1>. The camera cuts on her downward pen movement to a 65mm medium close-up from the same side of the table. Her back remains straight, but the pen tip pauses for half a beat. Her eyes move from the projection to the notebook, briefly to the wall clock, and back toward the clients. Behind her, the projection changes to a simplified Bellini Drop analysis: one product form with exactly three corners illuminating sequentially in the order RB, LB, RT, plus three clean delivery rows reserved for later compositing of 9/2 17:00, 9/8 17:00, and 9/10 17:00. Do not generate fake letters or numbers; preserve empty label areas for post-production. A third adult client voice (S3), calm but insistent, says in Mandarin Chinese: <d>[Chinese] 另外，請照 Bellini Drop 的條件跑 RB、LB、RT，並回覆各角落的完成時間。</d> During the line, the three corner markers and three delivery rows activate one by one. The female protagonist <Picture 1> listens without speaking; only the half-beat pen pause and a slightly shallower breath reveal fatigue.

[Shot 2] At 00:09.000, cut closer to an 85mm chest-up view of the female protagonist <Picture 1>, keeping the same screen direction and the same wall clock in the upper background. She contains one breath, lifts her right hand, tucks one loose strand of black hair behind her right ear, lowers that hand, and closes the same notebook with controlled precision. Her expression changes from momentary fatigue to a small courteous professional smile. In a calm adult female Mandarin voice (S4), with a tiny pause after the first word but no sarcasm, she says exactly: <d>[Chinese] 好。好，沒問題，我來處理。</d> On the final syllable, she maintains eye contact toward the off-camera clients. End with the notebook closed, her polite smile held, and the final word's audio tail continuing into the sound of a conference chair beginning to slide backward. No Cadi <Picture 2>, no virtual factory <Picture 3>, no visible faces on clients, no extra protagonist, no slouching, no exaggerated sadness, no backward time movement on the clock, no mirrored room, no deformed fingers, no unreadable generated text, no subtitles, no logos, no design-sheet layouts, and no storyboard panel borders.

overall_soundscape:
Continue the identical projector-fan whir and air-conditioning hum from H3-01A without a level change. Add quiet pen contact, a half-beat absence of pen sound, three restrained interface confirmation tones synchronized to the RB/LB/RT corner markers, soft fabric movement while hair is tucked behind the ear, the notebook closing, and a conference chair beginning to slide backward under the final dialogue tail. Dialogue remains dry, centered, and intelligible.

non_diegetic_music:
N/A. Add the continuous score only in post-production.
```

**首幀／尾幀要求：** 首幀沿用 H3-01A 實際尾端 5 幀，保持女主、筆、投影與攝影機方向；尾幀為同一本筆記本已合上、女主角 `<Picture 1>` 維持禮貌微笑，椅子剛開始後滑，準備銜接 SEG-02。

---

## 測試剪輯與驗收

- 先各自生成完整 15 秒；不要在生成前把對白加速。
- H3-01A 正片優先保留原劇情約 13 秒；H3-01B 正片優先保留原劇情約 11 秒，從無對白的停留與聲景尾端修剪，使 SEG-01 回到 24 秒。
- H3-01A → H3-01B：使用 A 的實際末尾 5 幀透過 `MiniMaxH3AddGuide` 接到 B 的 `frame_idx = 0`，完成後刪除 B 重複的前 5 幀再拼接。
- 兩段必須使用完全相同的 `<Picture 1>`～`<Picture 3>` 宣告、模型、解析度、24 FPS、色溫與曝光設定；`<Picture 3>` 的實體路徑待使用者補充。
- 技術標題、RB／LB／RT 與日期由後製精確疊加；H3 只生成結構清楚的圖形與留白區，避免亂碼。
- 接縫驗收：逐幀檢查女主臉、髮型、服裝、筆與筆記本位置、攝影機軸線、投影亮度、牆上時鐘、環境聲壓與視線方向。
- 若 5 幀 guide 仍造成動作停頓，改用末尾 22 幀並移除 B 對應的重複開場；不改寫劇情或台詞。
