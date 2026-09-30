# SEG-04-CU-02 特寫鏡頭製作卡 v02

依 `workflows/close-up/workflow-v02.md` v02 規則製作；v01 保留。

| 欄位 | 內容 |
|---|---|
| 完整鏡頭 ID／版本 | SEG-04-CU-02／v02 |
| 狀態與阻礙 | prompt_ready（文字檢查通過）；影片未生成；D 為估計值 |
| 使用者台詞來源／訊息日期 | 2026-09-30 SEG-04 對話，逐字沿用 v01 |
| 說話者／逐字台詞 | Cadi：「供電要從六相增加到八相，周邊元件的配置得跟著調整，散熱能力也需要重新評估。」 |
| 聲音 | `in a bright, playful yet professional childlike female Mandarin voice`（使用者 2026-09-30 指示：孩子氣的女聲；比專案統一句多一個 female） |
| 當鏡唯一角色／視線 | Cadi；畫面右側、眼平；構圖略偏左 |
| 背景原圖 | `assets/environments/6289735f-06d2-40a2-bb98-d253a20a5a8c.png` |
| 乾淨背景衍生圖 | `assets/environments/seg04-cu-background-eastside-crop-v01.png`，裁 (1060,0)–(1672,344)，612×344；已檢視：無角色、無可讀文字 |
| 背景鏡位 | 反打：Cadi 身後為與女主角背景（CU-01 高塔方向）不同的街區側；**為假設，待使用者確認** |
| 台詞 D 秒 | 估計 8.0 秒（約 33 音節、兩處句中停頓）；**未實測** |
| 目標素材長度 T = D+2 | 10 秒；0–1 靜音／1–9 說話／9–10 靜音停留 |
| 生成設定 | Ref2VA／10 秒（約 241 幀）／seed 7401；節點取整待查 |
| 音訊 | 僅逐字台詞；music = None. |
| 與 v01 差異 | 移除小點頭（不新增反應事件）、環境音與配樂、泛用平台描寫、對話對象敘述 |
| 文字驗證／影片驗證 | 12 passed／1 warning／0 failed／未生成 |

## 表演時間表

| 起訖秒 | 表現 | 台詞 | 剪輯備註 |
|---|---|---|---|
| 0–1 | 專注懸停，嘴閉，火焰持續流動 | 靜音 | 剪接緩衝 |
| 1–9 | 條理清楚地說明供電、佈局、散熱三點 | 完整台詞 | 首音前 1 秒起取 |
| 9–10 | 嘴閉，沉穩專注，同一視線與位置 | 靜音 | 尾音後 1 秒停留 |

## 實際參考素材

| 檔案 | 用途 | 插槽 | 邊界 |
|---|---|---|---|
| assets/characters/cadi_red.png | 身分 | ref_image_0／Picture 1 | 紅焰 canonical；不帶入排版與白底 |
| assets/environments/seg04-cu-background-eastside-crop-v01.png | 背景 | ref_image_1／Picture 2 | 繪製風格參考，成片畫風以 project.visual_style 為準 |

## 驗收

四項人工驗收未驗證：背景匹配／全段只含台詞且聲線為孩子氣女聲／前後各 1 秒緩衝／畫面只有 Cadi。
