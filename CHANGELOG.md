# 修改紀錄

## 2026-09-23｜SEG-06 H3 A／B v04：純白房間、殘影開場、15 秒緩衝

- 新建 `screenplay/master-storyboard-v0.24.md`（v0.23 保留）與 `segments/SEG-06/brief-v04.md`，只改 SEG-06 與 05→06／06→07 連續性描述。
- drop 工作站改為純白房間（上傳圖），移除工作台，資料浮空；A 開場 Cadi 背後殘影轉場；hapa／hana 左緣進出。
- 新增 A／B prompt v04、cast-registry／reference-manifest／生成說明／validation v04、pure-white-room-binding-v01；根目錄 registry、manifest.csv、PROJECT_STATE、README 同步。
- A 6969 字元 16 通過／1 軟警告；B 6951 字元 14 通過；均 0 失敗。影片未生成。

## 2026-09-23｜SEG-05 劇情微調與 H3 A／B v06：Agent 從建築飛出、更動資訊標黃

- 依使用者指示新建 `screenplay/master-storyboard-v0.23.md`（v0.22 保留）與 `segments/SEG-05/brief-v04.md`，只改 SEG-05。
- hapa 改從左側掛 SPEC／HTTP 直式招牌的建築開口飛出；hana 改從右側掛 GP 辨識直式招牌的建築開口飛出。
- DLG-10 改為「hapa，透過 HTTP 取得最新 Spec；正確資訊標綠，更動資訊標黃。」
- 新增 A／B prompt v06、cast-registry／reference-manifest／生成說明／validation v06；A 6786、B 6975 字元，各 13 項通過、0 警告、0 失敗。時長、seed、上傳圖不變；v05 保留，影片未生成。

## 2026-09-23｜SEG-05 H3 A／B v05：紅焰 Cadi、聲音統一、15 秒緩衝

- Cadi 全段紅焰（cadi_red.png、根目錄 canonical）；聲音逐字統一為「in a bright, playful yet professional childlike Mandarin voice」。
- 工廠描述改 v02（無地名）；保留環境音效。A／B 各生成 15 秒／362 幀，正片取 A 0–14＋B 0–12＝26 秒，尾段為穩定停留緩衝。
- 女主角不出場，Cadi canonical 刪去以女主角為基準的身高句（Absent Objects）。使用者直接要求，略過過時 Storyboard v02。
- 新增 cast-registry／reference-manifest／生成說明／validation v05、場景綁定 v02；A 6595、B 6985 字元，各 13 項通過、0 警告、0 失敗；v04 保留，影片未生成。

## 2026-09-23｜SEG-04 A H3 v05：改用參考圖（Ref2VA）

- 上傳女主角（Picture 1）與 cadi_red.png（Picture 2），同 B 段；流程圖不在 A 出場，不上傳。
- 改為六區段格式；時間軸同 v04。新增 cast-registry／reference-manifest／生成說明／validation v10，根目錄 registry 與狀態同步。
- A 13 項通過、0 警告、0 失敗；v04 保留。

## 2026-09-23｜SEG-04 A H3 v04：依最新規則補齊區段

- 補 `subject_definitions`、`retention_analysis`（registry 逐字），畫風置於 [Shot 1] 開頭，新增 Negative constraints。
- 改為 15 秒／362 幀生成、5 個時間段；正片取 0–10 秒，10–15 秒為銜接 B 的穩定緩衝。
- 新增 cast-registry／reference-manifest／生成說明／validation v09；根目錄 registry 與狀態同步。A 8 項通過、2 項預期警告、0 失敗；v03 保留。

## 2026-09-23｜SEG-04 H3 A v03／B v08／C v03：紅焰銜接、Cadi 聲音統一、全白開場

- Cadi 維持紅焰（cadi_red.png、根目錄 canonical）；A 開場掃光由青色改為紅橙暖光。
- B、C 的 Cadi 聲音逐字統一為「in a bright, playful yet professional childlike Mandarin voice」；A 無台詞。
- A 新增 0–1 秒全白畫面、四周紅橙火焰狀光效；A 改 10 秒，原動作順延 1 秒。
- 工廠描述改用 v02（無地名）；新增 brief-v05、cast-registry／reference-manifest／生成說明／validation v08，根目錄 registry 與狀態同步。
- B、C 各 14 項通過、0 警告、0 失敗；影片未生成，舊版保留。

## 2026-09-23｜SEG-03 H3 A／B v03：紅焰 Cadi、新台詞與驚訝表情

- 新增 A／B prompt v03、`cast-registry-v03.yaml`、`reference-manifest-v03.json`、`minimax-h3-generation-notes-v03.md`、`validation-v03.json`；v02 保留。
- Cadi 參考圖改為 `cadi_red.png`，canonical 逐字取自根目錄 registry；聲音描述統一。
- 剪輯改為 A 0–11.0 秒＋B 0–10.0 秒＝21 秒；根目錄 registry 的 seg03-a／b 提示詞路徑與 beat 同步更新。
- A、B 各 13 項通過、0 警告、0 失敗；影片未生成。

## 2026-09-23｜SEG-03 劇情更新：紅焰 Cadi、任務台詞與驚訝表情

- 新建 `screenplay/master-storyboard-v0.22.md` 與 `segments/SEG-03/brief-v03.md`，v0.21／brief-v02 保留。
- Cadi 藍焰改紅焰，火光與光掃鏡改為紅橙暖光；SEG-04 開頭掃光同步改色。
- Cadi 聲音描述統一為「in a bright, playful yet professional childlike Mandarin voice」。
- DLG-06A 改為「接到一個棘手的任務，你看一下。」；Cadi 讀完郵件後新增驚訝表情；DLG-06B 刪去「主題是 placement 會議」。
- 維持 21 秒；H3 A／B v02 標為過時，本輪未製作新版 H3。

## 2026-09-23｜SEG-10 B H3 v04：位置銜接與 Cadi 入鏡

- A 維持 v03，只新增 B prompt v04 及配套版本。
- B 開場逐項描述指定圖中的女主角／風扇相對位置：女主角在大型風扇左側綠色空隙、介於兩風扇之間且更靠近大型風扇，右手搭在頂板左上區。
- Cadi 改為0–2秒從畫面上緣外飛入，停在女主角左肩後方後才說話；Ray 殘影進場、敬禮、接資料與離鏡順延至5–13秒。
- 新增 registry／manifest／場景綁定／生成說明／驗證紀錄 v04。B 16項通過、1項五圖軟警告、0失敗；待重生影片驗證。

## 2026-09-23｜SEG-10 H3 v03：取消走入與 bottom view 機位

- A 的0–3秒改為女主角開場已站在風扇旁並直接蹲下，取消走入與接近動作。
- A、B 實際上傳 `assets/placement/bottom view 3_1.png` 作 placement-creo 攝影角度與構圖參考；原指定圖繼續負責風扇形狀與人物比例。
- 新增 A／B prompt v03、registry／manifest／場景綁定／生成說明／驗證紀錄 v03；維持13＋13秒、seed 8001、Creo船塢、對白及Ray動作。
- A 14項通過、0警告、0失敗；B 16項通過、1項五張參考圖軟警告、0失敗。影片未生成，v02保留。

## 2026-09-23｜SEG-10 H3 A／B v02：Creo 船塢與指定風扇

