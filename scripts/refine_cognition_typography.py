from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

replacements = [
    (
        'https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,100..900&family=Geist:wght@100..900&family=Geist+Mono:wght@100..900&display=swap',
        'https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,100..900&family=Geist:wght@100..900&family=Geist+Mono:wght@100..900&family=Noto+Sans+TC:wght@400;500;600;700&family=Noto+Serif+TC:wght@400;500;600;700&display=swap'
    ),
    (
        '--muted-dark:#6b6058;--rose:#8D7BB2;',
        '--muted-dark:#6b6058;--muted-readable:#8A7D75;--rose:#8D7BB2;'
    ),
    (
        '--serif:"Fraunces",Georgia,"Times New Roman",serif;--sans:"Geist",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;',
        '--serif:"Fraunces","Noto Serif TC",Georgia,"Times New Roman",serif;--sans:"Geist","Noto Sans TC",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;'
    ),
    (
        '.cognition-index-summary{color:var(--muted-dark);',
        '.cognition-index-summary{color:var(--muted-readable);'
    ),
    (
        '.cognition-card-type,.cognition-card-count{color:var(--muted-dark);',
        '.cognition-card-type,.cognition-card-count{color:var(--muted-readable);'
    ),
    (
        '.cognition-theme-card.developing{grid-column:1/-1;min-height:190px;border-color:var(--line-strong);background:var(--card)}',
        '.cognition-theme-card.developing{grid-column:1/-1;min-height:190px;border-color:var(--line-strong);background:var(--card)}.cognition-theme-card:last-child:not(.developing){grid-column:1/-1;width:calc(50% - 7px);justify-self:center}'
    ),
    (
        '.cognition-thought{max-width:870px;',
        '.cognition-thought{max-width:760px;'
    ),
    (
        '.cognition-related-label{margin-right:4px;padding-top:4px;color:var(--muted-dark);',
        '.cognition-related-label{margin-right:4px;padding-top:4px;color:var(--muted-readable);'
    ),
    (
        '.cognition-chain-step{position:relative;min-height:102px;display:flex;align-items:center;justify-content:center;padding:16px 12px;border:1px solid var(--line);border-radius:10px;background:rgba(26,20,32,.45);color:var(--text);font-family:var(--mono);font-size:11px;line-height:1.55;text-align:center}',
        '.cognition-chain-step{position:relative;min-height:102px;display:flex;align-items:center;justify-content:center;padding:16px 12px;border:1px solid var(--line);border-radius:10px;background:rgba(26,20,32,.45);color:var(--text);font-family:var(--mono);font-size:11px;line-height:1.55;text-align:center;white-space:pre-line}'
    ),
    (
        'footer{padding:28px 0 34px;color:var(--muted-dark);',
        'footer{padding:28px 0 34px;color:var(--muted-readable);'
    ),
    (
        '@media(max-width:760px){.cognition-theme-grid{grid-template-columns:1fr}.cognition-theme-card.developing{grid-column:auto}',
        '@media(max-width:760px){.cognition-theme-grid{grid-template-columns:1fr}.cognition-theme-card.developing{grid-column:auto}.cognition-theme-card:last-child:not(.developing){grid-column:auto;width:100%;justify-self:stretch}'
    ),
]

for old, new in replacements:
    if old not in text:
        raise SystemExit(f'Expected anchor not found: {old[:120]}')
    text = text.replace(old, new, 1)

required = [
    'Noto+Sans+TC',
    'Noto+Serif+TC',
    '--muted-readable:#8A7D75',
    '"Noto Serif TC"',
    '"Noto Sans TC"',
    '.cognition-theme-card:last-child:not(.developing){grid-column:1/-1;width:calc(50% - 7px);justify-self:center}',
    '.cognition-thought{max-width:760px;',
    'text-align:center;white-space:pre-line}',
    '.cognition-related-label{margin-right:4px;padding-top:4px;color:var(--muted-readable);',
    'footer{padding:28px 0 34px;color:var(--muted-readable);',
    '.cognition-theme-card:last-child:not(.developing){grid-column:auto;width:100%;justify-self:stretch}',
]
for item in required:
    if item not in text:
        raise SystemExit(f'Missing expected result: {item}')

path.write_text(text, encoding='utf-8')
