import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const raw = fs.readFileSync(new URL('../guide-data.js', import.meta.url), 'utf8');
const data = JSON.parse(raw.replace(/^window\.SXMGuide\s*=\s*/, '').replace(/;\s*$/, ''));

test('all 148 steps have the five detail parts and a sync key', () => {
  assert.equal(data.itemCount, 148);
  const ids = [];
  for (const cat of data.categories) {
    for (const item of cat.items) {
      ids.push(item.id);
      assert.ok(item.steps.length, item.id + ' steps');
      assert.ok(item.haveReady.length >= 3, item.id + ' haveReady');
      assert.ok(item.tips.length, item.id + ' tips');
      assert.ok(Array.isArray(item.links), item.id + ' links');
      assert.ok(item.storeKey.startsWith('sxm-'), item.id + ' store');
      for (const link of item.links) {
        assert.ok(link.url.startsWith('https://'), item.id + ' url');
        assert.ok(link.state === 'verified' || link.state === 'flagged', item.id);
        assert.ok(link.detail, item.id + ' link detail');
      }
      for (const cid of item.contactIds) {
        assert.ok(data.contacts[cid], cid);
        assert.ok(data.contacts[cid].lines.length, cid + ' lines');
      }
    }
  }
  assert.equal(new Set(ids).size, 148);
  assert.equal(data.verifiedLinks + data.flaggedLinks, ids.reduce((n, id) => n, 0) + data.categories.reduce((n, c) => n + c.items.reduce((m, it) => m + it.links.length, 0), 0));
});
