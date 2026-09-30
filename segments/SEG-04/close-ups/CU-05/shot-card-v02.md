# SEG-04-CU-05 特寫鏡頭製作卡 v02

依 `workflows/close-up/workflow-v02.md` v02 規則製作；v01 保留。

| 欄位 | 內容 |
|---|---|
| 完整鏡頭 ID／版本 | SEG-04-CU-05／v02 |
| 狀態與阻礙 | prompt_ready（文字檢查通過）；影片未生成；D 為估計值 |
| 說話者／逐字台詞 | Cadi：「再交給 AI Placement Planner 產生布局預覽，最後匯入 Creo 微調，檢查空間與散熱配置。」 |
| 聲音 | `in a bright, playful yet professional childlike female Mandarin voice`；使用者確認語速指令無明顯效果，故不另加語速詞 |
| 當鏡唯一角色／視線 | Cadi；畫面右側、眼平 |
| 背景 | `assets/environments/seg04-cu-background-eastside-crop-v01.png`（鏡位假設待確認） |
| D／T | D 估 8.5 秒（未實測）；T = 10.5 秒；以 11 秒生成 |
| 時間軸 | 0–1 靜音／1–10（尾音約 9.5 秒）／10–11 靜音停留 |
| 表情 | 承接上一鏡不停頓 → 說明布局預覽、Creo 微調與檢查 → 完成主要流程說明（沿用 v01，未新增事件） |
| 生成設定 | Ref2VA／11 秒（約 265 幀）／seed 7401；若 ComfyUI 固定 15 秒，只取 T 區間 |
| 音訊 | 僅逐字台詞；music = None. |
| 文字驗證／影片驗證 | 見 validation-v02.md／未生成 |

## 驗收

四項人工驗收未驗證：背景匹配／只含台詞／前後各 1 秒緩衝／畫面只有Cadi。