- 依使用者直接要求生成新版 H3，授權略過新版 Storyboard 尚未確認；舊版 A／B／C v01 保留。
- 新版改為 A／B 各13秒，合計26秒並沿用 seed 8001；場景固定為 SEG-09 後的同一座 Creo 船塢。
- `assets/placement/Screenshot 2026-09-22 165319.png` 在兩段均實際上傳，用於大型右上風扇的形狀、比例、頂部同心圓、中央圓蓋、外殼厚度與局部 placement 位置。
- 新增 A／B prompt v02、cast registry v02、reference manifest v02、場景綁定 v02、生成說明 v02 與驗證紀錄 v02。A 13項、B 15項通過，均0警告、0失敗；影片未生成。

## 2026-09-23｜SEG-10 風扇近看與 Ray 殘影派工

- 新建 `screenplay/master-storyboard-v0.21.md` 與 `segments/SEG-10/brief-v03.md`，保留舊版。
- 女主角依指定 placement-creo 比例圖走到風扇旁，蹲下端詳並觸摸風扇頂部；對白改為「這個風扇的強度不足」。
- Cadi 對白改為「我來啟動風扇Rib AI 最佳化服務」。Ray 改為殘影衝入、向 Cadi 敬禮、接過資料，再以殘影衝刺離鏡。
- 取消舊版 ABS／壓強10／Gap1.5／執行同意／模型資料箱內容；SEG-11 劇情不變，只更新資料交接連續性。
- SEG-10 Storyboard v01 與 H3 A／B／C v01 標記過時；本輪未製作新版 Storyboard 或 H3。同步更新 README、PROGRESS、PROJECT_STATE、DECISIONS 與資產索引。

## 2026-09-22｜SEG-09 B 北側外緣離場路徑

- 新增 SEG-09B H3 v06；其餘時間、素材、同步拉遠與地面 Placement 設定不變。
- Robot 第二鏡起點改為 Placement 北側外緣之外的裸露船塢地面，雙腳與綠色基底保持可見間距。
- Robot 背對 Placement 向外走入北側通道，完整路徑位於基底邊界之外。新增 brief v08、registry／manifest／生成說明與驗證紀錄 v06；A 相容性14項、B 13項通過，均0警告、0失敗；舊檔保留，影片未生成。

## 2026-09-22｜SEG-09 B 北側同步離場與地面 Placement

- 新增 SEG-09B H3 v05；A 維持 v02，時長、seed 與上傳素材不變。
- Creo Robot 朝 placement-creo 北側深處離開；Picture 2 畫面上方／遠端明確定義為北側。
- Robot 起步與攝影機後拉升高同步發生，離場與 Placement 揭露成為同一段連續運動。
- placement-creo 直接平放在船塢地面，綠色基底具有連續地面接觸與真實接觸陰影。新增 brief v07、registry／manifest／生成說明與驗證紀錄 v05；A 相容性14項、B 13項通過，均0警告、0失敗；舊檔保留，影片未生成。

## 2026-09-22｜SEG-09 B 上半身放置與 Creo Robot 離場

- SEG-09A 維持 v02；新增 B prompt v04，場景、13 秒時長、seed 與 placement-creo 參考圖不變。
- 放置鏡頭改為只取 Creo Robot 腰部以上；雙手伸到畫面下緣之外，以重擊聲、低頻共振和肩臂回震表達放下動作。
- Robot 放置後直起身、轉身，沿側通道走出鏡頭；工作區淨空後再拉遠升高展示完整 Placement。
- 新增 brief v06、registry／manifest／生成說明與驗證紀錄 v04；A 相容性14項、B 13項通過，均0警告、0失敗；舊檔保留，影片未生成。

## 2026-09-22｜SEG-09 B 重物落位特寫與 Placement 拉遠展示

- SEG-09A 維持 v02；只新增 B prompt v03，場景仍是 Creo 船塢，時長 13 秒、seed 7901 不變。
- 第一鏡特寫 Creo Robot 將沉重的右側冷卻風扇零件放入定位；接觸瞬間加入沉重金屬落地聲、低頻衝擊與短暫結構共振。
- 第二鏡不切鏡，攝影機後拉、升高並向下俯視，以 `assets/placement/Screenshot 2026-09-21 164040.png` 為完整 Placement 與最終構圖基準。
- B 只上傳 Creo Robot 與 placement-creo 兩圖，不再使用 Cadi、純白房間或舊版動作影片。新增 brief v05、registry／manifest／生成說明與驗證紀錄 v03；A 相容性 14項、B 13項通過，均0警告、0失敗；舊檔保留，影片未生成。

## 2026-09-22｜SEG-09 純白房間轉 Creo 船塢與影片弱參考

- Cadi 彈指鏡頭改在 `assets/environments/純白房間.png`；攝影機快速向右轉，Creo Robot 第一次清晰入鏡時已進入 Creo 船塢。
- H3 A／B v02 由 `assets/blender/seg09-creo-dock-v06/seg09-creo-dock-animation-v06.mp4` 分切兩支 13 秒上傳檔，分別只參考前半與後半的動作、時序、承重反應、搬運路線與運鏡。
- 移除 v01 三張 Blender 場景構圖圖的新版上傳，船塢改由正向文字建立；原 `.blend`、MP4 與 H3 v01 全部保留。
- 新增 brief v04、`master-storyboard-v0.20.md`、A／B prompt v02、registry、manifest、場景綁定、生成說明與驗證紀錄。A 14項、B 13項通過，均0警告、0失敗；影片未生成。

## 2026-09-22｜SEG-07／08 更新純白房間

- 場景參考更新為 `assets/environments/純白房間.png`，納入四個 H3 生成單元的實際上傳索引。
- Placement 維持在房間中央、腰胸高度水平懸浮；純白房間保留對稱牆板、反光地面、圓角天花凹槽、暖白燈線與兩側細黑通風縫。
- SEG-07 新增 A v07／B v10、registry／manifest／生成說明 v10；SEG-08 新增 A v07／B v05、registry／manifest／生成說明 v07。舊版保留。
- 劇情、角色動作、台詞、seed、時長與動作影片用途不變。SEG-07 B 最終布局圖仍待提供，影片未生成。

## 2026-09-22｜SEG-07／08 更新日式室內與中央懸浮 Placement

- 場景參考由 `assets/environments/室內.jpg` 更新為 `assets/environments/日式.jpg`，納入四個 H3 生成單元的實際上傳索引。
- Placement 改為在房間中央、腰胸高度水平懸浮，底下保留空間；後方盆栽維持可見。移除現行提示詞中的工作桌依附設定。
- SEG-07 新增 A v06／B v09、registry／manifest／生成說明 v09；SEG-08 新增 A v06／B v04、registry／manifest／生成說明 v06。舊版保留。
- 劇情、角色動作、台詞、seed、時長與動作影片用途不變。SEG-07 B 最終布局圖仍待提供，影片未生成。

## 2026-09-22｜SEG-07／08 drop 工站改為室內圖片場景

- 依使用者指示，以 `assets/environments/室內.jpg` 取代 SEG-07／08 舊版虛擬工廠街區文字場景，並把該圖納入每個 H3 生成單元的實際上傳索引。
- SEG-07 新增 A v05／B v08、`cast-registry-v08.yaml`、`reference-manifest-v08.json`、室內場景綁定與生成說明 v08。A 室內圖為 Picture 3；B 因 Picture 3 保留給最終布局，室內圖為 Picture 4。
- SEG-08 新增 A v05／B v03、`cast-registry-v05.yaml`、`reference-manifest-v05.json`、室內場景綁定與生成說明 v05。A 室內圖為 Picture 4；B 室內圖為 Picture 3。
- 劇情、動作、台詞、seed、時長、Placement 與動作影片用途均不變；舊檔保留。SEG-07 B 最終布局圖仍待提供，影片未生成。

