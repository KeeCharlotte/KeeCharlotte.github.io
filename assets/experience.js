/* A small navigation layer over the existing renderers. No framework or
   content fetch is required. Existing hashes remain valid. */
(() => {
  'use strict';
  // Software metadata shared by cards, detail pages, and breadcrumbs.
  Object.assign(projects.Software[0], {
    name: 'Veritrail',
    engineeringName: 'AAAS-TW',
    summaryEn: 'A traceable accounting and financial evidence workspace.',
    summaryZh: '可追溯的會計與財務證據工作台。',
    descriptionEn: 'A financial evidence and continuous-control workspace prototype for accountants, bookkeepers, and SMEs. It connects source documents, drafts, human review, controlled posting, reconciliation, and evidence exports. Currently limited to synthetic-data workflows in local/test environments; not production-ready.',
    descriptionZh: '面向會計師、記帳士與中小企業的財務證據與持續控制工作台原型，串接來源文件、草稿、人工覆核、受控過帳、對帳與佐證匯出。目前限本機／測試環境的合成資料流程，尚未正式上線。',
    status: 'In Development',
    technology: 'Python / Flask · PostgreSQL · HTML / CSS / JavaScript · Docker',
    github: 'https://github.com/KeeCharlotte/Veritrail-Portfolio'
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
  function addProjectAlias(title, project) {
    if (!title || !project?.engineeringName || title.querySelector('[data-engineering-name]')) return;
    const alias = el('span', 'project-work-zh', project.engineeringName);
    alias.dataset.engineeringName = 'true';
    // Reuse the original secondary-label style; only place this label on its own line.
    alias.style.display = 'block';
    alias.style.marginTop = '6px';
    alias.style.fontFamily = 'var(--sans)';
    title.append(document.createTextNode(' '), alias);
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
      addProjectAlias(byId('projectTitle'), projects[info.category]?.[index]);
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
      const a = routeLink(heading.textContent.trim(), info.route + '?section=' + heading.id);
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