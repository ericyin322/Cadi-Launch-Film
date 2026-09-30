# SEG-08-CU-01 驗證 v01

## 機器檢查

命令：

`python -X utf8 .agents/skills/h3-scene-prompt/scripts/check_prompt.py segments/SEG-08/close-ups/CU-01/seg08-cu01-minimax-h3-prompt-v01.txt --registry segments/SEG-08/close-ups/CU-01/cast-registry-v01.yaml --segment seg08-cu01`

結果：13 passed／0 warnings／0 failed，提示詞 5,718 字元。

## 人工文字檢核

- 通過：台詞逐字等於使用者原文「好的，我們把它實際畫出來吧」。
- 通過：只有 Cadi 與 `assets/environments/純白房間.png` 兩個實際參考，索引連續。
- 通過：純白房間圖已檢視，無人物、無可讀文字，與 SEG-08 現行 H3 使用相同素材。
- 通過：畫風逐字取自 `project.visual_style`；Cadi canonical／retention 使用現行紅焰規格。
- 通過：固定單一 Cadi 上半身特寫，嘴部及右手全程清楚；未提及或上傳未出鏡角色。
- 通過：1–4 秒完整台詞；4–5 秒僅在台詞結束後執行彈指；5.0 秒單次彈指聲同步；5–6 秒完整停留一秒。
- 通過：音軌只含指定台詞與使用者要求的一次彈指聲；其餘時段靜音；配樂為 None。

## 影片檢核

未生成，以下項目未驗證：Cadi 身分與火焰／純白房間匹配／嘴型同步／台詞實測 D／彈指手勢可讀性／彈指聲同步／彈指後完整一秒停留／其他時段無底噪／畫面單一角色。

