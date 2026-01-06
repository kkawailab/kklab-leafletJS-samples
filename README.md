# Leaflet.js 学習用サンプル集

Leaflet.js を初心者から上級者まで段階的に学べる30個のサンプルファイル集です。

各サンプルは独立したHTMLファイルで、CSS・JavaScriptがすべて含まれているため、ブラウザで直接開いて動作を確認できます。

---

## 学習ガイドブック

本サンプル集には、詳細な解説付きの**学習ガイドブック（PDF）**が付属しています。

**[guide.pdf](guide.pdf)** - Leaflet.js 学習ガイドブック（約160ページ）

ガイドブックの内容：
- 各サンプルの詳細な解説とコード説明
- 練習問題と模範解答
- APIリファレンス（主要なメソッド・オプション）
- タイルプロバイダー一覧とattribution設定
- LLMを活用した効率的な学習プロンプト集（20本）

---

## 公式ドキュメント

- [Leaflet公式サイト](https://leafletjs.com/)
- [APIリファレンス](https://leafletjs.com/reference.html)
- [チュートリアル](https://leafletjs.com/examples.html)

---

## 目次

### 初級レベル（01-10）

基本的な地図表示からシンプルな図形描画まで。

| No. | ファイル名 | 学習内容 |
|-----|-----------|---------|
| 01 | [01-basic-map.html](samples/01-basic-map.html) | 基本的な地図表示 - `L.map()`, `L.tileLayer()` の使い方 |
| 02 | [02-marker.html](samples/02-marker.html) | マーカーを追加 - `L.marker()` の基本 |
| 03 | [03-popup.html](samples/03-popup.html) | ポップアップを表示 - `bindPopup()`, `openPopup()` |
| 04 | [04-multiple-markers.html](samples/04-multiple-markers.html) | 複数のマーカー - 配列からマーカーを生成 |
| 05 | [05-circle.html](samples/05-circle.html) | 円を描画 - `L.circle()`, `L.circleMarker()` |
| 06 | [06-polygon.html](samples/06-polygon.html) | ポリゴンを描画 - `L.polygon()`, `L.rectangle()` |
| 07 | [07-polyline.html](samples/07-polyline.html) | ポリラインを描画 - `L.polyline()` でルート表示 |
| 08 | [08-zoom-pan.html](samples/08-zoom-pan.html) | 地図のズームとパン操作 - `setView()`, `flyTo()`, `fitBounds()` |
| 09 | [09-tile-layers.html](samples/09-tile-layers.html) | 異なるタイルレイヤー - OSM, CartoDB, 国土地理院など |
| 10 | [10-map-events.html](samples/10-map-events.html) | 地図のイベント処理 - click, zoom, move イベント |

### 中級レベル（11-20）

カスタマイズとデータ表示。

| No. | ファイル名 | 学習内容 |
|-----|-----------|---------|
| 11 | [11-custom-icons.html](samples/11-custom-icons.html) | カスタムマーカーアイコン - `L.icon()`, `L.divIcon()` |
| 12 | [12-draggable-marker.html](samples/12-draggable-marker.html) | ドラッグ可能なマーカー - `draggable: true`, イベント |
| 13 | [13-geojson-basic.html](samples/13-geojson-basic.html) | GeoJSONの基本 - `L.geoJSON()` の使い方 |
| 14 | [14-geojson-styling.html](samples/14-geojson-styling.html) | GeoJSONのスタイリング - データに基づく動的スタイル |
| 15 | [15-layer-groups.html](samples/15-layer-groups.html) | レイヤーグループ - `L.layerGroup()`, `L.featureGroup()` |
| 16 | [16-layer-control.html](samples/16-layer-control.html) | レイヤーコントロール - `L.control.layers()` でUIを追加 |
| 17 | [17-scale-control.html](samples/17-scale-control.html) | スケールコントロール - `L.control.scale()` と各種コントロール |
| 18 | [18-image-overlay.html](samples/18-image-overlay.html) | 画像オーバーレイ - `L.imageOverlay()`, `L.svgOverlay()` |
| 19 | [19-geolocation.html](samples/19-geolocation.html) | 現在地表示 - `map.locate()` で位置情報取得 |
| 20 | [20-tooltip.html](samples/20-tooltip.html) | ツールチップ - `bindTooltip()` の各種オプション |

### 上級レベル（21-30）

高度な機能とアプリケーション開発。

| No. | ファイル名 | 学習内容 |
|-----|-----------|---------|
| 21 | [21-choropleth-map.html](samples/21-choropleth-map.html) | コロプレスマップ（色分け地図） - データ可視化 |
| 22 | [22-custom-control.html](samples/22-custom-control.html) | カスタムコントロールの作成 - `L.Control.extend()` |
| 23 | [23-marker-cluster-concept.html](samples/23-marker-cluster-concept.html) | マーカークラスタリングの概念 - 大量マーカーの管理 |
| 24 | [24-map-bounds.html](samples/24-map-bounds.html) | 地図の境界と制限 - `maxBounds`, `minZoom`, `maxZoom` |
| 25 | [25-dynamic-markers.html](samples/25-dynamic-markers.html) | 動的なマーカー追加・削除 - CRUD操作 |
| 26 | [26-animated-marker.html](samples/26-animated-marker.html) | アニメーション付きマーカー - CSS/JSアニメーション |
| 27 | [27-wms-layer.html](samples/27-wms-layer.html) | WMSレイヤー - `L.tileLayer.wms()` の使い方 |
| 28 | [28-non-geographical-map.html](samples/28-non-geographical-map.html) | 非地理的マップ - `L.CRS.Simple` でフロアプラン |
| 29 | [29-map-panes.html](samples/29-map-panes.html) | マップペイン - レイヤーの重なり順を制御 |
| 30 | [30-store-locator.html](samples/30-store-locator.html) | 総合アプリケーション - 店舗検索システム |

---

## 使い方

1. このリポジトリをクローンまたはダウンロード
2. `samples` フォルダ内のHTMLファイルをブラウザで開く
3. 各サンプルの説明とコード例を読みながら学習

```bash
# リポジトリをクローン
git clone https://github.com/kkawailab/kklab-leafletJS-samples.git

# ディレクトリに移動
cd kklab-leafletJS-samples

# ブラウザでサンプルを開く（例）
open samples/01-basic-map.html
```

## 動作環境

- モダンブラウザ（Chrome, Firefox, Safari, Edge）
- インターネット接続（タイルレイヤーの読み込みに必要）
- Leaflet.js v1.9.4（CDNから読み込み）

## 学習の進め方

1. **初心者**: 01〜10を順番に進めて基本を理解
2. **中級者**: 11〜20でカスタマイズ方法を学習
3. **上級者**: 21〜30で実践的なアプリケーション開発を体験

各サンプルには以下が含まれています：
- 学習内容の説明
- 実際に動作する地図
- 重要なコード部分のサンプル

より深く学習したい場合は、[学習ガイドブック（PDF）](guide.pdf)を参照してください。

## ディレクトリ構成

```
.
├── guide.pdf          # 学習ガイドブック
├── index.html         # Webサイト用インデックス
└── samples/           # 30個のHTMLサンプル
```

## ライセンス

このサンプル集は学習目的で自由に使用できます。

## 参考リンク

- [Leaflet公式ドキュメント](https://leafletjs.com/reference.html)
- [OpenStreetMap](https://www.openstreetmap.org/)
- [CartoDB Basemaps](https://carto.com/basemaps/)
- [国土地理院タイル](https://maps.gsi.go.jp/development/ichiran.html)
