from pathlib import Path
import re

path = Path("index.html")
html = path.read_text(encoding="utf-8")

# 1) Add Games / Software project-row styling aligned with Fiction.
css_anchor = '.fiction-work.completed .fiction-status{color:var(--rose)}.fiction-work.completed .fiction-status::before{border-color:var(--rose);background:var(--rose)}\n'
css_addition = css_anchor + '    .project-work{grid-template-columns:minmax(260px,.9fr) minmax(360px,1.35fr) auto}.project-work-heading{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px 14px}.project-work-heading h2{margin:0;color:var(--text);font-family:var(--serif);font-size:clamp(27px,2.6vw,36px);font-weight:700;letter-spacing:-.015em}.project-work-zh{color:var(--muted);font-size:16px;font-weight:500;line-height:1.5}.project-work-description{min-width:0}.project-work-description-en,.project-work-description-zh{display:block;line-height:1.7}.project-work-description-en{color:var(--text);font-size:16px}.project-work-description-zh{margin-top:5px;color:var(--muted);font-size:14px}.project-work .fiction-status{white-space:nowrap}\n'
if '.project-work{grid-template-columns:' not in html:
    if css_anchor not in html:
        raise SystemExit('CSS anchor not found')
    html = html.replace(css_anchor, css_addition, 1)

# 2) Replace generic category page with the same header/list structure used by Fiction.
old_category = '  <div id="categoryPage" class="view subpage"><div class="shell"><nav class="topbar" aria-label="Category navigation"><button class="brand" type="button" onclick="showPortal()">KeeCharlotte</button><button class="back-link" type="button" onclick="backToAbility()">← Ability</button></nav><main class="detail-wrap"><p id="categoryEyebrow" class="eyebrow">Ability · Category</p><h1 id="categoryTitle" class="detail-title">Category</h1><div id="projectList" class="project-list"></div></main></div></div>'
new_category = '  <div id="categoryPage" class="view subpage"><div class="shell"><nav class="topbar" aria-label="Category navigation"><button class="brand" type="button" onclick="showPortal()">KeeCharlotte</button><button class="back-link" type="button" onclick="backToAbility()">← Ability</button></nav><main class="discipline-main"><section class="discipline-hero"><p id="categoryEyebrow" class="eyebrow">Ability · Category</p><h1 id="categoryTitle" class="detail-title">Category</h1><p id="categoryIntroEn" class="discipline-manifesto"></p><p id="categoryIntroZh" class="discipline-manifesto-zh"></p></section><section class="archive-section" aria-labelledby="categoryWorksTitle"><h2 id="categoryWorksTitle" class="archive-section-title">Projects</h2><div id="projectList" class="fiction-list"></div></section></main><footer>© 2026 KeeCharlotte</footer></div></div>'
if old_category in html:
    html = html.replace(old_category, new_category, 1)
elif 'id="categoryIntroEn"' not in html:
    raise SystemExit('Category page anchor not found')

# 3) Normalize project data into separate English / Chinese fields and add category intros.
projects_pattern = re.compile(r'    const projects=\{Games:\[\{name:"Civilization Rebuild".*?\}\],Software:\[\{name:"AAAS_TW".*?\}\],Achievements:\[\],Music:\[\],Art:\[\],Discipline:\[\],Fiction:\[\],"Survival Skills":\[\],"Civilizational Mastery":\[\],Cognition:\[\]\};', re.S)
projects_replacement = '''    const projects={Games:[{name:"Civilization Rebuild",nameZh:"文明重建",descriptionEn:"A Civilization-Building Game based on real-world rules",descriptionZh:"基於真實世界規則的文明建立遊戲",status:"In Development",technology:"C#, Unity",github:"https://github.com/KeeCharlotte"}],Software:[{name:"AAAS_TW",descriptionEn:"An Evidence-Driven Accounting System under development",descriptionZh:"開發中的證據導向會計系統",status:"In Development",technology:"Python, JavaScript",github:"https://github.com/KeeCharlotte"}],Achievements:[],Music:[],Art:[],Discipline:[],Fiction:[],"Survival Skills":[],"Civilizational Mastery":[],Cognition:[]};
    const categoryMeta={
      Games:{introEn:"A record of the games I am currently developing.",introZh:"這裡紀錄我目前製作的遊戲。"},
      Software:{introEn:"A record of the software I am currently developing.",introZh:"這裡紀錄我目前製作的軟體。"}
    };'''
