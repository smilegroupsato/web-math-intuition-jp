# Cleanup annotation placement and note-box styling: 2026-06-06 JST
from pathlib import Path
import re

CSS_VERSION = '20260606-note-style3'
ROOT = Path('site')
info_path = ROOT / 'information-and-relation.html'
image_path = ROOT / 'image-and-preimage-emotion.html'
css_path = ROOT / 'assets' / 'style.css'
page_paths = [
    info_path,
    image_path,
    ROOT / 'linear-vector.html',
    ROOT / 'linear-basis-coordinate.html',
    ROOT / 'linear-equation-geometry.html',
]

def cache_bust_css_link(html: str) -> str:
    return re.sub(
        r'href="assets/style\.css(?:\?v=[^"]*)?"',
        f'href="assets/style.css?v={CSS_VERSION}"',
        html,
    )

def extract_note(html: str, title_fragment: str) -> tuple[str, str | None]:
    pattern = r'\s*(<aside class="note-box">\s*<h3>' + re.escape(title_fragment) + r'.*?</aside>)\s*'
    match = re.search(pattern, html, flags=re.S)
    if not match:
        return html, None
    return html[:match.start()] + '\n' + html[match.end():], match.group(1) + '\n'

# Strengthen the shared note-box style and remove old pseudo-element hacks.
css = css_path.read_text(encoding='utf-8')
css = re.sub(r'#gap::after,#llm-compression::after,#info-quantity::after\{.*?\}(?=#gap::after)', '', css)
css = re.sub(r'#gap::after\{.*?\}(?=#llm-compression::after)', '', css)
css = re.sub(r'#llm-compression::after\{.*?\}(?=#info-quantity::after)', '', css)
css = re.sub(r'#info-quantity::after\{.*?\}(?=\.page-nav)', '', css)
strong_note_css = 'aside.note-box{display:block!important;margin:32px 0!important;padding:20px 22px!important;border:1px solid rgba(185,150,93,.38)!important;border-left:6px solid #b9965d!important;border-radius:14px!important;background:rgba(255,250,241,.82)!important;box-shadow:0 10px 24px rgba(24,32,47,.06)!important}aside.note-box h3{margin-top:0!important;font-size:22px!important;color:#7b5a2f!important}aside.note-box p,aside.note-box ul,aside.note-box blockquote{font-size:15px!important}aside.note-box blockquote{background:rgba(255,255,255,.62)!important}'
if 'aside.note-box{display:block!important' not in css:
    css += strong_note_css
css_path.write_text(css, encoding='utf-8')

# Move the Shannon note from immediately after h2 to the end of section 7.
info = cache_bust_css_link(info_path.read_text(encoding='utf-8'))
info, shannon_note = extract_note(info, '注記｜情報理論とシャノン情報量')
if shannon_note:
    marker = '      <p>その情報を成立させる候補空間、基準、関係、変換を見ることである。</p>\n'
    if marker not in info:
        raise SystemExit('info section end marker not found')
    info = info.replace(marker, marker + shannon_note, 1)
info_path.write_text(info, encoding='utf-8')

# Reinsert the perspective projection note at the correct boundary if it exists.
image = cache_bust_css_link(image_path.read_text(encoding='utf-8'))
image, projection_note = extract_note(image, '注記｜透視投影の定義域')
if projection_note:
    marker = '<h2 id="observation-map">8. 写真を観測写像として見る</h2>\n'
    if marker not in image:
        raise SystemExit('projection marker not found')
    image = image.replace(marker, projection_note + marker, 1)
image_path.write_text(image, encoding='utf-8')

# Cache-bust CSS links on the other note-bearing pages.
for path in page_paths:
    if path.exists() and path not in (info_path, image_path):
        path.write_text(cache_bust_css_link(path.read_text(encoding='utf-8')), encoding='utf-8')
