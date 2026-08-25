from pathlib import Path
import re

INDEX = Path("index.html")
s = INDEX.read_text(encoding="utf-8")

css_pattern = r'^\s*\.fiction-detail-body\{.*?\.fiction-full-link-value\{color:var\(--muted-dark\);font-family:var\(--mono\);font-size:13px\}\s*$'
new_css = '''    .fiction-detail-body{display:grid;gap:46px;padding-bottom:12px}.fiction-hero-grid{display:grid;grid-template-columns:minmax(250px,330px) minmax(0,1fr);gap:42px;align-items:start;padding-top:8px;border-top:1px solid var(--line)}.fiction-cover-wrap{position:relative;margin-top:30px}.fiction-cover{display:block;width:100%;height:auto;border:1px solid var(--line-strong);border-radius:10px;box-shadow:0 24px 70px rgba(0,0,0,.28)}.fiction-overview{display:flex;min-height:500px;flex-direction:column;padding-top:30px}.fiction-section-kicker{margin:0;color:var(--rose);font-family:var(--mono);font-size:12px;font-weight:550;letter-spacing:.09em}.fiction-profile{margin-top:24px;padding:18px 0 19px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.fiction-profile-line{display:flex;flex-wrap:wrap;align-items:baseline;color:var(--muted);font-family:var(--mono);font-size:12px;line-height:1.7;letter-spacing:.035em}.fiction-profile-line span:not(:last-child)::after{content:"·";margin:0 12px;color:var(--muted-dark)}.fiction-profile-primary{color:var(--text);font-family:var(--serif);font-size:21px;font-weight:650;letter-spacing:0}.fiction-profile-tags{display:flex;flex-wrap:wrap;gap:7px 16px;margin-top:13px}.fiction-profile-tag{color:var(--muted);font-family:var(--mono);font-size:11px;line-height:1.65;letter-spacing:.025em}.fiction-thesis{margin:auto 0 0;padding:30px 0 2px;border-top:1px solid var(--line)}.fiction-thesis-zh{margin:0;color:var(--text);font-family:var(--serif);font-size:clamp(24px,2.8vw,34px);font-weight:650;line-height:1.48;letter-spacing:-.012em;white-space:pre-line}.fiction-thesis-en{margin:12px 0 0;color:var(--muted);font-family:var(--serif);font-size:15px;font-style:italic;line-height:1.7;white-space:pre-line}.fiction-section{padding-top:30px;border-top:1px solid var(--line)}.fiction-section-head{display:flex;align-items:baseline;gap:12px;margin-bottom:18px}.fiction-section-head h2{margin:0;color:var(--text);font-family:var(--serif);font-size:clamp(28px,3vw,38px);font-weight:700}.fiction-section-head span{color:var(--muted-dark);font-family:var(--mono);font-size:11px;letter-spacing:.08em}.fiction-synopsis{max-width:860px;margin:0;color:var(--text);font-size:16px;line-height:2;white-space:pre-line}.fiction-character-voices{border-top:1px solid var(--line)}.fiction-character-voice{display:grid;grid-template-columns:42px minmax(0,1fr);gap:22px;padding:30px 0;border-bottom:1px solid var(--line)}.fiction-character-index{padding-top:5px;color:var(--rose);font-family:var(--mono);font-size:11px;letter-spacing:.08em}.fiction-character-head{display:flex;align-items:baseline;justify-content:space-between;gap:24px;max-width:820px}.fiction-character-name{margin:0;color:var(--text);font-family:var(--serif);font-size:clamp(25px,3vw,32px);font-weight:700;line-height:1.2}.fiction-character-meta{flex:0 0 auto;color:var(--rose);font-family:var(--mono);font-size:11px;letter-spacing:.06em}.fiction-character-text{max-width:760px;margin:18px 0 0;color:var(--muted);font-size:15px;line-height:1.95;white-space:pre-line}.fiction-empty{min-height:126px;border:1px dashed var(--line);border-radius:10px;background:rgba(26,20,32,.34)}.fiction-full-link{display:flex;align-items:center;justify-content:space-between;gap:24px;min-height:94px;padding:24px;border:1px solid var(--line);border-radius:10px;background:rgba(26,20,32,.5)}.fiction-full-link-copy{color:var(--muted);font-size:14px}.fiction-full-link-value{color:var(--muted-dark);font-family:var(--mono);font-size:13px}'''
s, count = re.subn(css_pattern, new_css, s, count=1, flags=re.M)
if count != 1:
    raise RuntimeError(f"fiction CSS replacement count={count}")

old_900 = '.fiction-hero-grid{grid-template-columns:minmax(220px,300px) minmax(0,1fr)}.fiction-character-grid{grid-template-columns:1fr}'
new_900 = '.fiction-hero-grid{grid-template-columns:minmax(220px,300px) minmax(0,1fr)}.fiction-overview{min-height:450px}'
if old_900 not in s:
    raise RuntimeError("900px responsive fiction rule not found")
s = s.replace(old_900, new_900, 1)

