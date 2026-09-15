# 專案工作規則

- 所有回覆與製作文件以繁體中文為主。
- 先讀 `README.md`、`PROGRESS.md`、`PROJECT_STATE.json` 與 `screenplay/DECISIONS.md`。
- 劇情內容以 `screenplay/master-storyboard-v0.7.md` 為唯一來源；未經使用者授權不得改寫劇情。
- 修改某個 SEG 時只處理該 SEG；除非連續性受到影響，否則不要改動其他段落。
- 新版本不得覆蓋舊檔，使用 `v02`、`v03` 依序增加。
- 新增分段可先使用 `SEG-xxA`；同步更新 `PROGRESS.md`、`PROJECT_STATE.json` 與 `CHANGELOG.md`。
- Cadi、主角、Creo 與畫風參考均以 `assets/ASSET_INDEX.md` 的用途邊界為準。
- Storyboard 為黑白前期圖；最終影片視覺是彩色、寫實真人電影質感的台港科幻工程街區。
- H3 提示詞的畫風一律逐字取自 `cast_registry.yaml` 的 `project.visual_style`，不得從參考圖推斷；提示詞不得出現 2D／animation／cel／drawing／illustration／design sheet／storyboard 等字眼，也不寫「參考圖畫風被取代」這類否定句（提到就會被畫出來）。女主角身分圖改用 `assets/characters/heroine-photo-reference-v01.png`。
- MiniMax H3 提示詞必須獨立存於對應 SEG 目錄，且僅在該段 Storyboard 確認後製作。
- 該段沒出場的角色或場景：不上傳參考圖、不編 `<Picture N>` 索引、提示詞一個字都不提；沒有排除宣告也沒有保留槽（H3 無否定運算子，提到就會被畫出來）。詳見 `.agents/skills/h3-scene-prompt/SKILL.md` 的 Absent Objects 一節，由 `check_prompt.py` 強制。






