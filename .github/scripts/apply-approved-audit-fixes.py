from pathlib import Path
import re

path = Path("index.html")
text = path.read_text(encoding="utf-8")


def replace_once(old: str, new: str, label: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly 1 match, found {count}")
    text = text.replace(old, new, 1)


def replace_all(old: str, new: str, label: str, min_count: int = 1) -> None:
    global text
    count = text.count(old)
    if count < min_count:
        raise SystemExit(f"{label}: expected at least {min_count} match(es), found {count}")
    text = text.replace(old, new)


def sub_once(pattern: str, repl: str, label: str, flags: int = 0) -> None:
    global text
    updated, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly 1 match, found {count}")
    text = updated


# 1. Games copy: sentence case + punctuation.
replace_once(
    'descriptionEn:"A Civilization-Building Game based on real-world rules",descriptionZh:"基於真實世界規則的文明建立遊戲"',
    'descriptionEn:"A civilization-building game based on real-world rules.",descriptionZh:"基於真實世界規則的文明建立遊戲。"',
    "Games description copy",
)

# 2. Fiction: preserve conversational intro; add known start period to detail data.
replace_once(
    '"interference-of-fate-and-time":{title:"時空干涉",subtitle:"Interference of Fate and Time",period:"—"}',
    '"interference-of-fate-and-time":{title:"時空干涉",subtitle:"Interference of Fate and Time",period:"Jun 2022"}',
    "Fiction start period",
)

# 3. Discipline: Chinese-only routine descriptions, plus the explicit English corrections.
routine_english = [
    '<p class="primary-en">Go to sleep</p>',
    '<p class="primary-en">Brush teeth and wash face</p>',
    '<p class="primary-en">20 mins of meditation</p>',
    '<p class="primary-en">30 mins of running</p>',
    '<p class="primary-en">15 mins of cold shower</p>',
    '<p class="primary-en">Breakfast / Plan the day’s tasks / Intensive morning study</p>',
]
for item in routine_english:
    if text.count(item) != 1:
        raise SystemExit(f"Routine English description mismatch: {item}")
    text = text.replace(item, "", 1)
replace_all("Purpose : Just for fun.", "Purpose: Just for fun.", "Discipline purpose punctuation")
replace_once("Mental &amp; Emotion", "Mental &amp; Emotional State", "Discipline English heading")

# 4. Chinese punctuation and site-wide terminology consistency.
replace_once('"作者:"', '"作者："', "Chinese author colon")
replace_once('"總字數:"', '"總字數："', "Chinese word-count colon")
text = text.replace("記錄", "紀錄")

# 6. Survival Skills: Location & Time as survival orientation/time, not lost-person doctrine.
location_block = '''      location:{num:"01.4",titleEn:"Location & Time",titleZh:"位置與時間",introEn:"Understand your position relative to terrain, direction, and remaining usable time.",sections:[
        {title:"建立周遭空間基準",items:["觀察太陽位置、陰影、坡向、水流方向、稜線、谷地、海岸或其他穩定自然地標，建立對周遭地形的方向感。","辨認水源、遮蔽處、材料來源、危險區域與可通行地形彼此之間的位置關係，而不是只記住單一地點。","把確定觀察到的地形資訊與推測分開，並在移動後持續更新對周遭環境的空間模型。"]},
        {title:"評估移動的目的與回返成本",items:["移動前先確認目的：要取得什麼、解決什麼問題，以及是否有更近或代價更低的選項。","利用自然地標維持方向與路徑關係，避免移動後失去水源、庇護位置或重要材料的位置資訊。","把坡度、地表、距離、體力消耗與回程需求一起計算；到達目的地不代表仍有能力安全回到需要使用資源的位置。"]},
        {title:"把時間放進決策",items:["估計剩餘日照，並觀察天候與氣溫是否會在短時間內明顯改變。","需要移動、找材料、取水或搭建庇護的工作都會消耗日照與體力；不能把時間視為無限資源。","同一項行動在白天、黃昏、夜間或天候即將改變時可能具有完全不同的成本與風險。"]}
      ],principle:"位置資訊的價值在於支援行動、資源利用與安全回返，而不只是回答『我在哪裡』。每次移動都應知道方向、目的、成本與剩餘可用時間，並持續更新對周遭地形的空間模型。"},'''
sub_once(
    r'      location:\{num:"01\.4".*?\],principle:".*?"\},\n      resources:',
    location_block + "\n      resources:",
    "Survival Location & Time block",
    flags=re.S,
)

# Replace the rescue-oriented NPS reference with broad survival doctrine.
r2 = '<a class="survival-reference" href="https://armypubs.army.mil/epubs/DR_pubs/DR_a/pdf/web/ARN12086_ATP%203-50x21%20FINAL%20WEB%202.pdf" target="_blank" rel="noopener noreferrer"><span class="survival-reference-id">R2</span><span class="survival-reference-title">U.S. Department of the Army · ATP 3-50.21 Survival<span class="survival-reference-meta">生存心理、生存醫療、水、食物、庇護、火、工具與導航等基礎生存技能。</span></span><span class="survival-reference-arrow">↗</span></a>'
sub_once(
    r'<a class="survival-reference" href="https://www\.nps\.gov/articles/gtgemergencyplan\.htm".*?</a>',
    r2,
    "Replace rescue-oriented R2",
    flags=re.S,
)

# 7. WMS: current official entry points; do not falsely relabel hypothermia as 2026.
r4 = '<a class="survival-reference" href="https://www.wms.org/WMS/Research/WEM/Clinical-Practice-Guidelines.aspx" target="_blank" rel="noopener noreferrer"><span class="survival-reference-id">R4</span><span class="survival-reference-title">Wilderness Medical Society · Clinical Practice Guidelines<span class="survival-reference-meta">WMS 現行官方 CPG 索引，集中列出各主題的現行與歷年更新指引。</span></span><span class="survival-reference-arrow">↗</span></a>'
sub_once(
    r'<a class="survival-reference" href="https://www\.wms\.org/WMS/Research/WEM/Clinical-Practice-Guidelines\.aspx".*?</a>',
    r4,
    "Update WMS R4",
    flags=re.S,
)
r5 = '<a class="survival-reference" href="https://wms.org/magazine/Core-Columns/WMS%20CPG%20Summaries.aspx" target="_blank" rel="noopener noreferrer"><span class="survival-reference-id">R5</span><span class="survival-reference-title">Wilderness Medical Society · Accidental Hypothermia<span class="survival-reference-meta">WMS 現行 CPG 摘要入口收錄失溫評估與處置；官方 CPG 索引目前仍將 Hypothermia 列為 2019 guideline。</span></span><span class="survival-reference-arrow">↗</span></a>'
sub_once(
    r'<a class="survival-reference" href="https://wms\.org/magazine/magazine/1260/2020hypothermia-CPG/default\.aspx".*?</a>',
    r5,
    "Update WMS R5",
    flags=re.S,
)

# 8. Priority Assessment: all five assessment inputs can change.
replace_once(
    "優先順序不是一次決定後永遠不變。環境、身體、位置與資源都會改變，因此完成重要行動或情況明顯變化後，要重新跑一次評估。",
    "優先順序不是一次決定後永遠不變。立即危險、環境、身體、位置與資源都會改變，因此完成重要行動或情況明顯變化後，要重新跑一次評估。",
    "Priority reassessment inputs",
)

# 9. Survival English precision.
replace_once(
    "Identify hazards that can cause serious harm before slower survival problems matter.",
    "Identify hazards that can cause serious harm before slower-developing survival problems become critical.",
    "Immediate Threats English intro",
)
replace_once(
    "Look for useful water, terrain, shelter, and natural materials around you.",
    "Identify usable water sources, terrain features, natural shelter, and materials around you.",
    "Available Resources English intro",
)

# 10a. Accessibility: remove heading elements nested in buttons without changing visual hierarchy.
text = text.replace(".card-copy h2{margin:0;", ".card-copy .card-title{display:block;margin:0;")
text = text.replace(".category h2{margin:0;", ".category .category-title{display:block;margin:0;")
text = text.replace(".category.available h2{", ".category.available .category-title{")
text = text.replace(".category:hover h2,.category:focus-visible h2{", ".category:hover .category-title,.category:focus-visible .category-title{")
text = text.replace(".fiction-title h2{margin:0;", ".fiction-title .fiction-work-title{display:block;margin:0;")
text = text.replace(".project-work-heading h2{margin:0;", ".project-work-heading .project-work-title{display:block;margin:0;")
replace_once('<span class="card-copy"><h2>Ability</h2>', '<span class="card-copy"><span class="card-title">Ability</span>', "Portal Ability heading")
replace_once('<span class="card-copy"><h2>About me</h2>', '<span class="card-copy"><span class="card-title">About me</span>', "Portal About heading")
text, category_count = re.subn(
    r'(<button class="category[^"]*"[^>]*>)<h2>([^<]+)</h2>',
    r'\1<span class="category-title">\2</span>',
    text,
)
if category_count != 10:
    raise SystemExit(f"Category button headings: expected 10 replacements, found {category_count}")
text, fiction_count = re.subn(
    r'<span class="fiction-title"><h2>([^<]+)</h2>',
    r'<span class="fiction-title"><span class="fiction-work-title">\1</span>',
    text,
)
if fiction_count != 3:
    raise SystemExit(f"Fiction button headings: expected 3 replacements, found {fiction_count}")
replace_once(
    'heading.appendChild(makeText("h2","",project.name));',
    'heading.appendChild(makeText("span","project-work-title",project.name));',
    "Generated project heading",
)
replace_once(
    'const title=makeText("h2","cognition-card-title",theme.title);',
    'const title=makeText("span","cognition-card-title",theme.title);',
    "Generated cognition heading",
)

# 10b. Accessibility: muted-dark now clears 4.5:1 against #14101a.
replace_once("--muted-dark:#6b6058;", "--muted-dark:#887b73;", "muted-dark contrast")

# 11. Language metadata: English remains document default; Chinese-dominant direct text is tagged zh-Hant.
old_runtime = 'function currentHash(){return window.location.hash||"#home"}function activateView(id){views.forEach(viewId=>document.getElementById(viewId).classList.toggle("active",viewId===id));window.scrollTo({top:0,behavior:"auto"})}function setHash(hash){if(currentHash()!==hash)history.pushState({route:hash,from:currentHash()},"",hash)}function makeText(tag,className,text){const element=document.createElement(tag);if(className)element.className=className;element.textContent=text;return element}'
new_runtime = 'function currentHash(){return window.location.hash||"#home"}function inferredTextLang(value){const text=String(value??"");const cjk=(text.match(/[\\u3400-\\u9fff]/g)||[]).length;const latin=(text.match(/[A-Za-z]/g)||[]).length;return cjk>latin?"zh-Hant":""}function applyLanguageTags(root){if(!root)return;root.querySelectorAll("*").forEach(element=>{const direct=[...element.childNodes].filter(node=>node.nodeType===3).map(node=>node.nodeValue||"").join("").trim();const lang=inferredTextLang(direct);if(lang)element.lang=lang})}function activateView(id){views.forEach(viewId=>document.getElementById(viewId).classList.toggle("active",viewId===id));queueMicrotask(()=>applyLanguageTags(document.getElementById(id)));window.scrollTo({top:0,behavior:"auto"})}function setHash(hash){if(currentHash()!==hash)history.pushState({route:hash,from:currentHash()},"",hash)}function makeText(tag,className,text){const element=document.createElement(tag);if(className)element.className=className;element.textContent=text;const lang=inferredTextLang(text);if(lang)element.lang=lang;return element}'
replace_once(old_runtime, new_runtime, "Language metadata runtime")
replace_once(
    '<p id="projectDescription" class="project-description">Project description</p>',
    '<p id="projectDescriptionEn" class="project-description">Project description</p><p id="projectDescriptionZh" class="project-description" lang="zh-Hant"></p>',
    "Project detail bilingual description structure",
)

# 12. Remove AI involvement labels while preserving the two-column category layout.
replace_once(
    '<section class="ability-group" aria-labelledby="independentWorkTitle"><h2 id="independentWorkTitle" class="ability-group-title">0% AI Involvement</h2><div class="category-grid">',
    '<section class="ability-group"><div class="category-grid">',
    "Remove 0% AI label",
)
replace_once(
    '<section class="ability-group" aria-labelledby="aiAssistedTitle"><h2 id="aiAssistedTitle" class="ability-group-title">AI-Assisted</h2><div class="category-grid">',
    '<section class="ability-group"><div class="category-grid">',
    "Remove AI-Assisted label",
)

# 14. Project detail consistency.
replace_once(
    ".info-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));",
    ".info-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));",
    "Project info grid",
)
replace_once(
    'onclick="backToCategory()">← Category</button></nav><main class="detail-wrap project-detail">',
    'id="projectBackLink" onclick="backToCategory()">← Category</button></nav><main class="detail-wrap project-detail">',
    "Project back link id",
)
replace_once(
    '<div class="info-grid"><section class="info-card"><h3>Status</h3><p id="projectStatus">In Development</p></section><section class="info-card"><h3>Technologies</h3><p id="projectTechnology">—</p></section></div>',
    '<div class="info-grid"><section class="info-card"><h3>Status</h3><p id="projectStatus">In Development</p></section><section class="info-card"><h3>Start</h3><p id="projectStart">—</p></section><section class="info-card"><h3>Technologies</h3><p id="projectTechnology">—</p></section></div>',
    "Project Start card",
)
replace_once(
    '</a></main></div></div>\n  <script>',
    '</a></main><footer>© 2026 KeeCharlotte</footer></div></div>\n  <script>',
    "Project detail footer",
)
old_render_project = 'function renderProject(project){activateView("projectPage");document.getElementById("projectTitle").textContent=project.name;document.getElementById("projectDescription").textContent=[project.descriptionEn,project.descriptionZh].filter(Boolean).join("\\n");document.getElementById("projectDescription").style.whiteSpace="pre-line";document.getElementById("projectStatus").textContent=project.status;document.getElementById("projectTechnology").textContent=project.technology;document.getElementById("githubLink").href=project.github;document.title=project.name+" — KeeCharlotte"}'
new_render_project = 'function renderProject(project){activateView("projectPage");document.getElementById("projectTitle").textContent=project.name;document.getElementById("projectDescriptionEn").textContent=project.descriptionEn||"";document.getElementById("projectDescriptionZh").textContent=project.descriptionZh||"";document.getElementById("projectStatus").textContent=project.status;document.getElementById("projectStart").textContent=project.start||"—";document.getElementById("projectTechnology").textContent=project.technology;document.getElementById("projectBackLink").textContent="← "+currentCategory;document.getElementById("githubLink").href=project.github;document.title=project.name+" — KeeCharlotte"}'
replace_once(old_render_project, new_render_project, "Project detail render")

# Add missing Discipline detail footer too.
sub_once(
    r'(<div id="disciplinePeriodPage".*?</main>)(</div></div>\n\n  <div id="cognitionPage")',
    r'\1<footer>© 2026 KeeCharlotte</footer>\2',
    "Discipline detail footer",
    flags=re.S,
)

# 15. Discipline routing bug: slug is now an actual slug parameter.
old_discipline_fn = 'function openDisciplinePeriod(push=true){currentCategory="Discipline";activateView("disciplinePeriodPage");if(push)setHash("#ability/Discipline/2022-08-2022-11");document.title="High School · Second Year — KeeCharlotte"}'
new_discipline_fn = 'function openDisciplinePeriod(slug="2022-08-2022-11",push=true){if(slug!=="2022-08-2022-11"){showDiscipline(push);return}currentCategory="Discipline";activateView("disciplinePeriodPage");if(push)setHash("#ability/Discipline/2022-08-2022-11");document.title="High School · Second Year — KeeCharlotte"}'
replace_once(old_discipline_fn, new_discipline_fn, "Discipline period function")
replace_once(
    'if(parts[2]==="2022-08-2022-11")openDisciplinePeriod(false);',
    'if(parts[2]==="2022-08-2022-11")openDisciplinePeriod("2022-08-2022-11",false);',
    "Discipline route call",
)

path.write_text(text, encoding="utf-8")

# Post-write structural/content validation.
checks = {
    "games sentence case": "A civilization-building game based on real-world rules." in text,
    "games Chinese punctuation": "基於真實世界規則的文明建立遊戲。" in text,
    "fiction period": '"interference-of-fate-and-time":{title:"時空干涉",subtitle:"Interference of Fate and Time",period:"Jun 2022"}' in text,
    "routine English removed": all(item.split(">", 1)[1].split("<", 1)[0] not in text for item in routine_english),
    "Chinese terminology unified": "記錄" not in text,
    "Chinese colons": '"作者："' in text and '"總字數："' in text,
    "no rescue NPS reference": "gtgemergencyplan" not in text,
    "survival doctrine R2": "ATP 3-50.21 Survival" in text,
    "WMS current summaries": "Core-Columns/WMS%20CPG%20Summaries.aspx" in text,
    "old hypothermia page removed": "2020hypothermia-CPG" not in text,
    "priority includes immediate threats": "立即危險、環境、身體、位置與資源都會改變" in text,
    "survival English improved": "slower-developing survival problems become critical" in text and "Identify usable water sources" in text,
    "contrast fixed": "--muted-dark:#887b73;" in text,
    "language tagging runtime": "function applyLanguageTags(root)" in text and "zh-Hant" in text,
    "AI labels removed": "0% AI Involvement" not in text and "AI-Assisted" not in text,
    "project Start detail": 'id="projectStart"' in text,
    "project back label": 'id="projectBackLink"' in text,
    "discipline slug signature": 'function openDisciplinePeriod(slug="2022-08-2022-11",push=true)' in text,
}
failed = [name for name, ok in checks.items() if not ok]
if failed:
    raise SystemExit("Failed checks: " + ", ".join(failed))

for button_body in re.findall(r"<button\b[^>]*>(.*?)</button>", text, flags=re.S):
    if "<h2" in button_body:
        raise SystemExit("Accessibility check failed: heading remains inside a button")

scripts = re.findall(r"<script>(.*?)</script>", text, flags=re.S)
if len(scripts) != 1:
    raise SystemExit(f"Expected one inline script, found {len(scripts)}")
Path("/tmp/site.js").write_text(scripts[0], encoding="utf-8")
print("All approved content and structure checks passed.")
