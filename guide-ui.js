/* Step-by-step guides for the 148 approved checklist items.
   Notes live in sxm-notes under guide:<id>, the same synced object as every other note.
   An empty string means the note was cleared, so an older note is not shown again. */
(function () {
  'use strict';
  var OPEN = {};
  var QUERY = '';

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function notesObj() {
    try {
      var v = JSON.parse(localStorage.getItem('sxm-notes') || '{}');
      if (v && typeof v === 'object' && !Array.isArray(v)) return v;
    } catch (e) {}
    return {};
  }

  function readNote(item) {
    var notes = notesObj();
    var k = 'guide:' + item.id;
    if (Object.prototype.hasOwnProperty.call(notes, k)) return notes[k];
    var maps = item.mapsTo || [];
    for (var i = 0; i < maps.length; i++) {
      if (notes[maps[i]]) return notes[maps[i]];
    }
    return '';
  }

  function saveNote(id, value) {
    var notes = notesObj();
    var k = 'guide:' + id;
    var v = String(value || '');
    notes[k] = v.trim() ? v.trim() : '';
    localStorage.setItem('sxm-notes', JSON.stringify(notes));
  }

  function legacyDone(ctx, item) {
    var st = ctx.trkState(item.storeKey) || {};
    if (st[item.id] === 'Done') return false;
    var pref = (window.SXMGuide && window.SXMGuide.legacyPrefix) || {};
    var maps = item.mapsTo || [];
    for (var i = 0; i < maps.length; i++) {
      var p = String(maps[i]).split(':');
      var key = pref[p[0]];
      if (!key || (key === item.storeKey && p[1] === item.id)) continue;
      var old = ctx.trkState(key) || {};
      if (old[p[1]] === 'Done') return true;
    }
    return false;
  }

  function contactHtml(id) {
    var c = window.SXMGuide.contacts[id];
    if (!c) return '';
    var tel = c.tel ? ' <a href="tel:' + esc(c.tel) + '">Tap to call</a>' : '';
    return '<div class="gcontact"><b>' + esc(c.title) + '</b>' + tel +
      '<ul>' + (c.lines || []).map(function (line) { return '<li>' + esc(line) + '</li>'; }).join('') + '</ul>' +
      '<p class="est">Source: ' + esc(c.source) + (c.url ? ' · <a href="' + esc(c.url) + '" target="_blank" rel="noopener">Open the page</a>' : '') + '</p></div>';
  }

  function itemHtml(ctx, item) {
    var st = ctx.trkState(item.storeKey) || {};
    var done = st[item.id] === 'Done';
    var note = readNote(item);
    var open = OPEN[item.id] ? ' open' : '';
    var q = (item.title + ' ' + (item.phase || '') + ' ' + item.id).toLowerCase();
    var links = item.links.length
      ? item.links.map(function (L) {
        var badge = L.state === 'verified'
          ? '<span class="gok">Checked</span>'
          : '<span class="gflag">Check in Chrome</span>';
        return '<a class="glink" href="' + esc(L.url) + '" target="_blank" rel="noopener"><b>' + esc(L.label) + '</b><br>' +
          badge + ' <span class="est">' + esc(L.detail) + '</span></a>';
      }).join('')
      : '<p>No official web page for this step. The source is named under Tips. A web address was not guessed.</p>';
    var steps = '<ol class="gsteps">' + item.steps.map(function (s) { return '<li>' + esc(s) + '</li>'; }).join('') + '</ol>';
    var ready = '<ul>' + item.haveReady.map(function (s) { return '<li>' + esc(s) + '</li>'; }).join('') + '</ul>';
    var tips = '<ul>' + item.tips.map(function (s) { return '<li>' + esc(s) + '</li>'; }).join('') + '</ul>';
    var contacts = (item.contactIds || []).map(contactHtml).join('');
    var legacy = legacyDone(ctx, item)
      ? '<p class="est">This was already marked done on an earlier list. The tick is still there. Tick this box too when you are happy with this version.</p>'
      : '';
    var phase = item.phase ? '<span class="tag">' + esc(item.phase) + '</span> ' : '';
    var who = item.appliesWhenLabel ? '<span class="est">' + esc(item.appliesWhenLabel) + '</span>' : '';
    return '<article class="gitem' + open + '" data-gid="' + esc(item.id) + '" data-q="' + esc(q) + '">' +
      '<div class="ghead"><label class="chk"><input type="checkbox" data-act="guide-done" data-k="' + esc(item.storeKey) + '" data-i="' + esc(item.id) + '"' +
      (done ? ' checked' : '') + ' aria-label="Done: ' + esc(item.title) + '"></label>' +
      '<button type="button" class="gopen" data-act="guide-open" aria-expanded="' + (open ? 'true' : 'false') + '">' +
      phase + esc(item.title) +
      '<span class="sub">' + (done ? 'Done · ' : '') + esc(item.estTime || '') + (who ? ' · ' + who : '') + ' · tap for steps</span></button></div>' +
      '<div class="gbody">' + legacy +
      (item.alert ? '<div class="callout warn"><b class="t">Florida licences</b>' + esc(item.alert) + '</div>' : '') +
      '<div class="gsec"><h4>1. Official pages</h4>' + links + '</div>' +
      '<div class="gsec"><h4>2. Do this</h4>' + steps +
      ((item.earlierSteps && item.earlierSteps.length) ? '<details class="archive"><summary>Earlier wording (kept)</summary><ol class="gsteps">' + item.earlierSteps.map(function (s) { return '<li>' + esc(s) + '</li>'; }).join('') + '</ol></details>' : '') +
      '</div>' +
      '<div class="gsec"><h4>3. What to have ready</h4>' + ready + '</div>' +
      '<div class="gsec"><h4>4. Tips, phone numbers and addresses</h4>' + tips + contacts + '</div>' +
      '<div class="gsec"><h4>5. Your notes</h4>' +
      '<p class="est">For Queenie and Michael. Saved on this phone and, when Google Drive sync is on, in your Scout file with the rest of your data. Do not type passport numbers, Social Security numbers, bank numbers, or medical details.</p>' +
      '<textarea class="gnote" data-act="guide-note" data-i="' + esc(item.id) + '" aria-label="Notes for ' + esc(item.title) + '" placeholder="Type a reminder. Leave out ID numbers.">' + esc(note) + '</textarea>' +
      (ctx.stampHtml ? ctx.stampHtml('sxm-notes', 'guide:' + item.id, 'Note saved') : '') +
      '</div></div></article>';
  }

  function catHtml(ctx, cat, onlyIds, anchor) {
    var items = cat.items.filter(function (it) { return !onlyIds || onlyIds[it.id]; });
    if (!items.length) return '';
    var done = 0;
    items.forEach(function (it) { if ((ctx.trkState(it.storeKey) || {})[it.id] === 'Done') done++; });
    var html = '<section class="gcat"' + (anchor ? ' id="gcat-' + esc(cat.id) + '"' : '') + '><h3>' + esc(cat.title) + ' <span class="est">' + done + ' of ' + items.length + '</span></h3>';
    if (!onlyIds) {
      html += '<p>' + esc(cat.intro || '') + '</p>';
      if (cat.differs) html += '<div class="callout"><b class="t">Saint-Martin differs</b>' + esc(cat.differs) + '</div>';
    }
    html += items.map(function (it) { return itemHtml(ctx, it); }).join('') + '</section>';
    return html;
  }

  function findCat(id) {
    var cats = window.SXMGuide.categories;
    for (var i = 0; i < cats.length; i++) if (cats[i].id === id) return cats[i];
    return null;
  }

  function renderMount(el, ctx) {
    var which = el.getAttribute('data-guide');
    var idAttr = el.getAttribute('data-guide-ids');
    var only = null;
    if (idAttr) {
      only = {};
      idAttr.split(',').forEach(function (id) { only[id] = 1; });
    }
    var html = '';
    if (which === 'all') {
      var G = window.SXMGuide;
      var total = 0, doneN = 0;
      G.categories.forEach(function (cat) {
        cat.items.forEach(function (it) {
          total++;
          if ((ctx.trkState(it.storeKey) || {})[it.id] === 'Done') doneN++;
        });
      });
      html += '<div class="nolaw"><b>Not legal, tax, or immigration advice.</b> ' + esc(G.disclaimer) + '</div>';
      html += '<div class="callout warn"><b class="t">Visa timing</b>' + esc(G.timeline) + '</div>';
      html += '<div class="card"><h3>Questions to settle</h3><ol>' + G.questions.map(function (q) { return '<li>' + esc(q) + '</li>'; }).join('') + '</ol><p class="est">From the open questions gathered with this checklist. Write the answers in the notes box on the matching step.</p></div>';
      html += '<p><b>' + doneN + ' of ' + total + '</b> steps ticked. Link check on ' + esc(G.checked) + ': <b>' + G.verifiedLinks + '</b> links opened, <b>' + G.flaggedLinks + '</b> flagged (blocked automatic check, or the page would not reopen). Flagged links are still shown. No address was invented to replace one.</p>';
      html += '<label for="guide-search">Find a step</label><input id="guide-search" data-act="guide-search" type="search" placeholder="Try visa, bank, hospital…" value="' + esc(QUERY) + '" autocomplete="off">';
      html += '<div class="gjump">' + G.categories.map(function (cat) {
        return '<button type="button" class="btn alt sm" data-act="jump" data-to="gcat-' + esc(cat.id) + '">' + esc(cat.title) + '</button>';
      }).join('') + '</div>';
      html += G.categories.map(function (cat) { return catHtml(ctx, cat, null, true); }).join('');
    } else {
      var cat = findCat(which);
      if (!cat) return;
      html += '<p class="est">Approved steps. The same ticks and notes are on <a href="#guides">Step-by-step</a>.</p>';
      html += catHtml(ctx, cat, only, false);
    }
    el.innerHTML = html;
    if (QUERY) applyQuery(el);
  }

  function applyQuery(root) {
    var q = QUERY.trim().toLowerCase();
    root.querySelectorAll('[data-gid]').forEach(function (el) {
      var hay = el.getAttribute('data-q') || '';
      el.style.display = (!q || hay.indexOf(q) >= 0) ? '' : 'none';
    });
  }

  function previewBanner() {
    var el = document.getElementById('preview-banner');
    if (!el) return;
    var h = location.hostname || '';
    var live = h === 'blur7285.github.io' || h === 'localhost' || h === '127.0.0.1';
    if (live) { el.hidden = true; el.innerHTML = ''; return; }
    el.hidden = false;
    el.innerHTML = '<b>Review copy.</b> The live app is unchanged. Ticks and notes you type here stay on this web address only. They do not sync into the live Scout file. Google sign-in works on the live site, not on this preview.';
  }

  if (window.SXM_SECTIONS && !window.SXM_SECTIONS.some(function (s) { return s.id === 'guides'; })) {
    window.SXM_SECTIONS.splice(3, 0, {
      id: 'guides',
      title: 'Step-by-step',
      icon: '📋',
      group: 'Start here',
      desc: 'All 148 move steps, with links, what to bring, and your notes'
    });
  }

  document.addEventListener('input', function (e) {
    var t = e.target;
    if (!t || !t.getAttribute) return;
    if (t.getAttribute('data-act') === 'guide-note') saveNote(t.getAttribute('data-i'), t.value);
    if (t.getAttribute('data-act') === 'guide-search') {
      QUERY = t.value;
      var root = t.closest('[data-guide]') || document;
      applyQuery(root);
    }
  });

  window.SXMGuideUI = {
    rememberOpen: function (id, on) {
      if (!id) return;
      if (on === false) delete OPEN[id];
      else OPEN[id] = 1;
    },
    render: function (ctx) {
      if (!window.SXMGuide) return;
      previewBanner();
      document.querySelectorAll('[data-guide]').forEach(function (el) {
        if (!el.closest('.page.on') && el.closest('.page')) return;
        renderMount(el, ctx);
      });
    }
  };
})();