## 2026-09-21｜SEG-08 A 動作修訂與 H3 v04

- Placement 全程留在工作桌面，Cadi 懸停於右側、雙手自然垂放，不托拿布局。
- A 前半女主角認真查看 Placement；後半只以食指指向 CPU，手做小幅度控制移動並說 DLG-20；12–13秒放下手、挺直上半身，恢復直立站姿。
- B v02、CPU 側移、確認採用與啟動 Creo 等後續劇情不變。新增 `brief-v04.md`、`master-storyboard-v0.19.md`、A prompt／registry／manifest／生成說明 v04；舊版保留，影片未生成。

## 2026-09-21｜SEG-08 A H3 v03：布局改用圖片參考

- A 段移除完成布局的 `<Video 1>`，改以上傳 `assets/placement/placement_2D.png` 為 `<Picture 3>`；圖片只負責完整布局的零件身分、比例、間距、位置、輪廓、配色分組與矩形平面方向。
- A 的女主角站姿、13秒、12–13秒持續對 placement 比劃、DLG-20 與其他劇情均不變；B 維持 v02。
- 新增 A prompt v03、cast registry v03、reference manifest v03 與生成說明 v03；舊版保留，影片未生成。

## 2026-09-21｜SEG-08 站姿修訂與 H3 A／B v02

- A 段承接 SEG-07 B v07 末端站姿：女主角站著端詳 Placement，9–12秒咕噥並比劃，12–13秒持續對 Placement 比劃；A 由12秒改為13秒。
- B 段女主角改為站姿；CPU 金黃亮顯側移停住、女主角確認採用與 Cadi 啟動 Creo 等後續劇情及10秒時長維持不變。
- 新建 `brief-v03.md`、`master-storyboard-v0.18.md`、A／B H3 prompt v02、cast registry v02、reference manifest v02、場景綁定 v02 與生成說明 v02；工廠文字採 v02。舊版保留，影片未生成。
- H3 配置合計23秒，較原02:46–03:08剪輯時槽多1秒，標記待剪輯校時。

## 2026-09-21｜SEG-07 B H3 v07：結尾端詳動作

- B 段 11–12 秒改為 Cadi 完成展示後保持位置，女主角稍微彎腰端詳 Placement；鏡頭共同聚焦 Placement 與女主角認真的表情。其餘圖片、場景、台詞、片長與缺席物件設定沿用 v06。

## 2026-09-21｜SEG-07 B H3 v06：最終布局改用圖片

- B 段移除 `<Video 1>` 與影片上傳，改以待提供的 `<Picture 3>` 鎖定最終布局的零件、比例、間距、位置與平面方向。Picture 1／2 維持女主角與 Cadi；drop 不出場。新增 prompt、registry、manifest 與生成說明 v06，圖片路徑待補。

- 2026-09-21：依使用者修正，SEG-07 B 升為 H3 v05，只保留站姿女主角與 Cadi；移除 drop 的所有文字、動作、Picture／Subject 索引及上傳圖片。A v04、B 12秒、seed 7701、場景 v02、台詞及完成布局影片參考保留；新增 registry／manifest／生成說明 v05，影片未生成。

## 2026-09-21｜SEG-07 H3 v04：最新場景與 B 段站姿

- 新增 SEG-07 A／B H3 v04，套用 `virtual-factory-description-v02.txt`；B 段女主角改為站在工作區近左側觀看布局，移除躺椅與坐姿。時長、seed、指定台詞、圖片上傳順序與動作影片用途不變。
- 新增 `cast-registry-v04.yaml`、`reference-manifest-v04.json`、`factory-scene-binding-v02.md` 與生成說明 v04；更新根 registry、PROJECT_STATE、PROGRESS 與本段 revisions。A 13項、B 14項通過，均0警告、0失敗；舊版保留，影片未生成。

## 2026-09-21｜虛擬工廠共用描述 v02

- 新建 `assets/environments/virtual-factory-description-v02.txt` 與 `virtual-factory-usage-v02.md`，移除台灣／香港及其英文地名字樣，改以 `dense high-rise urban streetscapes` 保留高密度垂直街區意象。
- README、根 `cast_registry.yaml` 與 `PROJECT_STATE.json` 的正式入口已切換至 v02；v01、既有 H3 提示詞及各段 registry／manifest 快照保留不回改。

## 2026-09-21｜SEG-07 正式併入 master storyboard v0.17

- 新建 `screenplay/master-storyboard-v0.17.md`，保留 v0.16。將已確認的 `segments/SEG-07/brief-v02.md` 正式寫入鏡頭24–27：drop 查看 Spec／GP 資料、展開立體影像、全部零件灑落並排成水平發光布局，Cadi 邀請躺椅上的女主角評估。
- 停用 DLG-18 且不重用編號；DLG-19 保留「這是最新版的placement，您覺得如何」。同步更新段落表、EV-12、對白統計與 06→07 連續性。README 與 PROJECT_STATE 的唯一劇情來源切換至 v0.17；既有 Storyboard、H3、brief 與舊版主檔不回改。

## 2026-09-21｜人物設定正式併入 master storyboard v0.16

- 新建 `screenplay/master-storyboard-v0.16.md`，保留 v0.15。鎖定設定更新為紅焰 Cadi，並納入 hapa、hana、drop、Ray、Finn 的身分與資產基準。
- SEG-05 正式採用已授權版本：hapa 回答後向左飛離、hana 回答後向右飛離；女主角不出場；末鏡攝影機環繞 Cadi 約180度，Cadi 準備前往下一站。
- 為維持必要連續性，SEG-06 正式承接 Cadi 單獨抵達 drop 站、hapa／hana 親自交付資料後飛離，以及 drop 開始彙整。同步更新時長表、事件覆蓋、跨段連續性與技術模組名稱。
- README 與 PROJECT_STATE 的唯一劇情來源切換至 v0.16；既有 Storyboard、H3 與版本快照不回改。

## 2026-09-21｜SEG-08 H3 A／B v01

- 依使用者直接要求，略過尚未製作的新版 Storyboard，新增 SEG-08 Ref2VA A／B v01（12＋10秒，共22秒，seed 7801）。A 為 Cadi 托起整片發光布局平面平移到漂浮躺椅前並微傾展示、女主角坐起前傾端詳、食指空中筆畫並咕噥 DLG-20；B 為金黃零件水平側移一小段後停住維持亮顯、其餘零件不動，接女主角 DLG-21 與 Cadi DLG-22。兩段 cast 只有女主角與 Cadi（ref_image_0／ref_image_1），drop 不入鏡且提示詞一字不提；工廠維持純文字場景。B 的 `<Video 1>` 明寫只用 02-cpu-move-highlight-v07 的移動與停住段，零件停在新位置。新增 `cast-registry-v01.yaml`、`reference-manifest-v01.json` 與生成說明 v01；A／B 各13項通過，0警告、0失敗。影片未生成。

## 2026-09-21｜SEG-08 女主角微調 CPU 並確認 placement

