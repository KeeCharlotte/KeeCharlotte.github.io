from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

old = '''.survival-subtree{display:grid;justify-items:center}.survival-subtree-root,.survival-priority-node{width:min(100%,440px);padding:20px 23px;border:1px solid var(--line-strong);border-radius:var(--radius-card);background:var(--card);text-align:center}.survival-subtree-root .survival-node-en,.survival-priority-node .survival-node-en{font-size:23px}.survival-tree-line{width:1px;height:30px;background:var(--rose-soft);opacity:.8}.survival-subbranches{position:relative;width:100%;display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px;padding-top:22px}.survival-subbranches::before{content:"";position:absolute;top:0;left:8.3%;right:8.3%;height:1px;background:var(--line-strong)}.survival-subnode{position:relative;min-height:144px;padding:18px 15px;border:1px solid var(--line);border-radius:10px;background:rgba(26,20,32,.5);cursor:pointer;text-align:left;transition:transform .22s var(--ease),border-color .2s ease,background .2s ease}.survival-subnode::before{content:"";position:absolute;top:-22px;left:50%;width:1px;height:22px;background:var(--line-strong)}.survival-subnode:hover,.survival-subnode:focus-visible,.survival-priority-node:hover,.survival-priority-node:focus-visible{transform:translateY(-2px);border-color:var(--rose);background:var(--card-hover);outline:none}.survival-node-num{display:block;color:var(--rose);font-family:var(--mono);font-size:11px;letter-spacing:.08em}.survival-node-en{display:block;margin-top:7px;color:var(--text);font-family:var(--serif);font-size:19px;font-weight:700;line-height:1.18}.survival-node-zh{display:block;margin-top:5px;color:var(--muted);font-size:13px;line-height:1.5}.survival-priority-node{border-color:var(--rose-soft);cursor:pointer;transition:transform .22s var(--ease),border-color .2s ease,background .2s ease}'''

new = '''.survival-subtree{display:grid;justify-items:center}.survival-subtree-root,.survival-priority-node{width:min(100%,440px);padding:20px 23px;border:1px solid var(--line-strong);border-radius:var(--radius-card);background:var(--card);text-align:center}.survival-subtree-root .survival-node-en,.survival-priority-node .survival-node-en{font-size:23px}.survival-tree-line{width:1px;height:30px;background:var(--rose-soft);opacity:.8}.survival-subbranches{position:relative;width:100%;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px;padding:22px 0}.survival-subbranches::before,.survival-subbranches::after{content:"";position:absolute;left:10%;right:10%;height:1px;background:var(--line-strong)}.survival-subbranches::before{top:0}.survival-subbranches::after{bottom:0}.survival-subnode{position:relative;min-height:144px;padding:18px 15px;border:1px solid var(--line);border-radius:10px;background:rgba(26,20,32,.5);cursor:pointer;text-align:left;transition:transform .22s var(--ease),border-color .2s ease,background .2s ease}.survival-subnode::before,.survival-subnode::after{content:"";position:absolute;left:50%;width:1px;height:22px;background:var(--line-strong)}.survival-subnode::before{top:-22px}.survival-subnode::after{bottom:-22px}.survival-subnode:hover,.survival-subnode:focus-visible,.survival-priority-node:hover,.survival-priority-node:focus-visible{transform:translateY(-2px);border-color:var(--rose);background:var(--card-hover);outline:none}.survival-node-num{display:block;color:var(--rose);font-family:var(--mono);font-size:11px;letter-spacing:.08em}.survival-node-en{display:block;margin-top:7px;color:var(--text);font-family:var(--serif);font-size:19px;font-weight:700;line-height:1.18}.survival-node-zh{display:block;margin-top:5px;color:var(--muted);font-size:13px;line-height:1.5}.survival-priority-node{border-color:var(--rose-soft);cursor:pointer;transition:transform .22s var(--ease),border-color .2s ease,background .2s ease}'''

if old not in html:
    raise SystemExit('Desktop Survival subtree CSS block not found')
html = html.replace(old, new, 1)

old_media = '''@media(max-width:900px){.survival-subbranches{grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;padding-top:0}.survival-subbranches::before,.survival-subnode::before{display:none}}'''
new_media = '''@media(max-width:900px){.survival-subbranches{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;padding:0}.survival-subnode{flex:0 1 calc(33.333% - 7px)}.survival-subbranches::before,.survival-subbranches::after,.survival-subnode::before,.survival-subnode::after{display:none}}'''
if old_media not in html:
    raise SystemExit('Tablet Survival subtree media block not found')
html = html.replace(old_media, new_media, 1)

old_mobile = '''@media(max-width:760px){.survival-index-heading,.survival-section-heading{align-items:flex-start;flex-direction:column;gap:7px}.survival-major-node{grid-template-columns:42px minmax(0,1fr) auto;padding:22px 20px;gap:13px}.survival-subbranches{grid-template-columns:1fr}.survival-subnode{min-height:0}.survival-reference{grid-template-columns:36px minmax(0,1fr) auto}.survival-category-head,.survival-detail-head{padding-top:20px}}'''
new_mobile = '''@media(max-width:760px){.survival-index-heading,.survival-section-heading{align-items:flex-start;flex-direction:column;gap:7px}.survival-major-node{grid-template-columns:42px minmax(0,1fr) auto;padding:22px 20px;gap:13px}.survival-subbranches{display:grid;grid-template-columns:1fr}.survival-subnode{min-height:0;width:100%;flex:none}.survival-reference{grid-template-columns:36px minmax(0,1fr) auto}.survival-category-head,.survival-detail-head{padding-top:20px}}'''
if old_mobile not in html:
    raise SystemExit('Mobile Survival subtree media block not found')
html = html.replace(old_mobile, new_mobile, 1)

for forbidden in [
    'grid-template-columns:repeat(6,minmax(0,1fr))',
    'left:8.3%;right:8.3%'
]:
    if forbidden in html:
        raise SystemExit('Old six-column tree CSS remains: ' + forbidden)

required = [
    'grid-template-columns:repeat(5,minmax(0,1fr))',
    '.survival-subbranches::before,.survival-subbranches::after',
    '.survival-subnode::before,.survival-subnode::after',
    'left:10%;right:10%',
    'justify-content:center'
]
for token in required:
    if token not in html:
        raise SystemExit('Required balanced-tree CSS missing: ' + token)

path.write_text(html, encoding='utf-8')
print('Balanced Survival Skills five-node tree layout applied.')
