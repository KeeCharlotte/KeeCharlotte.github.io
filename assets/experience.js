/* A small navigation layer over the existing renderers. No framework or
   content fetch is required. Existing hashes remain valid. */
(() => {
  'use strict';
  // Pin the site's dated claims to an already-public portfolio snapshot.
  const ledgerTrailSnapshot = 'https://github.com/KeeCharlotte/LedgerTrail-Portfolio/blob/d20a0ddcdc7c400f2566fad9a05e9af81f1a9662/';
  // Project metadata shared by cards, detail pages, and breadcrumbs.
  Object.assign(projects.Software[0], {
    name: 'LedgerTrail',
    engineeringName: 'AAAS-TW / AAAS',
    summaryEn: 'An accounting workspace spanning review, posting, corrections, and evidence.',
    summaryZh: '串起來源、覆核、過帳、更正與交付，並管理組織權限及版本依據。',
    descriptionEn: 'An AI-assisted accounting systems project connecting workflows, database controls, and traceable evidence.',
    descriptionZh: '帳跡面向會計師／記帳士主導的中小企業流程，讓人查到數字的依據、處理者、使用版本與未解問題。完整系統保留私人，公開政策模組只是其中一個實作樣本。',
    status: 'Local / synthetic prototype',
    technology: 'Python / Flask · PostgreSQL · HTML / CSS / JavaScript · Docker',
    technologyGroups: [
      { label: 'Backend', value: 'Python · Flask' },
      { label: 'Database', value: 'PostgreSQL' },
      { label: 'Frontend', value: 'HTML · CSS · JavaScript' },
      { label: 'Deployment', value: 'Docker' }
    ],
    overview: {
      scope: {
        heading: 'System scope · 系統全貌',
        items: [
          { title: '12 個功能領域', text: '涵蓋身分與平台治理、來源、草稿、覆核、過帳更正、對帳、交付、證據、工作台、恢復、AI 控制及外部接入；實作、受限與待完成項目分開列示。' },
          { title: '727 個 SQL 目錄項目', text: '涵蓋會計、安全治理、證據及維運。這是生成目錄的物件統計，包含停用與相容資產，不是 727 個可用功能，也不是部署中的實測物件數。' },
          { title: '1,838 個不重複 Python 案例', text: '0c15ee9 修復基準記錄互補環境取得 PASS；其中 29 套隔離 PostgreSQL 模組記錄 298 項通過。數字不相加，也不代表最新版本重新驗收。' }
        ],
        note: '2026-09-29 盤點，對照公開作品集 0.4.0／d20a0dd，系統盤點來源 2bc586c。完整系統測試數沿用庫內紀錄，本次未重跑或取得全部原始 JUnit。',
        link: { label: '查看系統架構與統計口徑', url: ledgerTrailSnapshot + 'docs/ARCHITECTURE.md' }
      },
      workflowTitle: 'Workflow & controls · 流程與控制',
      workflowIntro: '工作台與 API 連接領域服務、PostgreSQL、背景工作及證據查詢。下列是主要操作流程，不是所有元件都依序執行；必要條件不成立時停止。',
      workflow: [
        { title: '來源與欄位', text: '受控上傳、查閱與版本關聯；固定合成文字模板可帶入欄位，文件原值與人工修正分開保存。', control: '帶入欄位，不等於完成辨識或覆核。' },
        { title: '草稿與科目', text: '檢查交易語意、金額、政策及科目。科目修訂另有提案、獨立決策、生效、取代與停用。', control: '借貸平衡，不等於會計判斷正確。' },
        { title: '確認、覆核與補件', text: '必要確認與核准分工處理；補件保留原版，建立新版後重新覆核。', branch: { label: '覆核退回', text: '補件 → 新版本 → 重新確認，不沿用舊核准。' } },
        { title: '過帳、更正與期間', text: '寫入時重驗來源、政策、權限與期間；更正透過受控沖回或替代重記，保留原帳依據。', branch: { label: '已過帳有誤', text: '另提更正案件，經核准及必要期間控制後處理。' } },
        { title: '對帳與例外', text: '合成銀行資料配對經獨立確認；例外須依對應佐證結案，保留拒絕及重開歷程。', control: '配對成功，不代表所有差異已解決。' },
        { title: '交付與具名審查', text: '建立與下載 CSV、限定範圍的證據包，分開記錄交付、開啟與回覆。', control: '下載或回覆，不等於外部接受或離線驗證通過。' }
      ],
      workflowControls: ['不同組織的資料與權限分開', '保存來源、版本與處理歷程', '未知結果先查回，不任意重送'],
      workflowNote: '目前主要操作限本機／測試與合成資料；工作台交付包尚未完整接通離線驗證器。',
      cases: {
        heading: 'Design cases · 跨模組難題',
        items: [
          { title: '改了科目，舊帳依據怎麼辦？', text: '科目生效、原核准、目前認列、銀行結算及更正鏈必須協調。新設定不能直接改寫過去，單一函式通過也不足以證明整條流程成立。' },
          { title: '逾時，是沒入帳還是沒收到回覆？', text: '保留原操作與內容，先查提交結果；允許重試時沿用原操作身分。不把網路錯誤當成另一筆交易，也不把未知結果顯示為成功。' },
          { title: '切換客戶，舊請求還能回來嗎？', text: '每個組織重查成員與細分權限，清除舊畫面並拒收過期回應。管理員身分、看得到案件與有權過帳是不同條件。' }
        ],
        note: '這些是有來源的問題與控制原則，不是本次新跑的完整測試。',
        link: { label: '閱讀案例、取捨與驗證限制', url: ledgerTrailSnapshot + 'docs/CASE_STUDY.md' }
      },
      progress: {
        heading: 'Current status · 進度與界線',
        items: [
          { title: '已有的受控操作', text: '來源核對、製單、確認與核准、第三個帳號過帳、CSV 下載，以及案件搜尋、帳跡與本機試用引導。三個帳號不等於三位真人獨立覆核。' },
          { title: '仍待接通與驗證', text: '真實來源、通用 OCR／ERP 等接入、專業政策採信、交付包與離線工具銜接，以及完整發布與正式維運驗收。部分還要實作，不只是缺 API key。' },
          { title: '刻意暫緩', text: '跨國合併、永續報告、零知識證明、公有鏈及自主資金等 14 類不列入近期可用功能。另有帳齡／現金流投影未完成，所有環境停用；AI 財務變更控制限內部實驗。' }
        ],
        link: { label: '查看 12 領域、暫緩項目與剩餘工作', url: ledgerTrailSnapshot + 'docs/STATUS.md' }
      },
      example: {
        heading: 'Recorded outcome · 歷史操作成果',
        title: '105 元退回，210 元新版重新核准後過帳',
        text: '2026-09-12 的合成瀏覽器測試保留舊版與退回歷程，新版重新確認及覆核，再由第三個帳號過帳。原 CSV 有同一分錄 3 行，借貸各 210 元；公開政策函式另有 112 項測試的原紀錄。',
        note: '流程版本 9012a79、模組版本 4841c001；不是最新版畫面或真實客戶成果。當時整批 19 個工作有 18 個成功，安全套件 2 項失敗仍保留，局部 PASS 不覆蓋整輪失敗。',
        link: { label: '查看原圖、CSV 與歷史結果', url: ledgerTrailSnapshot + 'docs/CASE_STUDY.md#historical-demo' }
      },
      role: [
        '我以會計背景提出問題、界定範圍及驗收要求，檢視 AI 回報與證據，再依操作反例要求修正。例如減少來源重抄、讓拒絕可定位，並保留原錯誤案件，而不是放寬控制讓它通過。',
        'AI 協助程式、文件、測試與證據產出。我尚未親自完整重跑或獨立驗證整套系統；系統規模不等於我獨力完成全部實作。'
      ],
      more: '完整架構、功能狀態與證據請看公開作品集；本網站不提供完整工作台、核心後端、SQL 或試用帳密。',
      roleLink: { label: '需求、取捨與實際分工', url: ledgerTrailSnapshot + 'docs/CASE_STUDY.md#contribution' }
    },
    github: 'https://github.com/KeeCharlotte/LedgerTrail-Portfolio',
    sourceLabel: 'View full portfolio'
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
  // Project summaries can cite dated public snapshots; other projects keep their existing layout.
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
