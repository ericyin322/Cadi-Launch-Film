# SEG-04-CU-01 驗證 v02

- 日期：2026-09-30
- 檢查器：`.agents/skills/h3-scene-prompt/scripts/check_prompt.py`
- prompt：`seg04-cu01-minimax-h3-prompt-v02.txt`／registry：`cast-registry-v02.yaml`／segment：`seg04-cu01`
- 結果：12 passed／1 warning／0 failed；字元數 4393／7000
- 警告：「只有約 3 個 beat；15 秒建議 5-6 個」——舊固定時長假設，v02 規定不套用，已人工核對 3 個 beat 對應 D+2 結構。
- 上傳索引：ref_image_0 → Picture 1／Subject 1（女主角）；ref_image_1 → Picture 2／Subject 2（乾淨背景）
- 人工檢核（文字）：台詞逐字一致；只有女主角出鏡；未提及對話對象；soundscape／music 依 v02；無畫風禁字；背景圖已檢視、無角色無文字。
- 影片檢核：未生成。背景匹配、純對白、前後緩衝、單人畫面四項均未驗證。
