# SEG-04-CU-08 驗證 v01

## 機器檢查

命令：

`python -X utf8 .agents/skills/h3-scene-prompt/scripts/check_prompt.py segments/SEG-04/close-ups/CU-08/seg04-cu08-minimax-h3-prompt-v01.txt --registry segments/SEG-04/close-ups/CU-08/cast-registry-v01.yaml --segment seg04-cu08`

結果：12 passed／1 warning／0 failed，提示詞 5,823 字元。

唯一警告為「只有約 3 個 beat；15 秒建議 5–6 個」。本鏡實際為 6 秒單鏡頭，依特寫工作流刻意使用 0–1／1–5／5–6 三段，警告不構成失敗。

## 人工文字檢核

- 通過：台詞逐字等於使用者原文「收到指令，開始進行，我來招集夥伴! 」。
- 通過：只有 Cadi 與已檢視的東側街區背景兩個實際參考，索引連續。
- 通過：畫風逐字取自 `project.visual_style`。
- 通過：單一 Cadi 上半身特寫；未提及或上傳畫外角色。
- 通過：聲線明確為高昂、有活力、孩子氣女性國語聲線；未加入語速指令。
- 通過：點頭、右拳貼胸、挺直雙肩、胸核亮起、右拳高舉、左手叉腰與抬頭均為可觀察的自信動作。
- 通過：音軌僅指定台詞；前後各一秒靜音；配樂為 None。
- 通過：背景圖已檢視，無人物、無可讀文字。

## 影片檢核

未生成，以下項目未驗證：Cadi 身分與火焰／背景匹配／嘴型同步／高昂聲線／純人聲無底噪／首尾各一秒可用緩衝／畫面單一角色／自信動作完成度。

