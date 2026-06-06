from pathlib import Path

path = Path('site/image-and-preimage-emotion.html')
html = path.read_text(encoding='utf-8')

html = html.replace(
    '$$P(x\\mid y)= rac{P(y\\mid x)P(x)}{P(y)}$$',
    r'$$P(x\mid y)=\frac{P(y\mid x)P(x)}{P(y)}$$',
)
html = html.replace(
    '$$P(x\mid y)= rac{P(y\mid x)P(x)}{P(y)}$$',
    r'$$P(x\mid y)=\frac{P(y\mid x)P(x)}{P(y)}$$',
)
html = html.replace(
    '\\(F:X o Y\\)',
    r'\(F:X\to Y\)',
)
html = html.replace(
    '\(F:X o Y\)',
    r'\(F:X\to Y\)',
)

path.write_text(html, encoding='utf-8')
