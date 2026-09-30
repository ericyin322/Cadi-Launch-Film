# SEG-10-CU-01 驗證 v01

## 機器檢查

命令：

`python -X utf8 .agents/skills/h3-scene-prompt/scripts/check_prompt.py segments/SEG-10/close-ups/CU-01/seg10-cu01-minimax-h3-prompt-v01.txt --registry segments/SEG-10/close-ups/CU-01/cast-registry-v01.yaml --segment seg10-cu01`

結果：12 passed／1 warning／0 failed，提示詞 4,897 字元。

唯一警告為「只有約 3 個 beat；15 秒建議 5–6 個」。本鏡實際為 9 秒單鏡頭，依特寫工作流刻意使用 0–1／1–8／8–9 三段，警告不構成失敗。

## 人工文字檢核

- 通過：台詞逐字等於使用者原文。
- 通過：只有女主角與 `dock.png` 兩個實際參考，索引連續。
- 通過：畫風逐字取自 `project.visual_style`。
- 通過：單人固定機位臉部特寫；未提及或上傳畫外角色。
- 通過：音軌僅指定台詞；前後各一秒靜音；配樂為 None。
- 通過：`dock.png` 已檢視，無人物、無可讀文字。

## 影片檢核

未生成，以下項目未驗證：女主角身分／背景匹配／嘴型同步／`cover` 發音／純人聲無底噪／首尾各一秒可用緩衝／畫面單一角色。
