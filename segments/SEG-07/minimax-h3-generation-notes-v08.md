# SEG-07 室內工站 H3 v08

2026-09-22。依使用者指示，drop 工站由虛擬工廠街區文字場景改為 `assets/environments/室內.jpg`，該圖會實際上傳給 H3。劇情、動作、台詞、seed 與 14＋12 秒時長不變。

## 版本

- A：`seg07-a-minimax-h3-prompt-v05.txt`，室內圖新增為 `<Picture 3>`；Cadi／drop 仍為 `<Picture 1>`／`<Picture 2>`，散落排列動作仍為 `<Video 1>`。
- B：`seg07-b-minimax-h3-prompt-v08.txt`，室內圖新增為 `<Picture 4>`；女主角／Cadi／最終布局仍為 `<Picture 1>`／`<Picture 2>`／`<Picture 3>`。
- 場景綁定：`indoor-scene-binding-v01.md`。
- registry／manifest：`cast-registry-v08.yaml`、`reference-manifest-v08.json`。

## 上傳順序

- A：`ref_image_0` Cadi、`ref_image_1` drop、`ref_image_2` 室內工站；另掛 `<Video 1>` 散落排列影片。
- B：`ref_image_0` 女主角、`ref_image_1` Cadi、`ref_image_2` 最終布局、`ref_image_3` 室內工站。

B 的最終布局圖路徑仍待提供。影片尚未生成。
