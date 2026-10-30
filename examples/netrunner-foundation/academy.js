/* HACK THE PLANET Academy: local gameplay, independent of research claims. */
(function (root, factory) {
  'use strict';
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.NetrunnerAcademy = api;
})(typeof globalThis === 'object' ? globalThis : this, function () {
  'use strict';
  const copy = value => JSON.parse(JSON.stringify(value));
  const tracks = {
    solana: ['SOL-SYN-001', 'SOL-SYN-002', 'SOL-SYN-003'],
    arbitrum_one: ['ARB-SYN-001', 'ARB-SYN-002', 'ARB-SYN-003']
  };
  const lessons = {
    'SOL-SYN-001': {
      title: 'The ordering ghost',
      prompt: 'Three swaps move the midprice. Decide what this description supports before naming a cause.',
      evidence: ['Complete relevant transaction sequence', 'A screenshot of a profit counter', 'An unrelated Arbitrum recovery report'],
      correct: 'Complete relevant transaction sequence'
    },
    'SOL-SYN-002': {
      title: 'Two prices, one assumption',
      prompt: 'The reference says 150; the consumed value says 144. Is a discrepancy enough to establish manipulation?',
      evidence: ['Original feed timestamps/decimals', 'The size of the operator crew', 'An unrelated token price prediction'],
      correct: 'Original feed timestamps/decimals'
    },
    'SOL-SYN-003': {
      title: 'The missing record',
      prompt: 'Slot metadata and source samples are missing. Preserve the gap instead of completing the story.',
      evidence: ['Slot metadata and signed oracle source samples', 'A reputation badge', 'An Arbitrum sequencer status'],
      correct: 'Slot metadata and signed oracle source samples'
    },
    'ARB-SYN-001': {
      title: 'The price-input fork',
      prompt: 'Two synthetic ETH prices differ. Decide what you can infer before investigating the consumed feed.',
      evidence: ['On-chain consumed value path', 'A Solana slot reconstruction', 'A screenshot of a profit counter'],
      correct: 'On-chain consumed value path'
    },
    'ARB-SYN-002': {
      title: 'A monitor goes dark',
      prompt: 'A sequencer interruption marker appears. Could the observation channel itself have failed?',
      evidence: ['Independent sequencer verification', 'A crew reputation badge', 'A Solana transaction ordering rule'],
      correct: 'Independent sequencer verification'
    },
    'ARB-SYN-003': {
      title: 'Connection is not recovery',
      prompt: 'Connectivity returns, but protocol exposure has not been checked. Decide what remains unresolved.',
      evidence: ['Protocol-level post-recovery state', 'A green connection icon alone', 'An unrelated token price prediction'],
      correct: 'Protocol-level post-recovery state'
    }
  };

  function createSession(dossier, network) {
    if (!Object.hasOwn(tracks, network)) throw new Error('Choose Solana or Arbitrum One.');
    if (!dossier || dossier.mode !== 'OFFLINE_SYNTHETIC' || !Array.isArray(dossier.findings)) {
      throw new Error('Academy requires an offline synthetic dossier.');
    }
    const events = tracks[network].map(id => {
      const matches = dossier.findings.filter(f => f.event_id === id);
      const event = matches[0];
      if (matches.length !== 1 || event.network !== network || event.source_kind !== 'synthetic_fixture' ||
          !['HYPOTHESIS', 'UNKNOWN'].includes(event.claim_status)) {
        throw new Error('The mission source is incomplete or belongs to another network.');
      }
      return copy(event);
    });
    let cursor = 0;
    let phase = 'investigate';
    let inspected = false;
    let answers = [];

    function snapshot() {
      const event = events[cursor];
      const lesson = lessons[event.event_id];
      const result = answers[cursor] || null;
      return copy({
        network, phase, step: cursor + 1, total: events.length, inspected,
        eventId: event.event_id, title: lesson.title, prompt: lesson.prompt,
        evidenceChoices: lesson.evidence,
        source: inspected ? {observed_at: event.observed_at, source_ref: event.source_ref,
          source_kind: event.source_kind, observation: event.observation} : null,
        result,
        explanation: result ? {inference: event.inference,
          alternatives: event.alternative_explanations, missing: event.missing_evidence} : null,
        score: answers.reduce((sum, answer) => sum + answer.points, 0),
        maximum: events.length * 50,
        report: phase === 'complete' ? answers : []
      });
    }

    return Object.freeze({
      snapshot,
      inspect() {
        if (phase !== 'investigate') throw new Error('This decision is already recorded.');
        inspected = true;
        return snapshot();
      },
      submit(claim, evidence) {
        if (phase !== 'investigate') throw new Error('Each stage can be scored only once.');
        if (!inspected) throw new Error('Inspect the source record before recording a decision.');
        if (!['HYPOTHESIS', 'UNKNOWN', 'EVIDENCE'].includes(claim) ||
            !lessons[events[cursor].event_id].evidence.includes(evidence)) {
          throw new Error('Choose one claim status and one evidence request.');
        }
        const event = events[cursor];
        const expectedEvidence = lessons[event.event_id].correct;
        const claimCorrect = claim === event.claim_status;
        const evidenceCorrect = evidence === expectedEvidence;
        answers.push({eventId: event.event_id, claim, evidence, claimCorrect, evidenceCorrect,
          expectedClaim: event.claim_status, expectedEvidence,
          points: (claimCorrect ? 25 : 0) + (evidenceCorrect ? 25 : 0)});
        phase = 'review';
        return snapshot();
      },
      next() {
        if (phase !== 'review') throw new Error('Record and review the current decision first.');
        if (cursor === events.length - 1) phase = 'complete';
        else { cursor += 1; phase = 'investigate'; inspected = false; }
        return snapshot();
      },
      reset() {
        cursor = 0; phase = 'investigate'; inspected = false; answers = [];
        return snapshot();
      }
    });
  }
  return Object.freeze({createSession});
});
