# SEG-11 MiniMax H3 A／B v04 使用說明（C 沿用 v03）

依 2026-09-23 使用者指示更新 A／B；正式來源 `screenplay/master-storyboard-v0.25.md`。v01–v03 全數保留。

## 分段

| 段落 | 檔案 | 時長 | 內容 |
|---|---|---:|---|
| A | `seg11-a-minimax-h3-prompt-v04.txt` | 13秒 | Ray 殘影高速進房、DLG-30 交付膠囊；Finn 掃描、DLG-31；膠囊丟入煉丹爐 |
| B | `seg11-b-minimax-h3-prompt-v04.txt` | 13秒 | 煉丹爐觀察窗與爐身特寫轟鳴；Ray 驚訝；9秒爆鳴硬切；Finn 開爐取丹交給 Ray |
| C | `seg11-c-minimax-h3-prompt-v03.txt` | 13秒 | 不變 |

## 上傳順序（A、B 相同）

| 圖片／插槽 | 檔案 |
|---|---|
| Picture 1／ref_image_0 | `assets/characters/agent5-ray.png` |
| Picture 2／ref_image_1 | `assets/characters/agent4-finn.png` |
| Picture 3／ref_image_2 | `assets/environments/科技煉丹爐.jpg` |

C 的上傳順序同 v03（女主角、紅焰 Cadi、Ray）。seed 8101。

## 與 v03 的差異

- 研究所由文字場景改為圖片參考房間；煉丹爐是房間中央的爐體（非多層樓高巨爐），取消揭露運鏡與側邊艙門。
- A：Ray 由右側殘影衝入（承接 SEG-10 B v05 左側離鏡）；道具統一為 SEG-10 的暖白＋青色資料膠囊；結尾 Finn 把膠囊拋入觀察窗。
- B：全段集中在煉丹爐特寫與轟鳴；爆鳴時點由10秒提前到9秒，結果改由 Finn 從觀察窗內取出。

## 風險提醒

`科技煉丹爐.jpg` 是繪製風格圖，且含招牌與標籤文字。依專案規則，畫風句逐字取 `project.visual_style`、提示詞只正向描述實體材質，不提圖中文字；但參考圖仍可能把畫面往插畫感或亂碼文字拉。若試生成出現此現象，建議改用同構圖的寫實照片版房間圖。

本輪只交付提示詞與配套；尚未生成 H3 影片。
