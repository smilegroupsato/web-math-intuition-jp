from pathlib import Path
import re

ROOT = Path('site')
PAGES = [
    ROOT / 'information-and-relation.html',
    ROOT / 'image-and-preimage-emotion.html',
    ROOT / 'linear-vector.html',
    ROOT / 'linear-basis-coordinate.html',
    ROOT / 'linear-equation-geometry.html',
]
INFO = ROOT / 'information-and-relation.html'
IMAGE = ROOT / 'image-and-preimage-emotion.html'
CSS_VERSION = '20260606-note-style4'

INLINE_STYLE = '''
<style id="note-box-inline-style">
  aside.note-box {
    display: block !important;
    margin: 32px 0 !important;
    padding: 20px 22px !important;
    border: 1px solid rgba(185, 150, 93, 0.38) !important;
    border-left: 6px solid #b9965d !important;
    border-radius: 14px !important;
    background: rgba(255, 250, 241, 0.82) !important;
    box-shadow: 0 10px 24px rgba(24, 32, 47, 0.06) !important;
  }
  aside.note-box h3 {
    margin-top: 0 !important;
    font-size: 22px !important;
    color: #7b5a2f !important;
  }
  aside.note-box p,
  aside.note-box ul,
  aside.note-box blockquote {
    font-size: 15px !important;
  }
  aside.note-box blockquote {
    background: rgba(255, 255, 255, 0.62) !important;
  }
</style>
'''

BAYES_NOTE = '''
      <aside class="note-box">
        <h3>注記｜候補逆像・\(P(x\mid y)\)・ベイズ的な見方</h3>
        <p>ここで \(P(x\mid y)\) と書くなら、これは確率分布である。つまり、暗黙にいくつかのものが必要になる。</p>
        <ul>
          <li>候補世界 \(x\) の空間</li>
          <li>観測像 \(y\)</li>
          <li>尤度 \(P(y\mid x)\)</li>
          <li>事前分布 \(P(x)\)</li>
          <li>観測者の経験・期待・文化的モデル</li>
        </ul>
        <p>より数学的にするなら、次のベイズ的な見方を置ける。</p>
        <div class="math-block">$$P(x\mid y)\propto P(y\mid x)P(x)$$</div>
        <p>そして、情緒をこう近似できる。</p>
        <blockquote>情緒は、観測像 \(y\) から候補世界 \(x\) を復元するとき、候補分布 \(P(x\mid y)\) が一意に鋭く収束せず、複数の候補・期待・破綻・補完のあいだに偏りを持って揺れている状態として近似できる。</blockquote>
        <p>ベイズ的な見方とは、観測された結果だけから世界をいきなり決めるのではなく、あらかじめ持っている候補世界の重みづけと、観測像がその候補世界からどれくらい生じやすいかを組み合わせて、候補の重みを更新する見方である。</p>
        <p>まず、\(P(x)\) は事前分布である。これは、像 \(y\) を見る前に、どの世界 \(x\) がどれくらいありそうかを表す。人間の視覚で言えば、床は下にあるはずだ、光は上から来ることが多い、建物には入口があるはずだ、身体は重力に従うはずだ、といった経験や文化的な世界モデルがここに入る。</p>
        <p>次に、\(P(y\mid x)\) は尤度である。これは、ある候補世界 \(x\) が本当にあったとしたら、いま見えている像 \(y\) がどれくらい生じやすいかを表す。写真や絵画を見る場合には、輪郭、明暗、影、遠近、遮蔽、線の接続、比率などが、この候補世界と像の整合性を支える。</p>
        <p>そして、\(P(x\mid y)\) は事後分布である。これは、像 \(y\) を見た後で、どの世界 \(x\) がどれくらいありそうかを表す。ベイズの定理では、これは次のように書ける。</p>
        <div class="math-block">$$P(x\mid y)=\frac{P(y\mid x)P(x)}{P(y)}$$</div>
        <p>ここで \(P(y)\) は正規化定数であり、すべての候補世界について確率の合計が1になるように調整する役割を持つ。候補同士の相対的な重みを見るだけなら、\(P(x\mid y)\propto P(y\mid x)P(x)\) と書けばよい。</p>
        <p>候補逆像とは、像 \(y\) に写りうる世界 \(x\) の集まりである。理想化された決定論的な写像 \(F:X\to Y\) なら、候補逆像は \(F^{-1}(\{y\})\) と書ける。しかし現実の写真や絵画、視覚経験では、ノイズ、曖昧さ、遮蔽、遠近、描写上の省略があるため、「完全に \(F(x)=y\) を満たす候補」だけでなく、「この像をかなりよく説明する候補」も問題になる。</p>
        <p>そのため、候補逆像を確率分布として見ると、単に集合があるのではなく、その中に濃淡が生じる。ある候補世界は強くありそうに感じられ、別の候補世界は弱くしか感じられない。ある候補は局所的にはありそうだが、全体としては破綻する。ある候補は文化的期待には合うが、像の情報とは食い違う。</p>
        <p>ここで情緒が立ち上がる。情緒は、ただ \(x\) が一つに決まることではなく、候補世界の分布が鋭く一点へ収束せず、期待、補完、破綻、不在、ありそうさ、ありえなさのあいだで偏りを持ったまま揺れている状態に近い。</p>
      </aside>
'''

def cache_bust_css(html: str) -> str:
    return re.sub(
        r'href="assets/style\.css(?:\?v=[^"]*)?"',
        f'href="assets/style.css?v={CSS_VERSION}"',
        html,
    )

def ensure_inline_style(html: str) -> str:
    html = re.sub(
        r'\n\s*<style id="note-box-inline-style">.*?</style>\s*',
        '\n',
        html,
        flags=re.S,
    )
    return html.replace('</head>', INLINE_STYLE + '</head>', 1)

def move_shannon_note(info: str) -> str:
    pattern = r'\s*(<aside class="note-box">\s*<h3>注記｜情報理論とシャノン情報量</h3>.*?</aside>)\s*'
    match = re.search(pattern, info, flags=re.S)
    if not match:
        return info
    note = match.group(1) + '\n'
    info = info[:match.start()] + '\n' + info[match.end():]
    marker = '      <p>その情報を成立させる候補空間、基準、関係、変換を見ることである。</p>\n'
    if marker not in info:
        return info + '\n' + note
    return info.replace(marker, marker + note, 1)

for path in PAGES:
    html = path.read_text(encoding='utf-8')
    html = cache_bust_css(html)
    html = ensure_inline_style(html)
    path.write_text(html, encoding='utf-8')

info = INFO.read_text(encoding='utf-8')
info = move_shannon_note(info)
INFO.write_text(info, encoding='utf-8')

image = IMAGE.read_text(encoding='utf-8')
if '注記｜候補逆像・' not in image:
    marker = '      <p>\n        したがって、ここでいう「名づけ以前」とは'
    if marker not in image:
        raise SystemExit('Bayesian note marker not found')
    image = image.replace(marker, BAYES_NOTE + marker, 1)
IMAGE.write_text(image, encoding='utf-8')
