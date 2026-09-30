# SEG-04-CU-07 特寫鏡頭製作卡 v02

依 `workflows/close-up/workflow-v02.md` v02 規則製作；v01 保留。

| 欄位 | 內容 |
|---|---|
| 完整鏡頭 ID／版本 | SEG-04-CU-07／v02 |
| 狀態與阻礙 | prompt_ready（文字檢查通過）；影片未生成；D 為估計值 |
| 說話者／逐字台詞 | 女主角：「可以，就照這個計畫開始。」 |
| 聲音 | `calm, decisive adult female Mandarin voice with natural professional pacing`；使用者確認語速指令無明顯效果，故不另加語速詞 |
| 當鏡唯一角色／視線 | 女主角；畫面左側、眼平 |
| 背景 | `assets/environments/seg04-cu-background-tower-crop-v01.png`（鏡位假設待確認） |
| D／T | D 估 2.7 秒（未實測）；T = 4.7 秒；以 5 秒生成 |
| 時間軸 | 0–1 靜音／1–4（尾音約 3.7 秒）／4–5 靜音停留 |
| 表情 | 收到完整提案 → 短促點頭並核准 → 堅定收尾（沿用 v01，未新增事件） |
| 生成設定 | Ref2VA／5 秒（約 121 幀）／seed 7401；若 ComfyUI 固定 15 秒，只取 T 區間 |
| 音訊 | 僅逐字台詞；music = None. |
| 文字驗證／影片驗證 | 見 validation-v02.md／未生成 |

## 驗收

四項人工驗收未驗證：背景匹配／只含台詞／前後各 1 秒緩衝／畫面只有女主角。
