# SEG-08-CU-01 驗證 v02

## 機器檢查

命令：

`python -X utf8 .agents/skills/h3-scene-prompt/scripts/check_prompt.py segments/SEG-08/close-ups/CU-01/seg08-cu01-minimax-h3-prompt-v02.txt --registry segments/SEG-08/close-ups/CU-01/cast-registry-v02.yaml --segment seg08-cu01`

結果：13 passed／0 warnings／0 failed，提示詞 6,717 字元。

## 人工文字檢核

- 通過：逐字台詞維持「好的，我們把它實際畫出來吧」。
- 通過：台詞尾音明定於 5.5 秒結束，早於 6 秒；5.5–6 秒為閉嘴微笑停頓。
- 通過：6.0 秒才開始抬右手與彈指動作；7.0 秒手指接觸；7–8 秒完整停留一秒。
- 通過：第一幀、說話全程、彈指準備、接觸與最後停留皆明定維持友善微笑。
- 通過：7.0 秒只有一次響亮、清脆彈指爆裂聲，帶明顯白色硬質房間回音與自然衰減尾音。
- 通過：只有 Cadi 與既有純白房間兩個實際參考；索引連續，未召喚未出鏡角色。
- 通過：現行紅焰 Cadi canonical／retention 與 `project.visual_style` 逐字一致。
- 通過：音軌只含台詞與使用者指定彈指聲；無配樂、無其他環境音。

## 影片檢核

未生成，以下項目未驗證：Cadi 全程微笑／台詞是否確實在6秒前說完／6秒前手部保持靜止／彈指動作可讀性／7秒聲畫同步／彈指音量與回音強度／7–8秒完整停留／嘴型、身分與背景一致性。

