'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {createSession} = require('./academy.js');
const dossier = JSON.parse(fs.readFileSync(path.join(__dirname, 'synthetic-dossier.json'), 'utf8'));

const answers = {
  solana: [
    ['HYPOTHESIS', 'Complete relevant transaction sequence'],
    ['HYPOTHESIS', 'Original feed timestamps/decimals'],
    ['UNKNOWN', 'Slot metadata and signed oracle source samples']
  ],
  arbitrum_one: [
    ['HYPOTHESIS', 'On-chain consumed value path'],
    ['HYPOTHESIS', 'Independent sequencer verification'],
    ['HYPOTHESIS', 'Protocol-level post-recovery state']
  ]
};

for (const network of Object.keys(answers)) {
  test(`${network}: complete investigation, review and debrief without changing the dossier`, () => {
    const original = JSON.stringify(dossier);
    const session = createSession(dossier, network);
    assert.throws(() => session.next(), /Record and review/);
    for (const [claim, evidence] of answers[network]) {
      assert.equal(session.snapshot().source, null);
      assert.throws(() => session.submit(claim, evidence), /Inspect/);
      assert.equal(session.inspect().source.source_kind, 'synthetic_fixture');
      const reviewed = session.submit(claim, evidence);
      assert.equal(reviewed.result.points, 50);
      assert.equal(reviewed.phase, 'review');
      assert.throws(() => session.submit(claim, evidence), /only once/);
      session.next();
    }
    const result = session.snapshot();
    assert.equal(result.phase, 'complete');
    assert.equal(result.score, 150);
    assert.equal(result.report.length, 3);
    assert.equal(JSON.stringify(dossier), original);
  });
}

test('unsupported incident claims lose points and receive explicit correction', () => {
  const session = createSession(dossier, 'solana');
  session.inspect();
  const result = session.submit('EVIDENCE', 'A screenshot of a profit counter');
  assert.equal(result.score, 0);
  assert.equal(result.result.expectedClaim, 'HYPOTHESIS');
  assert.equal(result.result.expectedEvidence, 'Complete relevant transaction sequence');
  assert.match(result.explanation.inference, /does not prove/);
});

test('reset discards answers, score and source inspection and permits a fresh attempt', () => {
  const session = createSession(dossier, 'solana');
  session.inspect(); session.submit(...answers.solana[0]); session.next();
  const reset = session.reset();
  assert.equal(reset.step, 1);
  assert.equal(reset.score, 0);
  assert.equal(reset.result, null);
  assert.equal(reset.inspected, false);
  session.inspect();
  assert.equal(session.submit(...answers.solana[0]).score, 50);
});

test('network spoofing, duplicate IDs and live datasets cannot enter the exercise', () => {
  assert.throws(() => createSession(dossier, '__proto__'), /Choose/);
  assert.throws(() => createSession({...dossier, mode:'LIVE'}, 'solana'), /synthetic/);
  const wrong = structuredClone(dossier);
  wrong.findings.find(f => f.event_id === 'SOL-SYN-001').network = 'arbitrum_one';
  assert.throws(() => createSession(wrong, 'solana'), /another network/);
  const duplicate = structuredClone(dossier);
  duplicate.findings.push(duplicate.findings.find(f => f.event_id === 'SOL-SYN-001'));
  assert.throws(() => createSession(duplicate, 'solana'), /incomplete/);
});

test('invalid choices are rejected without consuming or scoring the attempt', () => {
  const session = createSession(dossier, 'solana'); session.inspect();
  assert.throws(() => session.submit('EVIDENCE', 'invented request'), /Choose/);
  assert.equal(session.snapshot().phase, 'investigate');
  assert.equal(session.submit(...answers.solana[0]).score, 50);
});

test('returned snapshots and later caller edits cannot mutate an active mission', () => {
  const input = structuredClone(dossier);
  const session = createSession(input, 'solana');
  input.findings.find(f => f.event_id === 'SOL-SYN-001').claim_status = 'EVIDENCE';
  const snapshot = session.inspect(); snapshot.source.observation.pattern_summary = 'tampered';
  assert.notEqual(session.snapshot().source.observation.pattern_summary, 'tampered');
  assert.equal(session.submit(...answers.solana[0]).result.expectedClaim, 'HYPOTHESIS');
});