old_760 = '.fiction-cover-wrap{max-width:300px;margin:30px auto 0}.fiction-profile{grid-template-columns:1fr}.fiction-section-head'
new_760 = '.fiction-cover-wrap{max-width:300px;margin:30px auto 0}.fiction-overview{min-height:0}.fiction-thesis{margin-top:28px}.fiction-character-voice{grid-template-columns:34px minmax(0,1fr);gap:14px;padding:25px 0}.fiction-character-head{align-items:flex-start;flex-direction:column;gap:5px}.fiction-section-head'
if old_760 not in s:
    raise RuntimeError("760px responsive fiction rule not found")
s = s.replace(old_760, new_760, 1)

if 'wordCount:"109,218",\n          genres:' in s:
    s = s.replace(
        'wordCount:"109,218",\n          genres:',
        'wordCount:"109,218",\n          status:"Completed",\n          genres:',
        1,
    )

old_name = '{name:"凡木悠浩矢",meta:'
if old_name not in s:
    raise RuntimeError("expected character name not found")
s = s.replace(old_name, '{name:"凡木悠 浩矢",meta:', 1)

render_pattern = r'    function renderFictionDetailBody\(work\)\{.*?\n    function showPortal'
new_render = '''    function renderFictionDetailBody(work){const body=document.getElementById("fictionDetailBody");body.replaceChildren();if(!work.detail)return;const detail=work.detail;const hero=document.createElement("section");hero.className="fiction-hero-grid";const coverWrap=document.createElement("div");coverWrap.className="fiction-cover-wrap";const cover=document.createElement("img");cover.className="fiction-cover";cover.src=detail.cover;cover.alt=work.title+" cover";cover.loading="eager";coverWrap.appendChild(cover);const overview=document.createElement("div");overview.className="fiction-overview";overview.appendChild(makeText("p","fiction-section-kicker","Work profile · 作品名片"));const profile=document.createElement("div");profile.className="fiction-profile";const profileLine=document.createElement("div");profileLine.className="fiction-profile-line";profileLine.append(makeText("span","fiction-profile-primary",detail.wordCount+" 字"),makeText("span","",detail.status||"Completed"),makeText("span","",work.period));const profileTags=document.createElement("div");profileTags.className="fiction-profile-tags";detail.genres.forEach(tag=>profileTags.appendChild(makeText("span","fiction-profile-tag","#"+tag)));profile.append(profileLine,profileTags);overview.appendChild(profile);if(detail.thesisZh||detail.thesisEn){const thesis=document.createElement("blockquote");thesis.className="fiction-thesis";if(detail.thesisZh)thesis.appendChild(makeText("p","fiction-thesis-zh",detail.thesisZh));if(detail.thesisEn)thesis.appendChild(makeText("p","fiction-thesis-en",detail.thesisEn));overview.appendChild(thesis)}hero.append(coverWrap,overview);body.appendChild(hero);
      const synopsis=document.createElement("section");synopsis.className="fiction-section";const synopsisHead=document.createElement("div");synopsisHead.className="fiction-section-head";synopsisHead.append(makeText("h2","","簡介"),makeText("span","","Synopsis"));synopsis.append(synopsisHead,makeText("p","fiction-synopsis",detail.synopsis));body.appendChild(synopsis);
      const characterSection=document.createElement("section");characterSection.className="fiction-section";const characterHead=document.createElement("div");characterHead.className="fiction-section-head";characterHead.append(makeText("h2","","角色介紹"),makeText("span","","In Their Own Words"));characterSection.appendChild(characterHead);const voices=document.createElement("div");voices.className="fiction-character-voices";detail.characters.forEach((character,index)=>{const voice=document.createElement("article");voice.className="fiction-character-voice";const number=makeText("span","fiction-character-index",String(index+1).padStart(2,"0"));const content=document.createElement("div");const head=document.createElement("div");head.className="fiction-character-head";head.append(makeText("h3","fiction-character-name",character.name),makeText("span","fiction-character-meta",character.meta));content.append(head,makeText("p","fiction-character-text",character.text));voice.append(number,content);voices.appendChild(voice)});characterSection.appendChild(voices);body.appendChild(characterSection);
      const excerpt=document.createElement("section");excerpt.className="fiction-section";const excerptHead=document.createElement("div");excerptHead.className="fiction-section-head";excerptHead.append(makeText("h2","","故事片段"),makeText("span","","Excerpt"));excerpt.append(excerptHead,document.createElement("div"));excerpt.lastChild.className="fiction-empty";body.appendChild(excerpt);
      const full=document.createElement("section");full.className="fiction-section";const fullHead=document.createElement("div");fullHead.className="fiction-section-head";fullHead.append(makeText("h2","","看完整版"),makeText("span","","Full Version"));const fullLink=document.createElement("div");fullLink.className="fiction-full-link";fullLink.append(makeText("span","fiction-full-link-copy",""),makeText("span","fiction-full-link-value","—"));full.append(fullHead,fullLink);body.appendChild(full)}
    function showPortal'''
s, count = re.subn(render_pattern, new_render, s, count=1, flags=re.S)
if count != 1:
    raise RuntimeError(f"render replacement count={count}")

required = [
    "In Their Own Words",
    "凡木悠 浩矢",
    "fiction-character-voices",
    "fiction-profile-line",
    'cover:"assets/unreachable-sincerity-cover.webp"',
]
for token in required:
    if token not in s:
        raise RuntimeError(f"post-update verification failed: {token}")
if "fiction-character-grid" in s:
    raise RuntimeError("legacy character grid remains")

INDEX.write_text(s, encoding="utf-8")
