# SEG-02 生成說明 v05｜依 v0.7 文字劇情重製（手錶起頭）

- 最新提示詞：`seg02-a-minimax-h3-prompt-v04.txt`、`seg02-b-minimax-h3-prompt-v05.txt`。舊版保留。
- 劇情來源：`screenplay/master-storyboard-v0.7.md` 鏡頭 05–08；Storyboard v03 尚未製作／確認，依使用者直接指示先出 H3（同 SEG-01 v05 前例）。
- 切分維持 9＋12 秒正片，各生成 362 幀（15.083 秒），seed 7201。
  - A（00:24–00:33）＝鏡頭 05＋06：背靠門、1 秒手錶亮起震動、看錶皺眉、4 秒掏手機、亮屏。正片取前 9 秒，9–15 秒為推近螢幕的備用尾段。
  - B（00:33–00:45）＝鏡頭 07＋08：郵件通知卡 0–4 秒停留、4.6 秒點 App、5 秒切滿版群組；三則訊息 5／7／9 秒跳出；10.5 秒腳步聲引出 SEG-03。正片取前 12 秒。
- 上傳（依 Absent Objects 規則，不出場就不掛圖）：
  - A：`ref_image_0` = 女主角 `assets/characters/Gemini_Generated_Image_6rilce6rilce6ril.jpg`
  - B：`ref_image_0` = Teams UI `assets/software/teams-ui-reference-v01.png`（**待使用者放入**）。B 裡女主角只露手、袖口與錶緣，刻意不掛她的圖，避免 Ref2VA 把整個人召喚進特寫或 UI 畫面。
- 聲音：承接 SEG-01 B 嘆氣後的安靜；A 第 1 秒錶震是第一個清楚聲音，低鼓同步進入。72 BPM、D 小調，與 SEG-01 配樂同調性；只有低鼓／低 tom／次低音 drone，不接回管弦旋律。門後說話聲依 v0.7 保持靜音（提示詞不提）。
- 參考圖注意：registry `teams_ui.canonical` 寫的是深紫藍 header、白色訊息區、左側圓形頭像。若實際放入的 Teams 截圖配色／版面不同，先改 canonical 再重跑驗證，否則文字與圖互相拉扯。截圖上的範例訊息、人名、時間戳建議先塗白，減少被沿用的機率。
- 中文字驗收：H3 對繁中字形不保證正確；「RF需求變更需求」「半小時後開會」「Placement 討論」與三則抱怨若有錯字，後製以 UI 圖層覆蓋（B 第 2 鏡為平面 UI，易於疊圖）。
- 驗證：A 5155 字元 11 passed／0 warn／0 fail；B 11 passed／0 warn／0 fail。影片與音樂未生成。