html, count = projects_pattern.subn(projects_replacement, html, count=1)
if count != 1 and 'const categoryMeta={' not in html:
    raise SystemExit(f'Projects data replacement count: {count}')

# 4) Render Games / Software in Fiction-like rows with status at far right.
open_category_pattern = re.compile(r'    function openCategory\(category,push=true\)\{.*?\}\n    function renderProject', re.S)
open_category_replacement = '''    function openCategory(category,push=true){currentCategory=category;if(category==="Fiction"){showFiction(push);return}if(category==="Discipline"){showDiscipline(push);return}if(category==="Cognition"){showCognition(push);return}if(category==="Survival Skills"){showSurvival(push);return}activateView("categoryPage");document.getElementById("categoryEyebrow").textContent="Ability · "+category;document.getElementById("categoryTitle").textContent=category;const meta=categoryMeta[category]||{introEn:"A record of projects in this category.",introZh:"這裡紀錄此分類目前的專案。"};document.getElementById("categoryIntroEn").textContent=meta.introEn;document.getElementById("categoryIntroZh").textContent=meta.introZh;const list=document.getElementById("projectList");const categoryProjects=projects[category]||[];list.replaceChildren();if(!categoryProjects.length){const empty=document.createElement("section");empty.className="empty-card";empty.append(makeText("h3","","No projects yet"),makeText("p","","This section is currently empty. More works will be added in the future"));list.appendChild(empty)}else categoryProjects.forEach((project,index)=>{const element=document.createElement("button");element.className="fiction-work project-work"+(project.status==="Completed"?" completed":"");element.type="button";element.onclick=()=>openProject(index);const heading=document.createElement("span");heading.className="project-work-heading";heading.appendChild(makeText("h2","",project.name));if(project.nameZh)heading.appendChild(makeText("span","project-work-zh",project.nameZh));const description=document.createElement("span");description.className="project-work-description";description.append(makeText("span","project-work-description-en",project.descriptionEn||""),makeText("span","project-work-description-zh",project.descriptionZh||""));element.append(heading,description,makeText("span","fiction-status",project.status));list.appendChild(element)});if(push)setHash("#ability/"+encodeURIComponent(category));document.title=category+" — KeeCharlotte"}
    function renderProject'''
html, count = open_category_pattern.subn(open_category_replacement, html, count=1)
if count != 1:
    raise SystemExit(f'openCategory replacement count: {count}')

# 5) Keep the existing detail page functional with the new bilingual fields.
old_render = '    function renderProject(project){activateView("projectPage");document.getElementById("projectTitle").textContent=project.name;document.getElementById("projectDescription").textContent=project.description;document.getElementById("projectStatus").textContent=project.status;document.getElementById("projectTechnology").textContent=project.technology;document.getElementById("githubLink").href=project.github;document.title=project.name+" — KeeCharlotte"}'
new_render = '    function renderProject(project){activateView("projectPage");document.getElementById("projectTitle").textContent=project.name;document.getElementById("projectDescription").textContent=[project.descriptionEn,project.descriptionZh].filter(Boolean).join("\\n");document.getElementById("projectDescription").style.whiteSpace="pre-line";document.getElementById("projectStatus").textContent=project.status;document.getElementById("projectTechnology").textContent=project.technology;document.getElementById("githubLink").href=project.github;document.title=project.name+" — KeeCharlotte"}'
if old_render in html:
    html = html.replace(old_render, new_render, 1)
elif '[project.descriptionEn,project.descriptionZh]' not in html:
    raise SystemExit('renderProject anchor not found')

path.write_text(html, encoding="utf-8")
print('Updated Games and Software category layout.')
