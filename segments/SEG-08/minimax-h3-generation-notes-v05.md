# SEG-08 室內工站 H3 v05

2026-09-22。依使用者指示，承接 SEG-07 的 drop 室內工站，場景改為 `assets/environments/室內.jpg` 並實際上傳給 H3。劇情、角色動作、台詞、seed 與 A 13秒＋B 10秒不變。

## 版本

- A：`seg08-a-minimax-h3-prompt-v05.txt`，室內圖為 `<Picture 4>`；女主角、Cadi、Placement 仍為 `<Picture 1>`～`<Picture 3>`。
- B：`seg08-b-minimax-h3-prompt-v03.txt`，室內圖為 `<Picture 3>`；女主角／Cadi 仍為 `<Picture 1>`／`<Picture 2>`，CPU 動作仍為 `<Video 1>`。
- 場景綁定：`indoor-scene-binding-v01.md`。
- registry／manifest：`cast-registry-v05.yaml`、`reference-manifest-v05.json`。

## 上傳順序

- A：`ref_image_0` 女主角、`ref_image_1` Cadi、`ref_image_2` Placement、`ref_image_3` 室內工站。
- B：`ref_image_0` 女主角、`ref_image_1` Cadi、`ref_image_2` 室內工站；另掛 `<Video 1>` CPU 側移與停住影片。

影片尚未生成。
