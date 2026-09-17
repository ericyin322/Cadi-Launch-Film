---
name: h3-prompt-writing
description: Write MiniMax H3 video generation prompts for T2VA, I2VA, FL2VA, L2VA, and Ref2VA. Use when rewriting multimodal requests into H3 prompt structures, composing integrated_multimodal_description, overall_soundscape, and non_diegetic_music, aligning keyframes, or defining reference labels for images, videos, and audio.
compatibility: Portable to any agent that can read local files — no external API calls, MiniMax Hub tools, or proprietary runtime required. The agents/openai.yaml file only adds optional ChatGPT/Codex UI metadata; it does not restrict the skill to OpenAI agents.
---

# H3 Prompt Writing

## Workflow

1. Identify the input mode: T2VA, I2VA, FL2VA, L2VA, or full-reference Ref2VA.
2. For base text/keyframe modes, read `references/base-en.txt` and follow its final prompt structure.
3. For full-reference mode, read `references/ref-en.txt` and follow its six-section rewrite format.
4. Preserve the exact field names, section order, labels, and timing notation from the selected guide.

## Base Modes

- T2VA: build the full audiovisual timeline from text.
- I2VA: start from the first frame and develop forward from it.
- FL2VA: describe the continuous path between the first and last frames.
- L2VA: infer a plausible opening and converge to the supplied last frame.

Use `integrated_multimodal_description`, `overall_soundscape`, and `non_diegetic_music` in the order shown in `references/base-en.txt`.

## Full-Reference Mode

Ref2VA rewrites use `subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape`, and `non_diegetic_music` in that order. Reference labels stay consistent across all sections.

Read `references/ref-en.txt` for label rules, retention analysis, and complete examples.

## Absent Objects (hard rule)

H3 has no negation operator. A text encoder turns `no Cadi`, `the excluded mascot` and
`absent from every shot` into the same embedding as `Cadi`: the model sees the noun and
renders it. Ref2VA makes this worse, because uploading a reference image is itself a
direct instruction to place that subject in the video. A "reserved" or "excluded" slot
therefore summons the subject even when no text mentions it.

1. Only cast members that actually appear get a `<Picture N>` / `<Subject N>` slot. Do
   not upload a reference image for an absent subject and do not reserve an index for
   one. Indices stay contiguous from 1 and match the uploaded `ref_image_{N-1}` slots.
2. Never name an absent object anywhere in the prompt: not in `subject_definitions`, not
   in `retention_analysis`, not in the negative list. Exclusion declarations do not
   exist; there is no phrasing that makes one safe.
3. Cross-segment identity consistency comes from a fixed seed plus verbatim reuse of the
   registry `canonical` text in the segments where the subject does appear. It never
   comes from carrying a ghost slot through the segments where it does not.
4. Negative lists may contain only rendering defects and frame-level attributes, such as
   `no subtitles`, `no readable text`, `no extra fingers`, `no deformed limbs`,
   `no shaky camera`, `no slow motion`, `no looping`. They may not contain object nouns.
5. Registry `extra_negatives` apply only while that asset is in the cast. They constrain
   how a present subject must not look; they never assert that a subject is absent.
6. To hold a present object in a state, write it positively: `the laptop stays closed`,
   not `no open laptop`.

Wrong — every line below drags the object into frame:

    <Subject 2> is the excluded mascot defined by <Picture 2>, not an on-screen performer.
    <Picture 3> is a reserved project declaration only: no third image is supplied or used in this scene.
    <Subject 2> / <Picture 2>: unused and absent from every shot and reflection.
    Negative constraints: ... No Cadi <Picture 2>, no virtual factory <Picture 3>, no robot or blue flame.

Right — the absent subjects are simply not present in the prompt at all, only
`<Picture 1>` / `<Subject 1>` is declared, and `ref_image_0` is the only upload:

    <Subject 1> is the female protagonist ... Her face, hair and clothing follow <Picture 1>.
    Negative constraints: no subtitles, no readable text, no extra fingers or limbs, no duplicate heroine, no shaky camera.

`scripts/check_prompt.py` enforces rules 1-4.


## Project Visual Style (hard rule)

A reference image carries its own rendering style into the video. Character design
sheets and storyboards are drawings, so "derive the style from the reference image"
turns a live-action project into 2D animation.

1. When the registry defines `project.visual_style`, the style opening of
   `detailed_description` is that sentence copied verbatim. Never infer style from
   `<Picture N>`.
2. Describe style only positively (`real skin, real fabric, real lighting`). Never write
   that the reference's drawing style, design-sheet layout or storyboard look is
   "replaced", "ignored" or "not copied": the noun is what the model reads.
3. In a live-action project, style words such as `2D`, `animation`, `cel shading`,
   `drawing style`, `illustrated`, `cartoon`, `anime`, `manga`, `sketch`, `line art`,
   `design sheet` and `storyboard` must not appear anywhere in the prompt.
4. Prefer a photographic reference image for identity; a drawn design sheet keeps
   pulling the render toward illustration no matter what the text says.

`scripts/check_prompt.py` enforces rules 1 and 3.

## Cadi 現行色系（本專案，2026-09-17 起）

- 新製作以根目錄 `cast_registry.yaml` 的 `assets.cadi.file`、`canonical` 與 `retention` 為準；身分圖為 `assets/characters/cadi_red.png`。紅橙火焰、暖白焰心與眼光、深灰機甲、紅色點綴及金橙胸核為現行色系。畫風仍逐字使用 `project.visual_style`。
- 保留持續燃燒、非固體、火舌上升、微光餘燼、移動拖曳及懸停消散的動態。新提示詞只正向描述現行色系，不寫「藍色改紅色」或排除舊色的句子。
- 既有 H3 提示詞與對應的分段 registry、manifest、生成說明都是歷史快照，本次不回改，也不因共用 registry 更新而批次重製。
- 日後新增或重製時，從根目錄取得最新 Cadi 規格，建立下一版分段 registry 與 manifest；不得直接沿用舊快照的 Cadi 色系或圖片路徑。保留該段專屬身高／出場設定，繼續遵守 Absent Objects。

## Output Rules

- Write rewrite sections in English; preserve dialogue, lyrics, and visible scene text in their original language.
- Describe each shot by composition, subjects, environment, actions, camera, sound, and the exact point where referenced content appears.
- Avoid plot summaries, unresolved reference labels, and timing that does not match the requested duration.
- Never mention, negate, exclude or reserve a subject that does not appear; see "Absent Objects" above.
## Tips for Better Results
- Always match the total duration of the description to the requested video length (4–15 seconds).
- Keep reference labels consistent (e.g. `<Picture 1>`, `<Video 1>`, `<Audio 1>`) across every section.
- Prefer concrete visual and audio details over abstract words like "cinematic" or "beautiful".
- When using keyframes (I2VA / FL2VA / L2VA), clearly state how the first and/or last frame connects to the timeline.
