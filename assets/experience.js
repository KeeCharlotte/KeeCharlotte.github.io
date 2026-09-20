/* A small navigation layer over the existing renderers. No framework or
   content fetch is required. Existing hashes remain valid. */
(() => {
  'use strict';
  // Project metadata shared by cards, detail pages, and breadcrumbs.
  Object.assign(projects.Software[0], {
    name: 'Veritrail',
    engineeringName: 'AAAS-TW',
    summaryEn: 'A traceable accounting and financial evidence workspace.',
    summaryZh: '可追溯的會計與財務證據工作台。',
    descriptionEn: 'A traceable workspace connecting source documents, human review, and accounting results.',
    descriptionZh: '帳跡把來源文件、人工覆核與帳務結果連在一起，讓每個數字都有可追查的依據。',
    status: 'In Development',
    technology: 'Python / Flask · PostgreSQL · HTML / CSS / JavaScript · Docker',
    technologyGroups: [
      { label: 'Backend', value: 'Python · Flask' },
      { label: 'Database', value: 'PostgreSQL' },
      { label: 'Frontend', value: 'HTML · CSS · JavaScript' },
      { label: 'Deployment', value: 'Docker' }
    ],
    overview: {
      workflowTitle: 'Workflow & controls · 流程與控制',
      workflowIntro: '從來源文件到帳務交付，串起資料依據、版本變更與操作責任；必要條件不成立時，流程停止，而不是勉強產生結果。',
      workflow: [
        {
          title: '來源接收與依據留存',
          text: '將來源文件與後續處理建立關聯，保留查閱、版本與內容核對依據，讓帳務結果能回到原始資料。',
          control: '有資料，不等於已有可信依據。'
        },
        {
          title: '草稿形成與政策檢查',
          text: '檢查交易資料、科目語意、金額與適用政策，再形成候選分錄；必要條件不足時要求補足。',
          control: '借貸平衡，不等於會計判斷正確。',
          branch: { label: '資料不足', text: '停止並要求補足，不以預設值或猜測繞過必要條件。' }
        },
        {
          title: '獨立覆核與補件重審',
          text: '由準備者以外的人確認與覆核；補件時保留舊版、建立新版，再重新完成確認與核准。',
          control: '內容變了，核准也要重新成立。',
          branch: { label: '覆核退回', text: '補件建立新版 → 重新確認與覆核，不沿用舊核准。' }
        },
        {
          title: '受控過帳與帳務更正',
          text: '過帳前重查來源、核准、科目、政策、權限與期間；更正以沖回或替代方式處理，保留原始關聯。',
          control: '已過帳內容，不以直接覆寫消除歷史。',
          branch: { label: '過帳後有誤', text: '另建更正案件 → 核准後沖回或替代，保留原紀錄與處理關聯。' }
        },
        {
          title: '對帳與異常處理',
          text: '配對提案經獨立確認；未解決差異進入例外處理，結案須有相應佐證，也保留重開歷程。',
          control: '配對不等於確認，標記不等於問題已解決。'
        },
        {
          title: '結果匯出與佐證交付',
          text: '將帳務結果連同相關歷程與佐證整理交付，分開記錄檔案建立、授權下載與獨立交付狀態。',
          control: '產生檔案，不等於完成交付。'
        }
      ],
      workflowControls: [
        '組織資料與操作權限隔離',
        '來源、版本與處理歷程追溯',
        '操作重試不重複產生帳務影響'
      ],
      workflowNote: '以上為系統流程與控制設計；各情境的支援及驗證範圍請見公開專案。',
      example: {
        heading: 'Case study · 合成資料案例',
        title: '草稿修改後，重新覆核再過帳',
        text: '一筆草稿退回補件後建立新版，重新完成獨立確認與核准，再由第三個帳號過帳並匯出分錄。舊版與退回歷程仍然保留，修改資料不沿用舊核准。',
        note: '2026-09-12 的歷史版本合成資料案例，不代表真實客戶成果或正式營運驗收。'
      },
      role: [
        '我負責提出問題、界定需求與範圍，並要求 AI 依目標修改。',
        '程式、文件、測試與修復由 AI 產出，測試由 AI 執行；這不等於我已親自重跑或獨立驗證整套系統。'
      ],
      more: '查看實作案例、功能範圍與最新專案狀態。'
    },
    github: 'https://github.com/KeeCharlotte/Veritrail-Portfolio',
    sourceLabel: 'View project'
  });
  // Main-game metadata; the frozen Babylon build remains a separate reference.
  Object.assign(projects.Games[0], {
    name: 'Civilization Rebuilt',
    summaryEn: 'A first-person simulation of rebuilding civilization from nature.',
    summaryZh: '從自然材料出發，逐步重建文明的第一人稱模擬遊戲。',
    descriptionEn: 'A first-person simulation of rebuilding civilization through observation and experimentation.',
    descriptionZh: '從自然材料出發，透過觀察、試驗與推理，逐步重建文明的第一人稱模擬遊戲。',
    start: 'May 2026',
    technology: 'Unity 6 · C# · URP · Blender',
    technologyGroups: [
      { label: 'Game Engine', value: 'Unity 6' },
      { label: 'Programming', value: 'C#' },
      { label: 'Rendering', value: 'Universal Render Pipeline (URP)' },
      { label: '3D Assets', value: 'Blender' }
    ],
    overview: {
      focusTitle: 'Design focus · 設計重點',
      highlights: [
        { title: '親手操作材料', text: '設計保留拿取、搬運與放置時的形狀、重量和接觸關係，不把材料只當作清單中的名稱。' },
        { title: '從觀察形成方法', text: '讓玩家先遇到問題，再比較材料、位置與做法，透過嘗試和修正理解條件，而非直接取得配方答案。' },
        { title: '讓成功成為可靠能力', text: '不只追求碰巧完成一次，而是理解方法何時成立，再逐步走向工具、製造與文明發展。' }
      ],
      example: {
        heading: 'Design scenario · 設計情境',
        title: '第一次面對寒冷',
        text: '天色逐漸轉暗，玩家需要決定先登高觀察附近地形，還是先搬運材料、安排停留的位置。探索可能帶來更好的判斷，但也會消耗準備時間；眼前方便的位置，也不一定適合整夜休息。',
        note: '這是呈現選擇與取捨的設計情境，不是已驗收的遊玩成果或固定攻略。'
      },
      role: [
        '我負責遊戲方向、世界與玩法取捨，並根據實際操作回饋調整需求。',
        'AI 參與研究整理、程式實作、製作工具與文件工作；人工操作回饋與自動檢查分開看待。'
      ],
      more: '查看研究、設計紀錄與最新開發進度。'
    },
    github: 'https://github.com/KeeCharlotte/Civilization-Rebuilt-Portfolio',
    sourceLabel: 'View project'
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
  // Stable project introductions; live progress and detailed evidence stay in the public repositories.
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
    const example = section('project-example', detail.example.heading);
    const exampleTitle = el('h3', 'project-item-title', detail.example.title); exampleTitle.lang = 'zh-Hant';
    const note = el('p', 'project-example-note', detail.example.note); note.lang = 'zh-Hant';
    example.append(exampleTitle, paragraph(detail.example.text), note);
    const role = section('project-role', 'My role · 我的角色');
    detail.role.forEach(text => role.append(paragraph(text)));
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