- 依使用者指示改寫 SEG-08：Cadi 把 drop 在 SEG-07 排好的布局（一整片發光平面）帶到女主角面前，女主角坐起端詳、以食指朝布局筆畫並咕噥「或許 cpu 往旁邊移動一點……」；CPU 金黃亮顯水平側移後停在新位置，女主角思考後說「好，使用這一版 placement。」Cadi 回「好的，我來啟動 Creo。」取消原上移 3 mm、限制條件與重算、新舊結果比較；新增鏡頭29A，DLG-20–22 改寫、DLG-23 停用不重用。正式主檔升至 v0.15（v0.14 保留），新增 `segments/SEG-08/brief-v02.md`；動作參考 `assets/blender/cpu-motion-v07/02-cpu-move-highlight-v07.mp4`，只採用移動與停住段（約0.6–1.6秒），回位段不使用。drop 不入鏡。SEG-09 僅同步鏡頭31 承接句與 08→09 聲音橋，動作與26秒不變。Storyboard v01 已過時，22 秒待校時，H3 未製作。

## 2026-09-20｜SEG-11 煉丹爐運算與 H3 A／B／C v03

- 正式主檔升至v0.14；原H3 B順延為C，新增13秒B展示煉丹爐式AI運算核心、Ray驚訝、火光、燃燒鍋爐、爆鳴硬切及Finn交付丹藥般結果。新增brief-v03、A／B／C v03、registry、manifest、生成說明及驗證紀錄。A/B各13項、C14項通過，0警告、0失敗；總長39秒，原26秒時槽待校正，影片未生成。

## 2026-09-20｜SEG-13 H3 A／B v01

- 依使用者直接授權略過已過時 Storyboard v01，新增 SEG-13 Ref2VA A／B v01。A 15秒，只掛女主角圖，完成凌亂會議室、2:30時鐘、HP筆電指定台詞、Placement 3D投影、長官反應、解說點頭及太陽轉白；B 5秒，只掛紅焰Cadi圖，完成右下飛入、單次眨眼與向上飛離。新增cast registry、reference manifest、生成說明與驗證紀錄；A／B各12項通過，0警告、0失敗。總長20秒，較原15秒時槽多5秒，影片未生成。

## 2026-09-20｜SEG-13 HP Placement Review 與片尾更新

- 依使用者指示僅更新 SEG-13：女主角抱著銀色 HP 筆電回到凌亂的多人會議室，牆上時鐘顯示 2:30；清出桌面、攤平筆電並向 HP 長官宣布開始 placement review。筆電投射完整 Placement 3D 影像，眾人驚訝；以輕快音樂呈現女主角自信解說與長官點頭，鏡頭再拉出窗外見太陽並轉白，Cadi 從右下角飛入眨眼後向上飛離。新增 `master-storyboard-v0.13.md` 與 `brief-v02.md`，v0.12及Storyboard v01保留；新版 Storyboard 與 H3 待製作，15秒待校時。

## 2026-09-20｜SEG-12 H3 A／B v01

- 依使用者直接授權，略過已過時 Storyboard v01，新增 SEG-12 Ref2VA A／B v01（12＋7秒，共19秒）。A使用女主角、紅焰Cadi兩圖，完成滿意致謝、Cadi回應與整理衣服；B只使用女主角一圖，完成完整Placement布局拉遠成辦公室電腦畫面、後方機位起身與螢幕關閉。新增registry、reference manifest、生成說明與驗證紀錄；A 13項、B 12項通過，均0警告、0失敗。影片未生成。

## 2026-09-20｜SEG-12 驗收致謝與辦公室轉場

- 依使用者指示更新 SEG-12：承接 SEG-11 同一風扇場景，新增女主角滿意致謝、Cadi 回應與女主角整理衣服；鏡頭拉遠完整 Placement 布局後，轉場至辦公室電腦畫面，女主角從後方機位起身並關閉螢幕。正式主檔升至 v0.12，新增 brief-v02；SEG-13 僅同步必要的黑畫面銜接，其他內容不變。Storyboard v01 已過時，19秒待校時，H3 尚未製作。

## 2026-09-20｜SEG-11 H3 A／B v02

- A更新兩句指定台詞，並將掃描內容改為殼體厚度、Gap距離、材質三層；B重構為Ray回到SEG-10同一風扇場景，風扇殼體內側長出單根矩形結構Rib，Cadi回報完成，女主角開心點頭。A掛Ray＋Finn，B掛女主角＋Cadi＋Ray；新增registry、manifest、生成說明及驗證紀錄。A 13項、B 14項通過，0警告、0失敗；v01保留，影片未生成。

## 2026-09-20｜SEG-11 H3 A／B v01

- 依使用者直接授權，新增 SEG-11 Ref2VA A／B v01（13＋13秒，共26秒）。A使用Ray、Finn兩圖；B使用Cadi、Ray、Finn三圖。新增分段registry、reference manifest、生成說明及驗證紀錄；完整保留三句對白，A 13項、B 14項通過，均為0警告、0失敗。Storyboard v01角色仍過時，影片未生成。

## 2026-09-20｜SEG-11 研究員改為 Finn

- 依使用者指示，將 SEG-11 原穿白袍的研究型機器人／研究員改為 Finn，身分參考 `assets/characters/agent4-finn.png`。Finn 接收 Ray 送達的資料、確認限制、執行 Rib 運算並交還結果；台詞、事件、時間與前後段連續性不變。正式主檔升至 v0.11，新增 brief-v02；Storyboard v01 已過時，H3 尚未製作。

## 2026-09-20｜SEG-10 H3 A／B／C v01

- 2026-09-20：使用者確認SEG-10修訂並直接要求H3，新增A／B／C v01（13＋15＋10秒，共38秒）。完整保留五句對白；A/B女主角與紅焰Cadi兩圖，C新增Ray為Picture 3。新增分段registry、manifest、生成說明與驗證紀錄；A/B各13、C14項通過，0警告、0失敗，對白逐字及時間連續性另驗通過。Storyboard v01仍過時，直接H3授權已記錄；影片未生成。原26秒時槽及全片時間待校正。

## 2026-09-20｜SEG-10 強度檢查與 Ray 派工

- 2026-09-20：依使用者指示更新 SEG-10：共同檢查已落位風扇、指出無法承受10的壓強、提議 Rib 結構 AI 最佳化、確認 ABS／壓強10／Gap 1.5、女主角同意後派 Ray 抱模型資料箱入研究所。完整保留五句對白，新增 DLG-27A／27B。正式主檔升至 v0.10，新增 brief-v02，舊檔保留；SEG-11 僅同步小花→Ray 的角色連續性。Ray 參考 assets/characters/agent5-ray.png。SEG-10 原26秒待試讀校時，單位未指定；SEG-10／11 Storyboard v01 已過時，H3未製作。

## 2026-09-20｜SEG-09 H3 A/B v01

- 2026-09-20：依使用者確認SEG09 Blender v06並直接要求H3，新增A/B v01各13秒，五圖順序為Cadi、Creo、接風扇、全布局搬運、Cadi在已放風扇旁；已備妥圖3/5截圖及圖4拉遠重渲染、registry／manifest／生成說明。五組17–18秒完成落位，搬運時空位、落位後單一零件固定。A/B各13通過、2已解釋提示、0失敗；未生成H3影片。

## 2026-09-20｜SEG-09 v06 多台Creo協同落位

- 2026-09-20：SEG-09 Blender v06讓其餘四台Creo各自移動至正確placement位置，左記憶體／CPU／SSD／左上散熱件分別於408／414／426／432幀放妥，與主風扇420幀約同時完成；全部放手、退開後Cadi才抵達。沿用同一可見零件完成搬運至落位，624幀無重複檢查及最終頂點位置比對通過。26秒，另存工程與影片，v05保留。

