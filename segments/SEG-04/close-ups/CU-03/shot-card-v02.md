# SEG-04-CU-03 特寫鏡頭製作卡 v02

依 `workflows/close-up/workflow-v02.md` v02 規則製作；v01 保留。

| 欄位 | 內容 |
|---|---|
| 完整鏡頭 ID／版本 | SEG-04-CU-03／v02 |
| 狀態與阻礙 | prompt_ready（文字檢查通過）；影片未生成；D 為估計值 |
| 使用者台詞來源／訊息日期 | 2026-09-30 SEG-04 對話，逐字沿用 v01 |
| 說話者／逐字台詞 | 女主角：「那就先擬一份評估計畫。」 |
| 聲音 | `calm, decisive adult female Mandarin voice with natural professional pacing`（同 CU-01） |
| 當鏡唯一角色／視線 | 女主角；畫面左側、眼平 |
| 背景 | 與 CU-01 v02 相同：`assets/environments/seg04-cu-background-tower-crop-v01.png`（女主角方向背景，鏡位假設待確認） |
| 台詞 D 秒 | 估計 2.5 秒（10 音節）；**未實測** |
| 目標素材長度 T = D+2 | 4.5 秒；以 5 秒生成（節點最短 4 秒），多 0.5 秒在尾端裁掉 |
| 時間軸 | 0–1 靜音／1–4 說話（尾音約在 3.5 秒，其後閉嘴靜音）／4–5 靜音停留 |
| 生成設定 | Ref2VA／5 秒（約 121 幀）／seed 7401 |
| 音訊 | 僅逐字台詞；music = None. |
| 表情 | 聽完後立即做決定 → 語氣果斷 → 視線穩定等待計畫（沿用 v01，未新增事件） |
| 文字驗證／影片驗證 | 12 passed／1 warning／0 failed／未生成 |

## 實際參考素材

| 檔案 | 用途 | 插槽 |
|---|---|---|
| assets/characters/heroine-photo-reference-v01.png | 身分 | ref_image_0／Picture 1 |
| assets/environments/seg04-cu-background-tower-crop-v01.png | 背景 | ref_image_1／Picture 2 |

## 驗收

四項人工驗收未驗證：背景匹配／只含台詞／前後各 1 秒緩衝（尾端實際取用區間以尾音後 1 秒為準）／畫面只有女主角。
