#!/usr/bin/env python3
"""
Add missing screenshots to chapters in guide.tex
"""

import re

# Mapping: chapter title -> screenshot filename -> caption
chapter_figures = {
    "ポップアップを表示": ("03-popup.png", "ポップアップの表示"),
    "ポリゴンを描画": ("06-polygon.png", "ポリゴンの描画"),
    "ポリラインを描画": ("07-polyline.png", "ポリラインの描画"),
    "地図のズームとパン操作": ("08-zoom-pan.png", "ズームとパン操作"),
    "地図のイベント処理": ("10-map-events.png", "イベント処理の実装"),
    "カスタムマーカーアイコン": ("11-custom-icons.png", "カスタムアイコンの表示"),
    "ドラッグ可能なマーカー": ("12-draggable-marker.png", "ドラッグ可能なマーカー"),
    "GeoJSONのスタイリング": ("14-geojson-styling.png", "GeoJSONのスタイリング"),
    "レイヤーグループ": ("15-layer-groups.png", "レイヤーグループの管理"),
    "レイヤーコントロール": ("16-layer-control.png", "レイヤーコントロール"),
    "スケールコントロール": ("17-scale-control.png", "スケールコントロール"),
    "画像オーバーレイ": ("18-image-overlay.png", "画像オーバーレイ"),
    "現在地表示（Geolocation）": ("19-geolocation.png", "現在地の表示"),
    "ツールチップ": ("20-tooltip.png", "ツールチップの表示"),
    "カスタムコントロール": ("22-custom-control.png", "カスタムコントロール"),
    "地図の境界制限": ("24-map-bounds.png", "境界制限の設定"),
    "動的なマーカー追加・削除": ("25-dynamic-markers.png", "動的なマーカー管理"),
    "WMSレイヤー": ("27-wms-layer.png", "WMSレイヤーの表示"),
    "非地理的マップ": ("28-non-geographical-map.png", "非地理的マップ"),
    "マップペイン": ("29-map-panes.png", "マップペインの制御"),
}

# Read the file
with open('../guide.tex', 'r', encoding='utf-8') as f:
    content = f.read()

added_count = 0

for title, (screenshot, caption) in chapter_figures.items():
    escaped_title = re.escape(title)

    # Check if this chapter already has the correct screenshot
    check_pattern = rf'\\chapter\{{{escaped_title}\}}.*?\\includegraphics.*?{screenshot}'
    if re.search(check_pattern, content, flags=re.DOTALL):
        print(f"Skipping {title}: already has correct figure")
        continue

    # Pattern to find the chapter and add figure after learning content description
    # Look for: \section{学習内容}\n\n<description>\n\n\begin{tipbox/methodbox/warnbox}
    pattern = rf'(\\chapter\{{{escaped_title}\}}.*?\\section\{{学習内容\}}\n\n)(.*?)(\n\n\\begin\{{(?:tipbox|methodbox|warnbox))'

    def replacer(match):
        before = match.group(1)
        description = match.group(2)
        after = match.group(3)

        figure = f'''
\\begin{{figure}}[h]
    \\centering
    \\includegraphics[width=0.85\\textwidth]{{screenshots/{screenshot}}}
    \\caption{{{caption}}}
\\end{{figure}}
'''
        return before + description + figure + after

    new_content = re.sub(pattern, replacer, content, count=1, flags=re.DOTALL)

    if new_content != content:
        content = new_content
        added_count += 1
        print(f"Added figure to: {title}")
    else:
        print(f"Could not add figure to: {title}")

# Write the result
with open('../guide.tex', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nTotal figures added: {added_count}")
