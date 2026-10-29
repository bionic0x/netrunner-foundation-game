/* UI adapter: presentation and game state never write into the source dossier. */
(function () {
  'use strict';
  const host = document.getElementById('academy-stage');
  const source = JSON.parse(document.getElementById('dossier-data').textContent);
  let session = null;
  let network = 'solana';

  function node(tag, text, className) {
    const el = document.createElement(tag);
    if (text !== undefined) el.textContent = text;
    if (className) el.className = className;
    return el;
  }
  function button(text, handler, secondary) {
    const el = node('button', text, 'button' + (secondary ? ' alt' : ''));
    el.type = 'button'; el.onclick = handler;
    return el;
  }
  function focusTitle() { host.querySelector('h3').focus(); }
  function heading(text) { const el = node('h3', text); el.tabIndex = -1; return el; }
  function brief() {
    session = null;
    host.replaceChildren();
    const panel = node('div', undefined, 'panel mission-brief');
    panel.append(node('div', 'MISSION 001 // GHOST SIGNAL', 'tiny'), heading('Question the signal. Keep the evidence.'),
      node('p', 'A three-stage investigation with ACID BURN. Inspect each source, choose the claim it supports, and request the evidence that could change your judgment.'),
      node('p', '50 training points per stage: 25 for claim discipline and 25 for the evidence request. Scores describe this exercise only. Progress stays in this tab and resets on reload.', 'mission-note'));
    const label = node('label', 'Choose your network track'); label.htmlFor = 'mission-network';
    const select = node('select'); select.id = 'mission-network';
    for (const [value, title] of [['solana', 'Solana'], ['arbitrum_one', 'Arbitrum One']]) {
      const option = node('option', title); option.value = value; select.append(option);
    }
    select.value = network;
    select.onchange = () => {network = select.value;};
    panel.append(label, select, button('Jack in · start mission', () => {
      try { session = NetrunnerAcademy.createSession(source, network); render(); focusTitle(); }
      catch (err) { status.textContent = err.message; }
    }));
    const status = node('p', '', 'mission-note'); status.setAttribute('role', 'alert'); panel.append(status);
    host.append(panel);
  }
  function choices(form, name, title, values, disabled) {
    const fieldset = node('fieldset'); fieldset.disabled = disabled;
    fieldset.append(node('legend', title));
    for (const [value, text] of values) {
      const label = node('label', undefined, 'mission-option');
      const input = node('input'); input.type = 'radio'; input.name = name;
      input.value = value; input.required = true;
      label.append(input, node('span', text)); fieldset.append(label);
    }
    form.append(fieldset);
  }
  function render() {
    const state = session.snapshot();
    host.replaceChildren();
    const top = node('div', undefined, 'mission-progress');
    top.append(node('span', (state.network === 'solana' ? 'SOLANA' : 'ARBITRUM ONE') + ' // ' +
      (state.phase === 'complete' ? 'DEBRIEF' : 'STAGE ' + state.step + ' OF ' + state.total)),
      node('span', state.score + ' / ' + state.maximum + ' TRAINING POINTS'));
    host.append(top);
    if (state.phase === 'complete') {
      const panel = node('div', undefined, 'panel');
      panel.append(heading('Mission complete · evidence preserved'),
        node('p', 'You recorded three decisions. Review the lessons below, then replay either track. The research dossier and its digest remain unchanged.'));
      const list = node('ul', undefined, 'mission-report');
      for (const answer of state.report) list.append(node('li', answer.eventId + ': ' + answer.points +
        '/50 · Supported status: ' + answer.expectedClaim + ' · Next evidence: ' + answer.expectedEvidence));
      panel.append(list, button('Replay mission', () => {brief(); focusTitle();})); host.append(panel); return;
    }
    const grid = node('div', undefined, 'grid mission-grid');
    const evidencePanel = node('div', undefined, 'panel');
    evidencePanel.append(heading(state.title), node('div', state.eventId + ' · SYNTHETIC', 'tiny'), node('p', state.prompt));
    if (!state.inspected) {
      evidencePanel.append(button('Inspect source record', () => {session.inspect(); render(); focusTitle();}));
    } else {
      evidencePanel.append(node('div', 'SOURCE RECORD · NOT A VERIFIED INCIDENT', 'fieldname'),
        node('p', state.source.source_ref + ' · ' + state.source.source_kind, 'mission-note'),
        node('p', state.source.observed_at, 'mission-note'),
        node('pre', JSON.stringify(state.source.observation, null, 2), 'mission-record'));
    }
    const decisionPanel = node('div', undefined, 'panel');
    decisionPanel.append(node('h4', 'Your decision'));
    const form = node('form');
    choices(form, 'claim', 'What does this source support?', [
      ['HYPOTHESIS', 'Hypothesis · a possible issue requires investigation'],
      ['UNKNOWN', 'Unknown · required observations are missing'],
      ['EVIDENCE', 'Verified real-world incident · the cause is established']
    ], !state.inspected || state.phase === 'review');
    choices(form, 'evidence', 'What evidence should you request next?',
      state.evidenceChoices.map(text => [text, text]), !state.inspected || state.phase === 'review');
    const submit = node('button', 'Record decision', 'button'); submit.type = 'submit';
    submit.disabled = !state.inspected || state.phase === 'review'; form.append(submit);
    const error = node('p', '', 'mission-note'); error.setAttribute('role', 'alert'); form.append(error);
    form.onsubmit = event => {
      event.preventDefault();
      const data = new FormData(form);
      try {session.submit(data.get('claim'), data.get('evidence')); render(); host.querySelector('.mission-feedback').focus();}
      catch (err) {error.textContent = err.message;}
    };
    if (state.result) {
      for (const input of form.querySelectorAll('input')) input.checked = state.result[input.name] === input.value;
    }
    decisionPanel.append(form);
    grid.append(evidencePanel, decisionPanel); host.append(grid);
    if (state.result) {
      const result = state.result;
      const feedback = node('div', undefined, 'panel mission-feedback'); feedback.tabIndex = -1;
      feedback.append(node('h4', 'Decision recorded · ' + result.points + '/50'),
        node('p', (result.claimCorrect ? 'Claim supported. ' : 'Revise the claim. ') +
          'Supported status: ' + result.expectedClaim + '. ' + state.explanation.inference),
        node('p', (result.evidenceCorrect ? 'Useful evidence request: ' : 'A more useful evidence request: ') + result.expectedEvidence + '.'),
        node('div', 'Alternatives and unresolved evidence', 'fieldname'));
      const alternatives = node('ul', undefined, 'alts');
      for (const text of state.explanation.alternatives) alternatives.append(node('li', text));
      if (!alternatives.children.length) alternatives.append(node('li', 'The required observations are missing; keep the conclusion unknown.'));
      feedback.append(alternatives, node('p', state.explanation.missing.join(' · '), 'mission-note'),
        button(state.step === state.total ? 'Open mission debrief' : 'Next stage', () => {session.next(); render(); focusTitle();}));
      host.append(feedback);
    }
    host.append(button('Reset mission', () => {brief(); focusTitle();}, true));
  }
  brief();
})();
