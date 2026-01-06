#!/usr/bin/env python3
"""
Add screenshot figures to each chapter in guide.tex
"""

import re

# Mapping of chapter titles to screenshot filenames
chapter_to_screenshot = {
    "基本的な地図表示": "01-basic-map.png",
    "マーカーを追加": "02-marker.png",
    "ポップアップを表示": "03-popup.png",
    "複数のマーカー": "04-multiple-markers.png",
    "円を描画": "05-circle.png",
    "ポリゴンを描画": "06-polygon.png",
    "ポリラインを描画": "07-polyline.png",
    "地図のズームとパン操作": "08-zoom-pan.png",
    "異なるタイルレイヤー": "09-tile-layers.png",
    "地図のイベント処理": "10-map-events.png",
    "カスタムマーカーアイコン": "11-custom-icons.png",
    "ドラッグ可能なマーカー": "12-draggable-marker.png",
    "GeoJSONの基本": "13-geojson-basic.png",
    "GeoJSONのスタイリング": "14-geojson-styling.png",
    "レイヤーグループ": "15-layer-groups.png",
    "レイヤーコントロール": "16-layer-control.png",
    "スケールコントロール": "17-scale-control.png",
    "画像オーバーレイ": "18-image-overlay.png",
    "現在地表示（Geolocation）": "19-geolocation.png",
    "ツールチップ": "20-tooltip.png",
    "コロプレスマップ": "21-choropleth-map.png",
    "カスタムコントロール": "22-custom-control.png",
    "マーカークラスタリング（概念）": "23-marker-cluster-concept.png",
    "地図の境界制限": "24-map-bounds.png",
    "動的なマーカー追加・削除": "25-dynamic-markers.png",
    "アニメーション付きマーカー": "26-animated-marker.png",
    "WMSレイヤー": "27-wms-layer.png",
    "非地理的マップ": "28-non-geographical-map.png",
    "マップペイン": "29-map-panes.png",
    "総合アプリケーション（店舗検索）": "30-store-locator.png",
}

# Read the file
with open('../guide.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# For each chapter, add a figure after the \section{学習内容} paragraph
for title, screenshot in chapter_to_screenshot.items():
    # Escape special regex characters in title
    escaped_title = re.escape(title)

    # Pattern: find the chapter and its "学習内容" section
    # Look for the pattern: \section{学習内容}\n\n<description line>\n\n\begin{tipbox}
    pattern = rf'(\\chapter\{{{escaped_title}\}}.*?\\section\{{学習内容\}}\n\n)(.*?)(\n\n\\begin\{{tipbox\}})'

    def replacer(match):
        before = match.group(1)
        description = match.group(2)
        after = match.group(3)

        figure = f'''
\\begin{{figure}}[h]
    \\centering
    \\includegraphics[width=0.85\\textwidth]{{screenshots/{screenshot}}}
    \\caption{{サンプル実行結果}}
\\end{{figure}}
'''
        return before + description + figure + after

    content = re.sub(pattern, replacer, content, flags=re.DOTALL)

# Write the result
with open('../guide.tex', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Added figures to {len(chapter_to_screenshot)} chapters")