## 2026-09-20｜SEG-09 v05 加速搬運及風扇落位

- 2026-09-20：SEG-09 Blender v05加快Hero風扇搬運與其他Robot 1.6倍速步態／位移；同一風扇於420幀（17.5秒）放妥、446幀放手並退開，Cadi抵達前已在placement原座標就位。原平面風扇複本持續隱藏，其他四組尚在搬運的零件繼續留空。保留26秒與舊版本。

## 2026-09-20｜SEG-09 v04 搬運零件去重

- 2026-09-20：SEG-09 Blender v04修正搬運零件重複出現在placement平面的問題。右風扇、左記憶體、CPU、SSD、左上散熱件五組在搬運期間保留平面空位；隱藏93個對應物件，624幀可見性檢查通過。維持26秒既有動作與運鏡，另存新版工程與MP4，v03保留。

## 2026-09-20｜SEG-09 v03 Blender 動畫預演

- 2026-09-20：SEG-09依使用者指定v02船塢、Creo概念圖與cpu-motion-v07實際零件布局，新增v03 Blender 26秒動畫預演（24fps／624幀）：Cadi彈指、Creo下夾胸、墜落接風扇與負重行走、多機器人搬運、升空俯瞰及下降至風扇附近。新增可編輯工程、MP4、鏡頭表與檢視圖；動作預演待使用者評估，舊版及正式劇本／Storyboard／H3保留。

## 2026-09-19｜SEG-09 v02 Blender 靜態定裝

- 新增 `assets/blender/seg09-creo-dock-v02/`：場景 `SEG09_Creo_Dock_v02`、`build-v02.py`、5 張關鍵機位定裝圖、接觸表與 `shot-manifest-v02.json`。
- 內容：Creo Robot 下夾胸亮相、巨型筆電風扇墜落與接住、CAD 船塢縱深、多台 Robot 搬運巨型零件、70x40m placement 布局板、Cadi 火焰代理飛行動線。
- `seg09-creo-dock-v01` 原樣保留；劇本、Storyboard、cast_registry 與其他 SEG 未變更。

- 2026-09-19：依使用者要求完成SEG-09方案二Blender白模預演v01（重型軌道船塢、Creo Robot操作台、煞停慣性、展開匯入），新增可編輯blend、12秒預演與檢視圖於assets/blender/seg09-creo-dock-v01。概念待評估；正式劇本、Storyboard與H3狀態不變。

- 2026-09-19：SEG-06依使用者要求重製H3 A／B v03（15＋9秒），DLG-14改為「最新 Spec 已取得。固有項目標綠，新增參數已標黃。」同步卡片顏色語意並移除兩項數量限制；重新讀取目前工廠文字，場景內容與v02相同。新增brief、registry、manifest與生成說明v03；舊版保留，影片未生成。

- 2026-09-19：依使用者要求將已確認英文工廠描述納為 SEG-04～12 共用文字場景。新增場景原文、套用規則與各段綁定；SEG04 A v02／B v07／C v02、SEG05 A/B v04、SEG06 A/B v02、SEG07 A/B v03已加入場景，並依既有規則使用紅焰Cadi。SEG04取消工廠參考圖，流程圖改Picture 3；各段新增registry／manifest／生成說明。SEG08～12待H3製作時套用，室內鏡頭只描述可見內容；原劇情、台詞、時間節點及舊檔保留。影片未生成。

- 2026-09-17：依使用者要求將SEG07 A／B H3升至v02，採commit 724a701的Cadi紅焰／深灰紅點綴規格與cadi_red.png。同步建立registry、reference manifest、生成說明v02，更新現行索引；v01保留。兩段檢查13／14項通過、0警告、0失敗。維持14＋12秒、指定台詞、角色動作、場景青藍補光及投影配色；影片未生成。

- 2026-09-17：依使用者要求，Cadi 新製作色系改為紅焰版；實際資產為 `assets/characters/cadi_red.png`（原訊息的 `cadi/_red.png` 不存在）。更新 AGENTS、H3 skill、共用 registry、registry 模板及資產索引；外觀依新版圖，持續燃燒／非固體動態保留。既有 H3 提示詞、各段 registry／manifest 與生成說明全部保留；劇情及分段進度不變。

- 2026-09-17：使用者確認SEG07文字修訂並直接要求H3，新增A／B v01（14＋12秒）、本段registry及圖片／影片manifest。A用Cadi、drop兩圖及零件影片，B用女主角、Cadi、drop三圖及同影片的完成布局；指定台詞完整保留，seed7701。檢查A13／B14項通過，0警告、0失敗。新版Storyboard未製作，影片未生成。

- 2026-09-17：依使用者指示新增 SEG-07 brief-v02，承接 SEG-06 drop 看資料，展開立體影像，全部零件灑落平面並排好；參考 cpu-motion-v07 的 01-scatter-rise-v07.mp4／.blend。Cadi 邀請女主角觀看，DLG-19 改為「這是最新版的placement，您覺得如何」，原 DLG-18 停用。結尾帶出躺椅上的女主角銜接 SEG-08；暫沿用26秒。主檔與舊版保留，Storyboard v01 已過時，H3 待新版圖確認。

- 2026-09-17：使用者明確要求直接修改 master-storyboard-v0.8.md，已將全文9處「小白」統一改為「drop」，涵蓋分段表、鏡頭23／24、DLG-16–18、事件表與連續性帳本；本次僅替換名稱，保留v0.8檔名與其餘內容。

- 2026-09-17：使用者看過 SEG-06 Storyboard v02 後直接要求生成 H3；新增 A／B v01，規劃15＋9秒。A使用Cadi、drop、hapa、hana四圖，B僅Cadi與drop兩圖；完整保留DLG-14–17及揮手招呼、直接交付後飛離的順序。逐字沿用真人電影畫風與既有角色canonical；新增drop身分、本段registry、manifest及生成說明。驗證A14／B12項通過，各1個小數beat誤報警告、0失敗；另核對六beat連續及對白逐字一致。影片尚未生成。

- 2026-09-17：依使用者要求，使用內建 imagegen 完成 SEG-06 Storyboard v02 六格黑白圖，依 brief-v02 呈現 Cadi 抵達並問候 drop、hapa／hana 親自交付 Spec／GP、兩者飛離、drop 接手彙整。已檢視角色與交接順序並校正殘留色彩；v01 及初稿保留。新版待使用者確認，H3 尚未製作。

- 2026-09-17：依使用者指示新增 SEG-06 brief-v02：小白改為 drop（agent3-drop.png）；承接 SEG-05，Cadi 直接飛抵 drop 站點並打招呼，hana／hapa 返回，親手交付各自資料後飛離。保留既有任務分工、回報及交叉驗證台詞，DLG-16 更新稱呼；原24秒時槽待試讀。SEG-07 鏡頭24 的小白身分同步延續為 drop，事件與台詞不變。v0.8 與舊版保留；Storyboard v01 已過時，H3 待新版圖確認後製作。

- 2026-09-17：依使用者要求新增SEG-05 brief v03與H3 A／B v03。hapa接令後左飛，hana接令後右飛；末4秒環繞Cadi約180度，準備前往下一站。全段移除女主角及相關道具引用，各段只掛Cadi與當段Agent；保留完整台詞與14＋12秒。新增本段registry去除Cadi身高比較中的女主角引用，其他段落不改。Storyboard v02已過時，待新版；影片未生成。

