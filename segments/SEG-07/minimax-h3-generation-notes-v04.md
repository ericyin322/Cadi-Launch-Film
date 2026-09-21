# SEG-07 場景 v02／B 段站姿修訂 v04

2026-09-21；依使用者要求建立新版本，v03 與更早版本保留。

- A／B 改用 `assets/environments/virtual-factory-description-v02.txt` 與 `assets/environments/virtual-factory-usage-v02.md`；工廠維持純文字，不占圖片索引。
- B 段女主角由坐姿改為站姿：她站在工作區近左側、面向發光布局，Cadi 在她與布局近左角之間邀請評估；提示詞不再提及躺椅或坐姿。
- A 14 秒、B 12 秒、seed 7701、指定台詞、參考圖順序及 `<Video 1>` 用途不變。
- 上傳順序與模式見 `reference-manifest-v04.json`；角色與場景規格快照見 `cast-registry-v04.yaml`。
- 影片尚未生成驗收。

## 驗證

- `.agents/skills/h3-scene-prompt/scripts/check_prompt.py`：A 13 項通過、B 14 項通過；兩段均 0 警告、0 失敗。A 6947 字元，B 6974 字元。
