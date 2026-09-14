# 《半小時之內》SEG-03｜S03a MiniMax H3 Ref2VA 提示詞 v01

## 生成規格

- 狀態：S03a 測試版；SEG-03 Storyboard v01 仍待集中審查。
- 覆蓋劇情：鏡頭 09–10（00:45–00:58），生成後剪輯保留約 13 秒。
- 模式：Ref2VA
- 畫幅：16:9，768p
- 幀率與長度：24 FPS，362 frames，15.083 秒
- Seed：7301
- 參考圖只掛女主角與 Cadi，不掛其他角色或場景圖。

## Ref2VA 上傳順序

1. `ref_image_0` → `<Picture 1>`／`<Subject 1>`：`assets/characters/Gemini_Generated_Image_6rilce6rilce6ril.jpg`
2. `ref_image_1` → `<Picture 2>`／`<Subject 2>`：`assets/characters/cadi Design Sheet.jpg`

```text
subject_definitions:
<Subject 1> is the female protagonist, a 20-something East Asian female mechanical R&D engineer. She has long, straight, center-parted black hair and wears a tailored taupe-gray blazer, an ivory crew-neck top, and loose light-colored trousers. She is professional, composed, and places a high value on immaculate grooming. Her face, hair, and clothing follow <Picture 1>.
<Subject 2> is Cadi, a small flying robot mascot. Its head is composed of actively burning, ethereal cyan-blue plasma fire that continuously flickers, dances, and undulates with rising wisps and subtle luminous embers (an energetic plasma flame, completely non-solid, with zero gelatinous or jelly-like surface tension). Within the dynamic flame sit two oversized oval cyan eyes and a tiny mouth, atop a dark navy segmented robot body and a glowing circular cyan chest core. Its height is approximately half of the female protagonist's upper body. Its design, proportions, and colors follow <Picture 2>.

summary:
[reference generation] Create a 15.083-second live-action cinematic technology-brand clip covering SEG-03 Shots 09 and 10. The exhausted but composed engineer reaches her workstation, connects her laptop, calls Cadi, and watches Cadi spring from the interface already aware of the new task. Only the female protagonist and Cadi appear.

retention_analysis:
<Subject 1> is fully preserved from <Picture 1>: fully preserved: her facial features, long straight center-parted black hair, tailored taupe-gray blazer, ivory crew-neck top, loose light-colored trousers, body proportions, professional composure, and immaculate grooming must remain consistent. Do not copy the design-sheet layout, text, color swatches, object icons, or white background.
<Subject 2> is fully preserved from <Picture 2>: fully preserved: its actively burning cyan-blue plasma fire head, continuous flickering combustion, soft rising flame tongues, subtle luminous embers, wind-drag during movement, upward licking and dissipation while hovering, oversized oval cyan eyes, tiny mouth, dark navy segmented robot body, body proportions, and glowing circular cyan chest core must remain consistent. Do not copy the design-sheet layout, title, Chinese text, or white background.

detailed_description:
[Shot 1, 0:00] Live-action cinematic technology brand film, 16:9, 768p. Continue the forward momentum from the office corridor into a cool-gray open-plan engineering office. The camera retreats smoothly at walking speed on a 35mm lens, waist-high and directly ahead of the female protagonist <Picture 1> (<Subject 1>). She enters alone carrying her open laptop, visibly tired but upright and professionally composed. Her long straight center-parted black hair, taupe-gray blazer, ivory top, and light trousers remain immaculate. Neutral overhead office light is softened by a cyan monitor glow ahead; no coworkers or background people are visible.

0:03 The camera continues backward as <Subject 1> reaches her assigned desk, pivots naturally toward the chair, and sits in one uninterrupted movement. She places the laptop squarely beside the workstation keyboard; the chair rolls only a few centimeters and stops. Her gaze stays on the dark central monitor.

0:06 Cut on the laptop placement to a 50mm front-right medium shot. <Subject 1> presses the workstation wake key with her right hand while her left hand inserts one laptop cable into the dock. The monitor wakes with abstract cyan interface geometry and no readable text. She leans slightly forward, looks directly at the screen, and says in a tired but familiar adult female Mandarin voice: <d>[Chinese] Hi，Cadi。</d>

0:09 A pinpoint cyan glow ignites at the exact center of the monitor and expands into actively burning, ethereal cyan-blue plasma fire. Cadi <Picture 2> (<Subject 2>) springs forward from the interface in one clean arc toward a small holographic platform above the desk. The completely non-solid flame head continuously flickers, dances, and undulates; soft flame tongues stream backward with the jump and shed subtle luminous embers that fade before reaching the desk.

0:12 <Subject 2> decelerates above the holographic platform, makes one light buoyant landing gesture without touching the surface, then hovers at the seated engineer's chest height. As motion stops, the plasma flame ceases trailing, licks upward, continuously dances, and softly dissipates at the tips. Its cyan eyes brighten and its glowing circular chest core pulses once. In a clear, playful, professional young-girl Mandarin voice, Cadi says exactly: <d>[Chinese] 妳開完會啦？我已經知道那件事囉。</d>

0:14 The camera settles into a stable 50mm two-shot from the engineer's front-right. <Subject 1> remains seated and slightly forward, her right hand resting beside the keyboard and her eyes fixed on <Subject 2>; recognition begins to replace fatigue. <Subject 2> finishes the line while hovering at her front-left, arms relaxed, chest core steady, and completely non-solid flame tips rising and dissolving. Hold this precise position, pose, camera axis, cool overhead light, cyan screen light, and emotional state for the S03b continuation.

No reverse motion, no backward walking, no looping, no mid-shot freeze, no readable text, no subtitles, no logos, no duplicate characters, no background people, no extra robots, no virtual factory, no deformed limbs, no object penetration, no mirrored layout, no sudden laptop or cable disappearance, no rubbery, gelatinous, solid jelly texture, no solid glass surface, no frozen flame, no rigid flame shell, and no copied design-sheet layout.

overall_soundscape:
Continuous restrained open-plan office ambience with distant ventilation and a low computer fan, but no audible coworkers. Footsteps and fabric movement lead into a soft chair-roll stop, laptop placement, one clean cable click, and a quiet workstation wake tone. The engineer's greeting is close and natural. Cadi's emergence adds a compact cyan plasma shimmer and a short holographic lift tone; the sound moves from the monitor center toward the desk platform. Cadi's Mandarin reply is clear, childlike, playful, professionally articulated, and never overlaps the engineer. No other voices occur.

non_diegetic_music:
N/A
```

## 尾幀與剪輯要求

- 尾幀：女主坐在工作位並微微前傾，右手停在鍵盤旁，視線對準前左方的 Cadi；Cadi 在女主胸口高度穩定懸停，胸口光核回到穩定亮度，火焰向上舔動並消散。
- S03a 正片優先保留原分鏡 00:45–00:58 約 13 秒；從開場行走或尾端穩定停留修剪，不壓縮三句對白。
- S03b 以相同 seed 7301、相同參考圖順序與上述尾幀 state anchor 續接。