- 2026-09-17：使用內建 imagegen 完成 SEG-05 Storyboard v02 四格，hapa／hana 依提供的身分圖替換，保留鏡頭16–19構圖及任務。v01 保留；新版待使用者確認。

- 2026-09-17：依使用者指示，SEG-05 小明改為 hapa（agent2-hapa.png）、小華改為 hana（agent1-hana.png）。新增 brief v02、H3 A／B v02 及生成說明 v02；移除舊角色外形，更新稱呼與身分圖、registry、manifest 及狀態。原時長、任務與其餘台詞保留。Storyboard v01 角色待更新；SEG-06 後續製作須延續同一身分對應。v0.8 與舊版檔案保留。

- 2026-09-16：使用者直接要求生成 SEG-05 H3，依 v0.8 鏡頭16–19製作 A v01（14秒）與 B v01（12秒），完整保留 DLG-10–13。兩段只掛女主角與 Cadi 身分圖；小明、小華依現有分鏡外形作文字描述，工廠街區採文字建構。Storyboard v01仍待審查，影片未生成；其他SEG未改。

- 2026-09-16：依使用者拆分SEG04-B/C，B v06保留0–7秒並加1秒停留；C v01首秒銜接，台詞改為「接著我會開啟Creo導入3D模型，接者做風扇Rib的運算」。C安排15秒，說完後流程上移露出approve鍵，女主才伸手按；原台詞的「接者」照錄。聲音沿用配樂＋人聲。全片時間待校正，其他段未修改。

- 2026-09-16：SEG04-B H3 v05 依使用者三項修正：台詞拆入各時間節點、流程圖顯示於虛擬螢幕、核准改為圓形且標示小寫 approve 的按鈕。按下後亮起並分送兩道資料光軌。維持15秒、一鏡到底、同步喝飲料、輕快配樂與對白、無效果音；新台詞逐字保留。新增 brief v03，舊版保留。

- 2026-09-16：SEG04-B H3 v04 依使用者指示改為輕快、有活力的器樂配樂，保留兩句完整對白；取消所有環境聲與動作效果音。維持15秒、同步喝飲料與四圖設定，v03保留；影片未生成。

- 2026-09-16：SEG04-B 升至 H3 v03，保留新台詞原文，15秒內同步喝飲料，最後核准。新增四圖上傳清單及空白路徑檔、brief v02 和生成說明 v03；更新 registry、manifest、進度與狀態。工廠／流程圖片尚未提供，影片未生成。

- 2026-09-16：依使用者要求僅製作 SEG-04 B H3 v02，採兩張角色身分圖、逐字 visual_style／canonical 與六區段格式，15 秒單鏡頭；完整保留 DLG-08／09 與流程圖順序。新增獨立提示詞、生成說明、registry／manifest 條目並同步狀態；舊 v01 及 A 保留，影片未生成。

- 2026-09-15：使用者直接要求生成 SEG-03 A／B H3。依 v0.8 製作 seg03-a v02（鏡頭09–10，取9.5秒）與 seg03-b v02（鏡頭11，取11.5秒），seed 7301，cast heroine＋cadi；新增 registry 分段 seg03-a／seg03-b 與生成說明 v02。兩段驗證 13 passed／0 warn／0 fail；Storyboard 未更新、影片未生成，S03a／S03b v01 保留。

- 2026-09-15（時長確認）：使用者決定 SEG-03 維持原定21秒（00:45–01:06），沿用 v0.8。完整保留對白、動作與0.5秒思考停頓；此決定取代先前35–40秒估計及待重排註記。全片維持5:00，後續段落時間碼不變；此為製作時長決定，非配音實測結果。

- 2026-09-15（後續微調）：使用者明確指定維持 v0.8，直接更新原檔 SEG-03。鏡頭09採使用者原文：攝影機進入辦公區，女主角將辦公椅稍微挪開並且坐下，喚醒螢幕，身體微微前傾；刪去倒退跟拍與筆電接工作站動作。鏡頭10思考停頓由1秒改為0.5秒。五句對白及鏡頭11轉場保留，其他段落不變；本紀錄取代先前1秒設定，時長仍待試讀。

- 2026-09-15：依使用者指示僅修訂 SEG-03，來源升至 v0.8，保留 v0.7。Lisa 喚醒螢幕並呼叫 Cadi；Cadi 在螢幕中問候，Lisa 不耐煩地請他查看棘手信件；Cadi 頭上冒出 Outlook icon，思考停頓1秒後提醒半小時後的 placement 會議，提出搜尋最新 IEC spec、結合 GP 圖建立 placement 預覽，Lisa 回答「讓我們開始吧」。校正「半小時候」為「半小時後」。新增 DLG-06A／06B，其他段落對白編號不變；預估35–40秒，未試讀，原時槽及後段時間碼待校時。SEG-03 Storyboard v01 與 H3 v01 標為過時，新增 brief-v02，未製作新圖或提示詞。


## 2026-09-15

- 依使用者要求移除專案內 Blender 模型、動畫影片／影格、製作腳本及連線暫存，新增 Git 忽略規則，與 SEG-02B v08 更新一併提交。

- SEG-02B 提示詞升至 v08：使用者指定手機桌面參考（Picture 2，待提供）、三位同事 profile 頭像及慌張／沮喪／憤怒的國語念詞。維持原訊息與 12 秒正片，以部分重疊配音安排時長，配樂在人聲下降。A v06 保留，更新 registry、manifest、狀態與生成說明 v08；Storyboard v03 依「很棒」及後續修改指示記錄已確認構圖。

- 依使用者要求使用內建 imagegen 生成 SEG-02 Storyboard v03 四格，對應 v0.7 鏡頭 05–08。修正初稿左右手、郵件圖示與灰階；舊版及初稿保留。已完成待確認；第一則群組訊息標點仍以文字來源為準。同步更新進度與狀態。

- 依使用者要求確認 H3 skills 與須知，重製 SEG-02 A v06／B v07；逐字使用真人 visual_style、移除畫風召喚詞，保留原文與 9＋12 秒。修正 A 抬手機鏡位及 B 已解鎖通知卡的接續；兩段均 12 passed／0 warnings／0 failed。新增生成說明 v07，更新 SEG-02 索引與 Teams 圖片標籤；Teams 素材尚缺，影片未生成，Storyboard 確認狀態不變。

- 依使用者指示，以 v0.7 文字劇情重製 SEG-02 H3：seg02-a v04（手錶震動、掏手機亮屏，只掛女主角）、seg02-b v05（RF 郵件通知、點開 Teams、滿版群組三則抱怨，只掛 Teams UI 參考圖）。9＋12 秒、seed 7201、低鼓漸強不變；Storyboard v03 未製作。更新 registry cast／路徑、manifest 上傳順序與生成說明 v05；兩段驗證 0 fail。

