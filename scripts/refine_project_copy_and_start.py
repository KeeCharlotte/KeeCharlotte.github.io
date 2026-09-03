from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

replacements = {
'''const projects={Games:[{name:"Civilization Rebuild",nameZh:"文明重建",descriptionEn:"A Civilization-Building Game based on real-world rules",descriptionZh:"基於真實世界規則的文明建立遊戲",status:"In Development",technology:"C#, Unity",github:"https://github.com/KeeCharlotte"}],Software:[{name:"AAAS_TW",descriptionEn:"An Evidence-Driven Accounting System under development",descriptionZh:"開發中的證據導向會計系統",status:"In Development",technology:"Python, JavaScript",github:"https://github.com/KeeCharlotte"}],Achievements:[],Music:[],Art:[],Discipline:[],Fiction:[],"Survival Skills":[],"Civilizational Mastery":[],Cognition:[]};''':
'''const projects={Games:[{name:"Civilization Rebuild",nameZh:"文明重建",descriptionEn:"A Civilization-Building Game based on real-world rules",descriptionZh:"基於真實世界規則的文明建立遊戲",start:"Jul 2026",status:"In Development",technology:"C#, Unity",github:"https://github.com/KeeCharlotte"}],Software:[{name:"AAAS_TW",descriptionEn:"A financial control system prototype built around traceable decisions and verifiable evidence.",descriptionZh:"以可追溯決策與可驗證證據為核心的財務控制系統原型。",start:"Feb 2026",status:"In Development",technology:"Python, JavaScript",github:"https://github.com/KeeCharlotte"}],Achievements:[],Music:[],Art:[],Discipline:[],Fiction:[],"Survival Skills":[],"Civilizational Mastery":[],Cognition:[]};''',
'''Software:{introEn:"A record of the software I am currently developing.",introZh:"這裡紀錄我目前製作的軟體。"}''':
'''Software:{introEn:"A record of the software systems I am building and refining.",introZh:"這裡紀錄我目前開發與持續改進的軟體系統。"}''',
'''.project-work{grid-template-columns:minmax(260px,.9fr) minmax(360px,1.35fr) auto}.project-work-heading''':
'''.project-work{grid-template-columns:minmax(230px,.85fr) minmax(300px,1.2fr) minmax(92px,.32fr) auto}.project-work-heading''',
'''.project-work-description-en{color:var(--text);font-size:16px}.project-work-description-zh{margin-top:5px;color:var(--muted);font-size:14px}.project-work .fiction-status{white-space:nowrap}''':
'''.project-work-description-en{color:var(--text);font-size:16px}.project-work-description-zh{margin-top:5px;color:var(--muted);font-size:14px}.project-work-start{min-width:0}.project-work-start .fiction-meta-label{margin-bottom:5px}.project-work .fiction-status{white-space:nowrap}''',
'''const description=document.createElement("span");description.className="project-work-description";description.append(makeText("span","project-work-description-en",project.descriptionEn||""),makeText("span","project-work-description-zh",project.descriptionZh||""));element.append(heading,description,makeText("span","fiction-status",project.status));''':
'''const description=document.createElement("span");description.className="project-work-description";description.append(makeText("span","project-work-description-en",project.descriptionEn||""),makeText("span","project-work-description-zh",project.descriptionZh||""));const start=document.createElement("span");start.className="project-work-start";start.append(makeText("span","fiction-meta-label","Start"),makeText("span","fiction-meta-value",project.start||"—"));element.append(heading,description,start,makeText("span","fiction-status",project.status));'''
}

for old, new in replacements.items():
    if old not in html:
        raise SystemExit(f'Expected source fragment not found:\n{old[:180]}')
    html = html.replace(old, new, 1)

path.write_text(html, encoding='utf-8')
print('Updated Software copy and project start dates.')
