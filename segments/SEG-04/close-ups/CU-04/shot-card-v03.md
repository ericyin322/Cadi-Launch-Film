# SEG-04-CU-04 特寫鏡頭製作卡 v03（語速加快）

依 `workflows/close-up/workflow-v02.md` v02 規則製作；v01 保留。

| 欄位 | 內容 |
|---|---|
| 完整鏡頭 ID／版本 | SEG-04-CU-04／v03 |
| 狀態與阻礙 | prompt_ready（文字檢查通過）；影片未生成；D 為估計值 |
| 說話者／逐字台詞 | Cadi：「我建議透過工作流提供的 MCP 工具，先取得最新 IEC Spec 和 GP 圖，確認變更參數，」（結尾逗號保留，下接 CU-05） |
| 聲音 | `bright, playful yet professional childlike female Mandarin voice at a brisk, quick pace`（使用者 2026-09-30 要求語速加快；音色同 CU-02） |
| 當鏡唯一角色／視線 | Cadi；畫面右側、眼平 |
| 背景 | 同 CU-02：`assets/environments/seg04-cu-background-eastside-crop-v01.png`（鏡位假設待確認） |
| D／T | D 估 6.5 秒（約 35 音節，較快語速約 5.5 音節／秒，逗號停頓縮短）；T = 8.5 秒；以 9 秒生成（多 0.5 秒尾端裁掉） |
| 時間軸 | 0–1 靜音／1–8 說話（尾音約 7.5 秒）／8–9 靜音停留（表情為「提案進行中」，好接 CU-05） |
| 生成設定 | Ref2VA／9 秒（約 217 幀）／seed 7401 |
| 音訊 | 僅逐字台詞；music = None. |
| 文字驗證／影片驗證 | 12 passed／1 warning／0 failed／未生成 |

## 驗收

四項人工驗收未驗證：背景匹配／只含台詞且為孩子氣女聲／前後各 1 秒緩衝／畫面只有 Cadi。與 CU-05 接點：語氣未收尾，剪輯時確認停頓長度自然。

## v03 變更

- 使用者要求 Cadi 語速加快：提示詞加 `at a brisk, quick pace` 與逗號僅微停頓；D 由 8.5 降為估 6.5 秒，生成由 11 秒降為 9 秒。v01、v02 保留。
- 注意：模型對語速指令的服從度不一定穩定，且與 CU-02／05／06 的語速可能落差；生成後實測，必要時其餘 Cadi 特寫也統一加快。
- CU-04～07 維持原拆法，不合併。