- 使用者實測發現：MiniMax H3 的文字條件沒有否定運算子，只要不該出場的物件出現在 `<Subject>` / `<Picture>` 標籤或提示詞裡（含 no / excluded / absent 等否定句），模型就會把它畫進畫面；Ref2VA 連上傳參考圖本身都是召喚。
- `.agents/skills/h3-scene-prompt/SKILL.md` 新增「Absent Objects」硬規則：不出場者不上傳圖、不編索引、全文不提名；負面表列只准放畫面瑕疵與鏡頭屬性；跨段一致性改由固定 seed ＋ 出場段落逐字重用 canonical 維持。
- `check_prompt.py` 新增 `check_summoning`：抓排除／保留宣告句型、與參考標籤同句的否定、以及不在 cast 卻被提名的 registry 資產（FAIL），並對負面表列裡的物件名詞提出 WARN；順手修掉在 Python 3.10 會 SyntaxError 的 f-string。
- `cast_registry.yaml` 移除 `visible_cast` 與 `reserved_unbound_picture`，`cast` 一律等於實際出場；資產新增 `summon_tokens` 供反向比對。`assets/segment_prompt.template.txt` 同步改寫指引。
- 既有提示詞尚未重做：seg02-a v03（7 FAIL）、seg02-b v04（6 FAIL）、SEG-01 a／b v04、SEG-03 S03b v01 均帶有排除宣告，需另開新版清除。

## 2026-09-14

- SEG-01 A／B 提示詞升至 v04：加入史詩管弦配樂、慢速滑軌與局部半速動作；v03 保留，更新製作狀態與決策。

- 依使用者指示完成 SEG-01 的 seg01-a／seg01-b H3 v03 獨立純文字提示詞與生成說明；各 362 幀，規劃剪為 11＋13 秒。更新 registry、manifest、進度與狀態，舊提示詞保留，未生成影片。

- 使用內建 imagegen 完成 SEG-01 Storyboard v02 四格黑白圖，附生成提示詞與鏡頭說明；圖像待使用者確認，保留 v01，尚未製作新版 H3 提示詞。

- 經使用者授權，新增正式文字分鏡 v0.3，保留 v0.2；僅改寫 SEG-01 及其事件、連續性與索引記錄，SEG-02～13 劇情維持原文。
- SEG-01 改為客戶爭吵、文件飛散的失控會議；鏡頭先呈現環境，再找到角落的主角，透過退椅撞牆與默默整理落紙呈現受困與疲勞。
- 保留 24 秒時長、四個鏡頭編號、既有 CAE 需求與主角承接台詞；離場椅子動線改為避開牆面，接續 SEG-02。
- 同步更新 README、AGENTS、DECISIONS、PROGRESS 與 PROJECT_STATE 的來源及狀態；SEG-01 Storyboard v01 標示需依新版重製，未製作新圖或 H3 提示詞。

## 2026-09-11

- 新增 S03b 獨立純文字 prompt 與生成說明 v01，涵蓋鏡頭 11；沿用 S03a 角色描述、兩圖順序與 seed 7301，補入 registry 與 manifest，更新 SEG-03 為兩段測試提示詞備齊。

- 新增 SEG-03 的 S03a MiniMax H3 Ref2VA 測試提示詞 v01，覆蓋鏡頭 09–10；限定只有女主角與 Cadi 出場。
- 建立 `cast_registry.yaml` 與 `manifest.csv`，固定 S03a 的角色 canonical description、seed、362 frames 與兩張參考圖上傳順序。
- 同步更新 `PROGRESS.md` 與 `PROJECT_STATE.json`；SEG-03 Storyboard 仍維持待集中審查，S03b 尚待製作。

## 2026-09-09

- 建立 `Cadi-Launch-Film` 專案資料夾。
- 匯入完整文字分鏡 v0.2。
- 匯入 SEG-01～SEG-13 Storyboard v01。
- 匯入 Cadi、主角臉部、主角服裝、Creo 與 Storyboard 畫風參考圖。
- 將 SEG-04 MiniMax H3 提示詞放回對應分段。
- 將舊版 MiniMax T2V 與 Seedance 文件移至 `archive/legacy-prompts`。
- 建立進度表、資產索引、機器可讀狀態與未來工作規則。
- 確立所有未來 MiniMax H3 提示詞的 Cadi 火焰規則：使用持續燃燒、具流體火焰動態的非固體青藍電漿描述，並明確排除果凍、橡膠與實心玻璃質感。
- 確立 MiniMax H3 圖片標籤規則：所有提示詞固定使用 `<Picture 1>` 綁定女主角、`<Picture 2>` 綁定 Cadi，兩者皆不得省略；其他圖片參考由 `<Picture 3>` 起編號。
- 新增 SEG-01 MiniMax H3 測試提示詞 v01：將原 24 秒內容拆成兩個各 15 秒的 Ref2VA 生成單元，並以 5 幀尾段 guide 規劃連續接合；維持 Storyboard 待審狀態。
- 新增 SEG-01 MiniMax H3 測試提示詞 v02：固定使用指定女主角設計表作 `<Picture 1>`、Cadi Design Sheet 作 `<Picture 2>`，並在兩段 prompt 中逐字加入指定的三段 `subject_definitions`。





## 2026-09-14｜SEG-02 修改

- 新增文字分鏡 v0.4 與 SEG-02 brief-v02；僅更新 SEG-02 劇情、事件與連續性記錄。保留 21 秒時長及既有鏡頭 05–08 編號。
- 新版六格 Storyboard 表現門外飛紙、衝出關門、背靠門嘆氣撥髮、手錶震動、RF 變更郵件及同事群組抱怨。舊版保留；新版待使用者審查，H3 待製作。
- 同步更新專案入口、決策、進度及機器可讀狀態。


## 2026-09-14｜SEG-02 H3 提示詞

- 使用者確認 Storyboard v02；新增 seg02-a／seg02-b MiniMax H3 v01 純文字提示詞與生成說明，保留文字劇情。
- 配樂以低沉鼓聲逐漸增強、加密為主，群組抱怨時推高緊張感；分段正片 9＋12 秒，各生成 362 幀。
- 同步更新 registry、manifest、PROGRESS、PROJECT_STATE 與決策；提示詞已驗證並記錄第三槽保留宣告例外，影片與音樂未生成。


## 2026-09-14｜SEG-02 H3 v02

- 依更新後 MiniMax H3 技能重新產生 A／B 六區段提示詞及生成說明 v02；補強角色保留分析、鏡頭內時間與聲音同步，保留固定圖片宣告的專案例外。
- 維持已確認劇情、Storyboard v02、9＋12 秒、低鼓漸強與 UI 原文。v01 保留；更新 registry、進度與狀態。manifest 生成參數未變；未生成影片。


## 2026-09-14｜SEG-02 H3 v03（潤飾）

- 只潤飾提示詞，不動劇情、Storyboard v02、UI 原文、9＋12 秒切分與 seed 7201。v02 原檔保留。
- 鏡內時間改為 `[0s-2s]` beat 標記（修正 v02 在 check_prompt.py 的「無時間碼」FAIL，並與 SEG-01 v04 一致）；補 `<Subject 2>` 排除宣告；刪除靜態生圖殘留句；A／B 的 retention_analysis 各自獨立。
- 補 A 的開門動作與閉合筆電、改用官方鏡頭語彙與 cuts to、重整兩段負面表列；把剪輯用說明移回生成說明，字元數壓在 6991／6998（上限 7000）。
- 新增 minimax-h3-generation-notes-v03.md；更新 registry 提示詞路徑、PROGRESS 與 PROJECT_STATE。影片與音樂未生成。


## 2026-09-14｜SEG-02 H3 v04（seg02-b 掛 Teams UI 參考圖）

