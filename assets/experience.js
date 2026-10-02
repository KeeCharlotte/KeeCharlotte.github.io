/* A small navigation layer over the existing renderers. No framework or
   content fetch is required. Existing hashes remain valid. */
(() => {
  'use strict';
  // Life-portfolio introductions record purpose, choices and experience.
  // Implementation status and versioned evidence belong in the linked project repositories.
  Object.assign(projects.Software[0], {
    "name": "LedgerTrail",
    "engineeringName": "AAAS-TW / AAAS",
    "summaryEn": "Exploring the evidence, judgment, and responsibility behind accounting decisions.",
    "summaryZh": "從會計問題出發，探索數字背後的來源、判斷與責任。",
    "descriptionEn": "An accounting systems project about making financial decisions understandable and traceable.",
    "descriptionZh": "帳跡是我從會計背景出發的資訊系統專案。我關心的不只是如何產生分錄，而是人如何理解數字的依據、檢查處理過程，並在出錯時保留可追溯的更正。",
    "status": "Accounting systems project",
    "start": "Feb 2026",
    "technology": "Python / Flask · PostgreSQL · HTML / CSS / JavaScript · Docker",
    "technologyGroups": [
      {
        "label": "Backend",
        "value": "Python · Flask"
      },
      {
        "label": "Database",
        "value": "PostgreSQL"
      },
      {
        "label": "Frontend",
        "value": "HTML · CSS · JavaScript"
      },
      {
        "label": "Environment",
        "value": "Docker"
      }
    ],
    "overview": {
      "scope": {
        "heading": "Why this project · 專案緣起",
        "items": [
          {
            "title": "數字之外，還需要看見依據",
            "text": "一筆帳務的意義不只在金額，也在原始資料、處理理由與責任分工。我把這些關係當成系統設計的起點，而不是等到查帳時才補上說明。"
          },
          {
            "title": "把會計問題轉成系統問題",
            "text": "我以會計師／記帳士與中小企業的工作情境為背景，思考哪些工作可以交給系統協助，哪些判斷仍需要人負責。"
          }
        ]
      },
      "workflowTitle": "A design lens · 如何看待會計流程",
      "workflowIntro": "我用以下問題整理流程與控制需求；它們是設計思路，不是功能完成清單。",
      "workflow": [
        {
          "title": "來源：這個數字從哪裡來？",
          "text": "先保留原件與使用脈絡，再談自動化；資料被帶入，不代表內容已經正確。"
        },
        {
          "title": "判斷：為什麼這樣處理？",
          "text": "把輸入事實、政策與專業判斷分開，讓建議有依據，也容許被質疑與退回。"
        },
        {
          "title": "責任：誰可以決定與執行？",
          "text": "區分準備、覆核與核准的責任，不把看得到資料當成有權改帳。"
        },
        {
          "title": "更正：出錯之後怎麼交代？",
          "text": "保留原來發生的事與後續修改，使新結果能被理解，而不是把舊錯誤直接抹去。"
        }
      ],
      "cases": {
        "heading": "Design choices · 代表性取捨",
        "items": [
          {
            "title": "自動化與專業判斷分工",
            "text": "我選擇讓 AI 協助整理與提出建議，而不是把生成結果視為會計結論。效率必須和可檢查、可退回及責任分工一起考慮。"
          },
          {
            "title": "保留錯誤，而不是只留下成功",
            "text": "面對被拒絕或出錯的案例，我要求先辨認原因、保存前後脈絡，再決定修改哪一層；不以放寬規則讓畫面看起來順利。"
          }
        ]
      },
      "progress": {
        "heading": "What I learned · 留下的思考",
        "items": [
          {
            "title": "單一步驟正確，不代表整個流程成立",
            "text": "來源、權限、覆核、更正與期間會互相影響。這個專案讓我把注意力從單一功能，移到規則之間的關係。"
          },
          {
            "title": "證據需要說明它能證明什麼",
            "text": "借貸平衡、資料完整與測試成功，各自回答不同問題；它們不能單獨證明交易真實、判斷適切或實際使用成效。"
          }
        ]
      },
      "example": {
        "heading": "A project experience · 一段開發經驗",
        "title": "測試之外，親自操作仍會提出新問題",
        "text": "一次合成資料的人工操作中，我選用了與發票內容不一致的認列證據，流程仍接受核准與過帳。我提出這個反例，再由 AI 協助唯讀核對與保存結果。這讓我更重視：按下核准與留下紀錄，不等於內容已被正確理解。",
        "note": "這是對一次開發經驗的回顧，不是對後續版本的缺陷狀態或完整系統正確性作判定。"
      },
      "role": [
        "我負責從會計問題界定需求、選擇範圍與取捨、提出驗收要求，並透過操作與結果核對檢查自己的假設。需求調整與錯誤案例，也是我在專案中的工作成果。",
        "我使用 AI 協助程式實作、研究整理、測試與文件；個人判斷、親自操作和 AI 執行的工作分開記錄，不把整套程式或全部驗證歸為我獨力完成。"
      ],
      "more": "這裡記錄專案的問題意識、設計取捨與個人經驗；實作、測試及適用限制由公開作品集承接，不以本頁介紹判定可部署或正式使用。"
    },
    "github": "https://github.com/KeeCharlotte/LedgerTrail-Portfolio",
    "sourceLabel": "Explore the project · 深入了解專案"
  });
  Object.assign(projects.Games[0], {
    "name": "Civilization Rebuilt",
    "summaryEn": "A first-person game project about rebuilding civilization through observation and experimentation.",
    "summaryZh": "從自然材料出發，透過觀察、試驗與推理，探索文明如何被建立。",
    "descriptionEn": "A game project about the gap between knowing how civilization works and making it work with your own hands.",
    "descriptionZh": "文明重建源於一個問題：離開現代便利之後，知道文明如何運作的人，真的能從自然材料重新做出來嗎？我希望玩家透過觀察、嘗試與修正，理解工具與生活能力如何逐步形成。",
    "start": "May 2026",
    "status": "First-person game project",
    "technology": "Unity · C# · URP · Blender",
    "technologyGroups": [
      {
        "label": "Game Engine",
        "value": "Unity"
      },
      {
        "label": "Programming",
        "value": "C#"
      },
      {
        "label": "Rendering",
        "value": "Universal Render Pipeline (URP)"
      },
      {
        "label": "3D Assets",
        "value": "Blender"
      }
    ],
    "overview": {
      "focusTitle": "Design philosophy · 核心理念",
      "highlights": [
        {
          "title": "讓玩家創造文明，而不只是使用文明",
          "text": "我把材料、環境與身體能力視為問題的條件；設計重點不是背熟配方，而是讓玩家理解某種做法為什麼成立。"
        },
        {
          "title": "簡化操作，不代替判斷",
          "text": "拿什麼、放哪裡、如何安排仍由玩家決定。角色可以協調日常動作，但操作上的協助不應替玩家完成材料與位置的取捨。"
        },
        {
          "title": "從偶然成功，走向可靠能力",
          "text": "一次做成不等於真正掌握。我關心玩家如何比較結果、修正假設，再把方法變成能重複使用的能力。"
        }
      ],
      "progress": {
        "heading": "A design lesson · 一次設計反思",
        "items": [
          {
            "title": "困難不一定等於深度",
            "text": "試玩時，拿取不順與持物抖動讓我重新區分兩種困難：一種來自材料與環境，一種只是操作沒有可靠回應。前者可以是玩法，後者需要被檢查，不能用「自由度」替它辯護。"
          }
        ]
      },
      "example": {
        "heading": "Design scenario · 設計情境",
        "title": "第一次面對寒冷",
        "text": "玩家需要決定先登高觀察地勢，還是搬運材料、安排停留的位置。探索可能增加資訊，也會消耗準備時間；眼前方便的位置，也未必適合休息。我想保留的是這種條件與代價之間的比較，而不是只有一條正確路線。",
        "note": "這個情境說明遊戲想呈現的選擇，不是固定攻略，也不代表列出的體驗已全面實作或驗收。"
      },
      "role": [
        "我負責遊戲方向、世界與玩法取捨，從研究和實際操作中提出問題，再決定哪些差異值得成為玩家需要理解的條件。",
        "AI 協助研究整理、程式實作、素材製作工具與文件。我把方向決策、人工感受與自動檢查分開看待；程式能執行，不等於遊戲已讓人理解或願意繼續探索。"
      ],
      "more": "這裡保留創作動機、設計理念與個人反思；研究、製作紀錄與實作範圍集中於公開作品集，並與設計目標分開說明。"
    },
    "github": "https://github.com/KeeCharlotte/Civilization-Rebuilt-Portfolio",
    "sourceLabel": "Explore the project · 深入了解專案"
  });
  const detailViews = new Set(['fictionDetailPage', 'disciplinePeriodPage',
    'cognitionDetailPage', 'survivalDetailPage', 'projectPage']);
  const own = (object, key) => Object.prototype.hasOwnProperty.call(object, key);
  const byId = id => document.getElementById(id);
  const el = (tag, className, text) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  };
  const memory = new Map();
  const lastVisit = new Map();
  let entry = null;
  let renderedHash = '';
  let generation = 0;
  let inputVersion = 0;
  let busy = false;
  let chapterHeadings = [];
  let scrollFrame = 0;
  let saveTimer = 0;

  // Parse defensively before the legacy router decodes any user-supplied hash.
  function describe(hash = location.hash) {
    const [path, query = ''] = String(hash || '#home').replace(/^#/, '').split('?');
    let parts;
    try { parts = path.split('/').map(decodeURIComponent); }
    catch { parts = ['home']; }
    const trail = [{ route: '#home', label: 'Home' }];
    let route = '#home';
    let category = '';
    if (parts[0] === 'about') {
      route = '#about'; trail.push({ route, label: 'About me' });
    } else if (parts[0] === 'ability') {
      route = '#ability'; trail.push({ route, label: 'Ability' });
      if (parts[1] && own(projects, parts[1])) {
        category = parts[1];
        route += '/' + encodeURIComponent(category);
        trail.push({ route, label: category });
        const slug = parts[2];
        let label = '';
        if (category === 'Fiction' && slug && own(fictionWorks, slug)) label = fictionWorks[slug].title;
        else if (category === 'Cognition' && slug && own(cognitionThemes, slug)) label = cognitionThemes[slug].title;
        else if (category === 'Discipline' && slug === '2022-08-2022-11') label = 'High School · Second Year';
        else if (category === 'Survival Skills' && slug === 'situation-assessment') label = 'Situation Assessment';
        else if (!['Fiction', 'Cognition', 'Discipline', 'Survival Skills'].includes(category)
          && /^\d+$/.test(slug || '') && projects[category][Number(slug)]) label = projects[category][Number(slug)].name;
        if (label) {
          route += '/' + encodeURIComponent(slug);
          trail.push({ route, label });
          if (category === 'Survival Skills' && parts[3] && own(survivalAssessmentNodes, parts[3])) {
            route += '/' + encodeURIComponent(parts[3]);
            trail.push({ route, label: survivalAssessmentNodes[parts[3]].titleEn });
          }
        }
      }
    }
    const candidate = new URLSearchParams(query).get('section') || '';
    const section = /^[A-Za-z0-9_-]+$/.test(candidate) ? candidate : '';
    return { route, category, trail, section,
      hash: route + (section ? '?section=' + encodeURIComponent(section) : ''),
      parent: trail.length > 1 ? trail[trail.length - 2] : null };
  }

  function makeEntry(route, from = null, saved = null) {
    return { id: globalThis.crypto?.randomUUID?.() || Date.now() + '-' + Math.random().toString(36).slice(2),
      route, from, x: saved?.x || 0, y: saved?.y || 0, focusId: saved?.focusId || '' };
  }
  function writeState(hash = location.hash || '#home') {
    history.replaceState({ ...history.state, portfolio: entry }, '', hash);
  }
  function remember(write = true, focus = document.activeElement) {
    if (!entry) return;
    const view = document.querySelector('.view.active');
    entry = { ...entry, x: window.scrollX, y: window.scrollY,
      focusId: view?.contains(focus) && focus.id ? focus.id : entry.focusId };
    memory.set(entry.id, { ...entry });
    lastVisit.set(entry.route, { ...entry });
    if (write && history.state?.portfolio?.id === entry.id && describe().route === entry.route) writeState();
  }
  function routeLink(label, route, className = '', up = false) {
    const a = el('a', className, label);
    a.href = route; a.dataset.route = route;
    if (up) a.dataset.up = 'true';
    return a;
  }
  function toLink(button, route, up = false) {
    const a = routeLink(undefined, route, button.className, up);
    for (const attribute of button.attributes) {
      if (!['class', 'onclick', 'type'].includes(attribute.name)) a.setAttribute(attribute.name, attribute.value);
    }
    a.append(...button.childNodes);
    button.replaceWith(a);
    return a;
  }
  function arrow(node) {
    const dot = node.querySelector(':scope > .portal-dot, :scope > .category-dot');
    if (dot) dot.remove();
    if (!node.querySelector(':scope > .entry-arrow, :scope > .cognition-card-arrow, :scope > .survival-major-arrow, :scope > .period-arrow')) {
      const mark = el('span', 'entry-arrow', '→');
      mark.setAttribute('aria-hidden', 'true'); node.append(mark);
    }
  }
  function flattenDirectory() {
    const main = byId('abilityPage').querySelector('main');
    const columns = [...main.querySelectorAll('.category-grid')].map(column => [...column.children]);
    if (!columns.length) return;
    const ordered = [];
    for (let row = 0; row < Math.max(...columns.map(column => column.length)); row++) {
      columns.forEach(column => { if (column[row]) ordered.push(column[row]); });
    }
    main.replaceChildren(...ordered); // Preserve the old desktop row order on every device.
  }
  function addProjectAlias(title, project, includeChinese = false) {
    const text = project?.engineeringName || (includeChinese ? project?.nameZh : '');
    if (!title || !text || title.querySelector('[data-project-alias]')) return;
    const alias = el('span', 'project-work-zh', text);
    alias.dataset.projectAlias = 'true';
    // Reuse the original secondary-label style; only place this label on its own line.
    alias.style.display = 'block';
    alias.style.marginTop = '6px';
    alias.style.fontFamily = 'var(--sans)';
    title.append(document.createTextNode(' '), alias);
  }
  // Long-lived introductions share the existing project layout and section anchors.
  function renderProjectOverview(view, project) {
    const grid = byId('projectStatus').closest('.info-grid');
    const technology = byId('projectTechnology').closest('.info-card');
    const title = byId('projectTitle');
    if (!view.querySelector('.project-intro')) {
      const eyebrow = title.previousElementSibling;
      const header = el('header', 'project-intro');
      eyebrow.before(header);
      header.append(eyebrow, title, byId('projectDescriptionEn'), byId('projectDescriptionZh'));
    }
    let overview = byId('projectOverview');
    if (!overview) {
      overview = el('div', 'project-overview'); overview.id = 'projectOverview';
      grid.insertBefore(overview, technology);
    }
    let more = byId('projectReadMore');
    if (!more) {
      more = el('p', 'project-read-more'); more.id = 'projectReadMore'; more.lang = 'zh-Hant';
      byId('githubLink').before(more);
    }
    const detail = project?.overview;
    // Rebuild only this shared detail region so project switches cannot retain another project's copy.
    overview.replaceChildren();
    overview.hidden = !detail; more.hidden = !detail;
    more.textContent = detail?.more || '';
    byId('githubLink').classList.toggle('has-project-context', Boolean(detail));
    if (!detail) return;
    const paragraph = text => {
      const p = el('p', 'project-section-copy', text); p.lang = 'zh-Hant'; return p;
    };
    const section = (id, heading) => {
      const node = el('section', 'project-section');
      const h = el('h2', 'project-section-title', heading); h.id = id;
      h.dataset.tocLabel = heading.split(' · ').at(-1);
      node.setAttribute('aria-labelledby', id); node.append(h); overview.append(node);
      return node;
    };
    // Optional, text-only sections share existing styles and chapter navigation.
    const reference = (parent, link) => {
      if (!link) return;
      const a = el('a', 'github-button has-project-context', link.label + ' ↗');
      a.href = link.url; a.target = '_blank'; a.rel = 'noopener noreferrer';
      a.lang = 'zh-Hant'; parent.append(a);
    };
    const group = (id, data) => {
      if (!data?.items?.length) return;
      const node = section(id, data.heading);
      const rows = el('div', 'project-highlights');
      data.items.forEach(item => {
        const row = el('div', 'project-highlight'); row.lang = 'zh-Hant';
        row.append(el('h3', 'project-item-title', item.title), paragraph(item.text));
        rows.append(row);
      });
      node.append(rows);
      if (data.note) {
        const note = el('p', 'project-example-note', data.note); note.lang = 'zh-Hant';
        node.append(note);
      }
      reference(node, data.link);
    };
    group('project-scope', detail.scope);
    if (detail.highlights?.length) {
      const focus = section('project-focus', detail.focusTitle);
      const highlights = el('div', 'project-highlights');
      detail.highlights.forEach(item => {
        const row = el('div', 'project-highlight'); row.lang = 'zh-Hant';
        row.append(el('h3', 'project-item-title', item.title), paragraph(item.text));
        highlights.append(row);
      });
      focus.append(highlights);
    }
    if (detail.workflow?.length) {
      const flow = section('project-workflow', detail.workflowTitle || 'Workflow · 流程概覽');
      const detailed = Boolean(detail.workflowIntro);
      if (detailed) {
        flow.classList.add('project-controlled-workflow');
        const intro = paragraph(detail.workflowIntro); intro.classList.add('project-workflow-intro');
        flow.append(intro);
        // Keep earlier links to the merged highlights section working.
        if (!detail.highlights?.length) {
          flow.id = 'project-focus'; flow.dataset.chapter = 'true'; flow.tabIndex = -1;
        }
      }
      const steps = el('ol', 'project-workflow'); steps.lang = 'zh-Hant';
      steps.classList.toggle('project-workflow-detailed', detailed);
      steps.setAttribute('role', 'list');
      detail.workflow.forEach((item, index) => {
        const step = el('li');
        const copy = detailed ? el('div', 'project-workflow-copy') : step;
        if (detailed) {
          const number = el('span', 'project-step-number', String(index + 1).padStart(2, '0'));
          number.setAttribute('aria-hidden', 'true'); step.append(number, copy);
        }
        copy.append(el('h3', 'project-item-title', item.title), paragraph(item.text));
        if (item.control) {
          const control = el('p', 'project-workflow-control');
          control.append(el('strong', '', item.control)); copy.append(control);
        }
        if (item.branch) {
          const branch = el('p', 'project-workflow-branch');
          branch.append(el('strong', '', item.branch.label + '：'), document.createTextNode(item.branch.text));
          copy.append(branch);
        }
        steps.append(step);
      });
      flow.append(steps);
      if (detail.workflowControls?.length) {
        const controls = el('div', 'project-workflow-controls'); controls.lang = 'zh-Hant';
        controls.append(el('h3', 'project-item-title', '貫穿整個流程的控制'));
        const list = el('ul', 'project-control-list'); list.setAttribute('role', 'list');
        detail.workflowControls.forEach(text => list.append(el('li', '', text)));
        controls.append(list); flow.append(controls);
      }
      if (detail.workflowNote) {
        const note = el('p', 'project-example-note', detail.workflowNote); note.lang = 'zh-Hant';
        flow.append(note);
      }
    }
    group('project-cases', detail.cases);
    group('project-progress', detail.progress);
    const example = section('project-example', detail.example.heading);
    const exampleTitle = el('h3', 'project-item-title', detail.example.title); exampleTitle.lang = 'zh-Hant';
    const note = el('p', 'project-example-note', detail.example.note); note.lang = 'zh-Hant';
    example.append(exampleTitle, paragraph(detail.example.text), note);
    reference(example, detail.example.link);
    const role = section('project-role', 'My role · 我的角色');
    detail.role.forEach(text => role.append(paragraph(text)));
    reference(role, detail.roleLink);
  }
  function renderProjectTechnologies(project) {
    const value = byId('projectTechnology');
    const card = value.closest('.info-card');
    const grid = card.closest('.info-grid');
    const groups = Array.isArray(project?.technologyGroups) ? project.technologyGroups : [];
    // The project view is shared: clear groups before showing another project.
    card.querySelector('.technology-list')?.remove();
    grid.classList.toggle('has-technology-groups', groups.length > 0);
    card.classList.toggle('technology-card', groups.length > 0);
    value.hidden = groups.length > 0;
    if (!groups.length) return;
    const list = el('dl', 'technology-list');
    groups.forEach(group => {
      const row = el('div', 'technology-row');
      row.append(el('dt', '', group.label), el('dd', '', group.value));
      list.append(row);
    });
    card.append(list);
  }
  function prepareLinks(view, info) {
    const fixed = { showPortal: '#home', showAbility: '#ability', showAbout: '#about' };
    const cognitionCards = [...view.querySelectorAll('.cognition-theme-card')];
    const projectCards = [...view.querySelectorAll('.project-work')];
    projectCards.forEach((card, index) => {
      const project = projects[info.category]?.[index];
      addProjectAlias(card.querySelector('.project-work-title'), project);
    });
    if (view.id === 'projectPage') {
      const index = Number(info.route.split('/').at(-1));
      const project = projects[info.category]?.[index];
      addProjectAlias(byId('projectTitle'), project, true);
      renderProjectOverview(view, project);
      renderProjectTechnologies(project);
      byId('githubLink').textContent = (project?.sourceLabel || 'View source code') + ' ↗';
    }
    view.querySelectorAll('button').forEach(button => {
      let route = '';
      let up = false;
      const action = button.getAttribute('onclick') || '';
      const argument = action.match(/\('([^']+)'\)/)?.[1];
      if (button.matches('.brand')) route = '#home';
      else if (button.matches('.back-link') && info.parent) { route = info.parent.route; up = true; }
      else if (button.matches('.category')) route = '#ability/' + encodeURIComponent(button.querySelector('.category-title').textContent);
      else if (button.matches('.project-work')) route = info.route + '/' + projectCards.indexOf(button);
      else if (button.matches('.fiction-work') && argument) route = '#ability/Fiction/' + argument;
      else if (button.matches('.cognition-theme-card')) route = '#ability/Cognition/' + cognitionThemeOrder[cognitionCards.indexOf(button)];
      else if (button.matches('.period-item')) route = '#ability/Discipline/2022-08-2022-11';
      else if (button.matches('.survival-major-node')) route = '#ability/Survival%20Skills/situation-assessment';
      else if (button.matches('.survival-subnode, .survival-priority-node') && argument) route = '#ability/Survival%20Skills/situation-assessment/' + argument;
      else { const name = action.match(/^(\w+)\(/)?.[1]; if (fixed[name]) route = fixed[name]; }
      if (route) toLink(button, route, up);
    });
    // A shared project view gets a new parent even after its button became a link.
    const back = view.querySelector('.topbar .back-link');
    if (back && info.parent) {
      back.href = info.parent.route; back.dataset.route = info.parent.route; back.dataset.up = 'true';
      back.textContent = '← ' + info.parent.label;
    }
    view.querySelectorAll('.fiction-work, .survival-subnode, .survival-priority-node').forEach(arrow);
    view.querySelectorAll('.project-work').forEach(card => {
      if (card.querySelector('.project-meta')) return;
      const meta = el('span', 'project-meta');
      meta.append(card.querySelector('.project-work-start'), card.querySelector('.fiction-status'));
      card.append(meta);
    });
  }
  function stampControls(view) {
    view.querySelectorAll('a, button, summary').forEach((node, index) => {
      if (!node.id) node.id = view.id + '-control-' + index;
    });
  }
  function breadcrumbs(view, info) {
    view.querySelector('.breadcrumbs')?.remove();
    if (info.trail.length < 3) return;
    const nav = el('nav', 'breadcrumbs'); nav.setAttribute('aria-label', 'Breadcrumb');
    const list = el('ol');
    info.trail.forEach((part, index) => {
      const li = el('li');
      if (index === info.trail.length - 1) {
        const label = el('span', '', part.label); label.setAttribute('aria-current', 'page'); li.append(label);
      } else li.append(routeLink(part.label, part.route, '', true));
      list.append(li);
    });
    nav.append(list); view.querySelector('.topbar').after(nav);
  }
  function tocList(info, headings) {
    const list = el('ol', 'toc-list');
    headings.forEach(heading => {
      const li = el('li');
      const a = routeLink(heading.dataset.tocLabel || heading.textContent.trim(), info.route + '?section=' + heading.id);
      a.dataset.chapterLink = heading.id;
      li.append(a); list.append(li);
    });
    return list;
  }
  function updateTocVisibility() {
    const main = document.querySelector('.view.active .reading-main');
    if (!main) return;
    const copy = main.querySelector('.reading-copy');
    const mobile = main.querySelector('.toc-mobile');
    const rail = main.querySelector('.toc-rail');
    if (!mobile || !rail) return;
    const readingHeight = copy.scrollHeight - (mobile.hidden ? 0 : mobile.offsetHeight);
    const needed = chapterHeadings.length >= 2 && readingHeight > window.innerHeight * 1.7;
    mobile.hidden = !needed; rail.hidden = !needed;
    main.classList.toggle('has-toc', needed);
  }
  function prepareReading(view, info) {
    chapterHeadings = [];
    if (!detailViews.has(view.id)) return;
    const main = view.querySelector('main');
    main.classList.add('reading-main');
    let copy = main.querySelector(':scope > .reading-copy');
    if (!copy) { copy = el('div', 'reading-copy'); copy.append(...main.childNodes); main.append(copy); }
    main.querySelectorAll('.toc-rail, .toc-mobile, .page-return').forEach(node => node.remove());
    // Keep the original empty sections, but omit them from chapter navigation.
    chapterHeadings = [...copy.querySelectorAll('h2')].filter(heading => {
      const section = heading.closest('.fiction-section');
      return !section?.querySelector('.fiction-empty, .fiction-full-link');
    });
    chapterHeadings.forEach((heading, index) => {
      if (!heading.id) heading.id = view.id + '-section-' + (index + 1);
      heading.dataset.chapter = 'true'; heading.tabIndex = -1;
    });
    if (chapterHeadings.length >= 2) {
      const rail = el('aside', 'toc-rail'); rail.setAttribute('aria-label', 'On this page');
      rail.append(el('p', 'toc-heading', 'ON THIS PAGE'), tocList(info, chapterHeadings));
      const mobile = el('details', 'toc-mobile');
      mobile.append(el('summary', '', 'On this page · 本頁章節'), tocList(info, chapterHeadings));
      const heading = copy.querySelector(':scope > header, :scope > .period-heading');
      if (heading) heading.after(mobile); else copy.prepend(mobile);
      main.append(rail);
    }
    if (info.parent) {
      const bottom = el('nav', 'page-return'); bottom.setAttribute('aria-label', 'Return to collection');
      bottom.append(routeLink('← Back to ' + info.parent.label, info.parent.route, '', true)); copy.append(bottom);
    }
    updateTocVisibility();
  }
  function decorate(info) {
    const view = document.querySelector('.view.active');
    prepareLinks(view, info); breadcrumbs(view, info); prepareReading(view, info);
    const main = view.querySelector('main');
    if (!main.id) main.id = view.id + '-main';
    main.tabIndex = -1;
    const title = view.querySelector('h1');
    if (!title.id) title.id = view.id + '-title';
    title.tabIndex = -1;
    main.setAttribute('aria-labelledby', title.id);
    if (!view.querySelector('.skip-link')) {
      const skip = el('a', 'skip-link', 'Skip to content · 跳至內容');
      skip.href = info.route; skip.dataset.skip = 'true'; view.prepend(skip);
    }
    stampControls(view); applyLanguageTags(view);
    return { view, title };
  }
  function updateChapterPosition() {
    if (!chapterHeadings.length) return;
    const bar = document.querySelector('.view.active .topbar');
    const limit = (bar?.getBoundingClientRect().height || 64) + 40;
    let current = chapterHeadings[0];
    for (const heading of chapterHeadings) { if (heading.getBoundingClientRect().top <= limit) current = heading; }
    if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 4) current = chapterHeadings.at(-1);
    document.querySelectorAll('.view.active [data-chapter-link]').forEach(link => {
      if (link.dataset.chapterLink === current.id) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  }
  function moveToSection(id, smooth = false) {
    const target = byId(id);
    if (!target?.closest('.view.active') || !target.hasAttribute('data-chapter')) return false;
    document.querySelector('.view.active .toc-mobile')?.removeAttribute('open');
    const bar = document.querySelector('.view.active .topbar');
    const y = Math.max(0, window.scrollY + target.getBoundingClientRect().top - bar.getBoundingClientRect().height - 24);
    target.focus({ preventScroll: true });
    window.scrollTo({ top: y, left: 0,
      behavior: smooth && !matchMedia('(prefers-reduced-motion: reduce)').matches ? 'smooth' : 'instant' });
    updateChapterPosition();
    return true;
  }
  function render(info, saved = null, initial = false) {
    const token = ++generation;
    const input = inputVersion;
    routeFromHash(); // Existing content/renderers; URL already validated.
    const { view, title } = decorate(info);
    renderedHash = location.hash;
    busy = false;
    const restore = () => {
      if (token !== generation || input !== inputVersion) return;
      updateTocVisibility();
      const focus = saved?.focusId ? byId(saved.focusId) : null;
      if (saved) {
        if (focus && view.contains(focus) && focus.getClientRects().length) focus.focus({ preventScroll: true });
        else if (!initial) title.focus({ preventScroll: true });
        window.scrollTo({ left: saved.x || 0, top: saved.y || 0, behavior: 'instant' });
      } else if (!info.section || !moveToSection(info.section)) {
        if (!initial) title.focus({ preventScroll: true });
        window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
      }
      remember(); updateChapterPosition();
    };
    requestAnimationFrame(restore);
    // Font loading can change line breaks; never yank the page after user input.
    document.fonts?.ready.then(() => requestAnimationFrame(restore));
  }
  function navigate(hash, up = false, source = null) {
    const info = describe(hash);
    const current = describe();
    if (busy) return;
    if (info.route === current.route && info.section) {
      remember(true, source || document.activeElement);
      if (moveToSection(info.section, true)) {
        writeState(info.hash); renderedHash = info.hash;
      }
      return;
    }
    if (info.route === current.route) {
      writeState(info.route); renderedHash = info.route;
      document.querySelector('.view.active h1')?.focus({ preventScroll: true });
      window.scrollTo({ top: 0, left: 0, behavior: 'instant' }); remember();
      return;
    }
    remember(true, source || document.activeElement);
    if (up && entry.from?.route === info.route) {
      busy = true; history.back(); return;
    }
    const from = { id: entry.id, route: entry.route };
    const saved = up ? lastVisit.get(info.route) : null;
    entry = makeEntry(info.route, from, saved);
    history.pushState({ portfolio: entry }, '', info.hash);
    render(info, saved);
  }
  function locationChanged() {
    if (location.hash === renderedHash && history.state?.portfolio?.id === entry?.id) { busy = false; return; }
    remember(false);
    const info = describe();
    const state = history.state?.portfolio;
    const saved = state?.route === info.route ? memory.get(state.id) || state : null;
    entry = saved ? { ...saved } : makeEntry(info.route);
    writeState(info.hash);
    render(info, saved);
  }

  document.addEventListener('click', event => {
    const a = event.target.closest('a');
    if (!a || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || a.target === '_blank' || a.hasAttribute('download')) return;
    if (a.dataset.skip) {
      event.preventDefault();
      const main = a.closest('.view').querySelector('main');
      main.focus({ preventScroll: true }); main.scrollIntoView({ block: 'start', behavior: 'instant' }); return;
    }
    if (a.dataset.route) { event.preventDefault(); navigate(a.dataset.route, a.dataset.up === 'true', a); }
  });
  ['pointerdown', 'wheel', 'touchstart', 'keydown'].forEach(type => {
    window.addEventListener(type, () => { inputVersion++; }, { passive: true, capture: true });
  });
  window.addEventListener('scroll', () => {
    if (!scrollFrame) scrollFrame = requestAnimationFrame(() => { scrollFrame = 0; updateChapterPosition(); });
    clearTimeout(saveTimer); saveTimer = setTimeout(() => remember(), 180);
  }, { passive: true });
  window.addEventListener('pagehide', () => remember());
  document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden') remember(); });
  let resizeTimer;
  window.addEventListener('resize', () => { clearTimeout(resizeTimer); resizeTimer = setTimeout(updateTocVisibility, 120); });
  window.addEventListener('popstate', locationChanged);
  window.addEventListener('hashchange', locationChanged);
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  flattenDirectory();
  const initial = describe();
  const previous = history.state?.portfolio;
  entry = previous?.route === initial.route ? { ...previous } : makeEntry(initial.route);
  writeState(initial.hash);
  render(initial, previous?.route === initial.route ? previous : null, true);
})();