- 依使用者決定，seg02-b 的 `<Picture 3>` 由「虛擬工廠保留宣告」改綁 Teams UI 參考圖並新增 `<Subject 3>`；其他 SEG 與 seg02-a 的第三槽規則不變。
- 新增介面保留分析（header、圖示、頭像欄、泡泡形狀、圓角、字級比例 fully_preserved），並明確禁止沿用參考圖自帶的範例訊息、人名、時間戳、未讀標記與真人頭像；[Shot 2] 的 app 圖示改為取自同一張圖。
- registry 新增 teams_ui 資產（priority 30，assets/software/teams-ui-reference-v01.png），seg02-b cast 改為三張圖並移除 reserved_unbound_picture；同步更新 ASSET_INDEX。
- 驗證：seg02-b v04 為 12 passed / 0 warnings / 0 failed，字元數 6991。參考圖檔案尚未放入，影片與音樂未生成。

## 2026-09-15｜SEG-01、SEG-02 劇情調整

- 2026-09-15：依使用者指示，SEG-01 保留吵雜外部 CAE 會議，刪除指派需求台詞 DLG-01–03 與女主角承接台詞 DLG-04，改為女主角收起筆電、悄悄離席；原 SEG-02 關門、背靠門嘆氣撥髮移至 SEG-01 結尾。SEG-02 從手錶震動開始，保留 RF 郵件與 Teams 抱怨。兩段維持 24 秒與 21 秒；SEG-03～13 不變。正式來源升至 v0.5，v0.4 保留；兩段新增 brief-v03，既有 Storyboard 與 H3 標為過時，待新版 Storyboard 確認後才製作 H3。
- 同步更新 README、AGENTS、PROGRESS、PROJECT_STATE、分段修訂紀錄與事件／對白／連續性表。

## 2026-09-15｜SEG-01 H3 v05

- 2026-09-15：使用者直接要求依 skill 生成 SEG-01 A／B H3；依 v0.5 文字製作 v05，新 Storyboard 尚未製作或確認。A 為吵雜會議與收拾起身，B 為悄悄離席、關門嘆氣；維持 11＋13 秒正片、seed 7101、各 362 幀。遵循 Absent Objects 僅掛女主角單圖，取消歷史未出場角色及場景保留槽；同步修正 SEG-01 manifest 上傳順序及 registry 提示詞路徑。兩段各 11 項通過、0 警告、0 失敗；影片未生成，v04 保留。

- 2026-09-15：依使用者指示，SEG-01 A 升至 v06，0–5 秒僅保留史詩器樂、現場聲與人聲静音；0–3 秒指責手勢、3–5 秒怒罵嘴型與噴口水極近特寫，均採四分之一速度。局部嘴型是客戶輪廓規則的授權例外；第5秒才加入模糊爭吵。B v05 保留不動，文字來源同步升至 v0.6，舊版保留。A 驗證11項通過、0警告、0失敗。

- 2026-09-15：依使用者指示新增 SEG-01 B v06，取消全段說話聲；史詩器樂貫通離席與關門，在 B 9 秒門扣接合瞬間硬切，9–10 秒完全靜默，10 秒才嘆氣，12–13 秒撥髮。A v06 保留，剪輯仍11＋13秒。來源升至 v0.7，SEG-02 只同步門後說話聲靜音的必要銜接；B檢查11項通過、0警告、0失敗。舊版保留。

- 2026-09-15：依使用者指示，SEG-01 A 升至 v07：(1) 史詩器樂從第一幀到最後一幀全程主導，不再有「靜音」描述；(2) 全段無人聲，刪除 shouting／Mandarin argument／breathing 等人聲字眼（避免召喚），嘴部特寫只保留畫面；(3) 筆電明確為銀色 HP，蓋背圓形 HP logo 對鏡頭並於合蓋、夾臂時保持可見，負面表列改用 no subtitles/no captions 以免壓掉 logo；(4) 由 2D 賽璐璐動畫改為寫實真人電影質感，參考圖只取身分與服裝。v06 保留；驗證 11 通過、0 警告、0 失敗。B v06 仍為 2D 動畫描述，待處理。

- 2026-09-15：SEG-01 B 升至 v07，與 A v07 統一：寫實真人電影質感取代 2D 動畫；筆電為銀色 HP、logo 全程朝外；刪除 argument／speech／inaudible／mouths moving／breathing／no spoken dialogue 等人聲字眼避免召喚；配樂寫明第一幀起全音量，9 秒門扣硬切、9–10 秒靜默、10 秒嘆氣結構不變。v06 保留。

## 2026-09-15｜SEG-01 Storyboard v04

- 依 v0.7 與 H3 A／B 最新節奏生成六格黑白 Storyboard，涵蓋指責手勢、怒罵嘴型與口水、收筆電、悄悄離席、關門及靜默後嘆氣。
- v03 首次生成稿保留；v04 將 03–06 的深色筆電修正為最新設定的銀色 HP 筆電。
- 新增 `brief-v04.md` 與 `storyboard-generation-prompt-v04.md`，同步更新進度與機器狀態；v04 待使用者確認。

## 2026-09-15｜H3 畫風召喚修正

- `cast_registry.yaml` 新增 `project.visual_style`；heroine 改掛 `heroine-photo-reference-v01.png`；heroine／cadi 的 retention 刪除 design-sheet 否定句，改為正向真人描述。
- skill：`base-en.txt` 改為專案有 visual_style 時逐字使用、不從參考圖推斷；`SKILL.md` 新增 Project Visual Style 硬規則。
- `check_prompt.py`：新增 `check_style`（2D／animation／cel／drawing style／illustrated／design sheet／storyboard 等字眼 FAIL、負面表列否定真人 FAIL、visual_style 逐字比對）；`NEGATIVE_ALLOW` 移除 live-action／photoreal。
- 範本、`AGENTS.md`、`PROJECT_STATE.json`、`ASSET_INDEX.md` 同步。既有提示詞未改版。
- SEG-02 依新規則出 A v05／B v06：畫風句逐字取自 visual_style、刪除 drawing style 否定句與 illustrated 字眼；A 改掛 heroine-photo-reference-v01.png；registry 與 manifest 路徑同步。兩段 12 passed／0 warn／0 fail。
## 2026-09-20｜正式文字分鏡升至 v0.9

- 依使用者指示，以已確認的SEG-09 Blender v06／H3 v01更新正式文字分鏡；新增 `screenplay/master-storyboard-v0.9.md`，v0.8保留。
- SEG-09改為26秒無台詞的Cadi彈指、Creo力量亮相、接風扇、五台協同搬運落位、俯瞰布局及Cadi降至風扇旁；同步更新分段表、EV-15／16、DLG-24–26狀態與09→10連續性。
- SEG-10鏡頭35–36只做必要銜接修正：對已落位風扇執行試排驗證；鏡頭37–38與DLG-27–29不變。

## 2026-09-23｜SEG-11 煉丹爐房間與 H3 A／B v04

- 新增 `screenplay/master-storyboard-v0.25.md`（v0.24 保留）：SEG-11 鏡頭39–41 改為 Ray 殘影高速進入 Finn 的科技煉丹爐房間、Finn 把資料丟入煉丹爐、爐體特寫轟鳴、Finn 從爐內取出結果交給 Ray；EV-18 與 10→11 連續性同步。
- SEG-11 新增 brief-v04、A／B prompt v04、cast-registry-v04、reference-manifest-v04、alchemy-lab-binding-v01、生成說明與驗證 v04；根 registry 新增 `alchemy_lab` 資產並更新 seg11-a／b。C 沿用 v03。影片未生成。
