import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from datetime import datetime, timedelta

SPEC = importlib.util.spec_from_file_location('controller', Path(__file__).resolve().parents[1] / 'office/controller.py')
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)

class OfficeTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        src = Path(__file__).resolve().parents[1] / 'office'
        (self.root / 'office').mkdir()
        for name in ['config.json', 'campaign.json']:
            (self.root / 'office' / name).write_bytes((src / name).read_bytes())
        self.now = datetime.fromisoformat('2026-10-29T08:00:00+07:00')
    def tearDown(self):
        self.temp.cleanup()
    def submit(self, task, **changes):
        p = self.root / task['expected_output']
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text('Research with sources')
        r = dict(task_id=task['id'], worker=task['worker'], status='completed', submitted_at=self.now.isoformat(), artifacts=[task['expected_output']], source_urls=['https://example.org'])
        r.update(changes)
        m.save(self.root / 'office/submissions' / (task['id'] + '.json'), r)
    def test_idempotence_and_dependency(self):
        a = m.run(self.root, self.now)
        b = m.run(self.root, self.now + timedelta(days=1))
        self.assertEqual(len(a['tasks']), len(b['tasks']))
        self.assertEqual(b['tasks'][1]['status'], 'waiting')
        self.assertEqual(b['tasks'][2]['status'], 'waiting')
    def test_real_handoff_unlocks_plan(self):
        a = m.run(self.root, self.now)
        self.submit(a['tasks'][0])
        b = m.run(self.root, self.now)
        self.assertEqual(b['tasks'][0]['status'], 'completed')
        self.assertEqual(b['tasks'][1]['status'], 'ready')
        self.assertEqual(b['tasks'][2]['status'], 'waiting')
    def test_wrong_worker_cannot_complete(self):
        a = m.run(self.root, self.now)
        self.submit(a['tasks'][0], worker='art')
        b = m.run(self.root, self.now)
        self.assertEqual(b['tasks'][0]['status'], 'invalid')
        self.assertEqual(b['tasks'][1]['status'], 'waiting')
    def test_future_or_stale_receipt_cannot_complete(self):
        a = m.run(self.root, self.now)
        for delta in [-1, 1]:
            self.submit(a['tasks'][0], submitted_at=(self.now + timedelta(days=delta)).isoformat())
            self.assertEqual(m.run(self.root, self.now)['tasks'][0]['status'], 'invalid')
    def test_path_escape_cannot_complete(self):
        a = m.run(self.root, self.now)
        self.submit(a['tasks'][0], artifacts=['../../config/webhooks.json'])
        self.assertEqual(m.run(self.root, self.now)['tasks'][0]['status'], 'invalid')
    def test_missing_output_cannot_complete(self):
        a = m.run(self.root, self.now)
        self.submit(a['tasks'][0])
        (self.root / a['tasks'][0]['expected_output']).unlink()
        self.assertEqual(m.run(self.root, self.now)['tasks'][0]['status'], 'invalid')

    def test_review_and_publish_gates(self):
        cfg = m.load(self.root / 'office/config.json')
        cfg['stage_workers'].update(video='art', review='general', publish='opportunity')
        m.save(self.root / 'office/config.json', cfg)
        a = m.run(self.root, self.now)
        for task in a['tasks'][:4]:
            self.submit(task)
        review = a['tasks'][4]
        self.submit(review)
        out = self.root / review['expected_output']
        m.save(out, dict(content_pass=True, sources_checked=True, rights_checked=False, platform_checked=True))
        self.assertEqual(m.run(self.root, self.now)['tasks'][4]['status'], 'invalid')
        m.save(out, dict(content_pass=True, sources_checked=True, rights_checked=True, platform_checked=True))
        self.assertEqual(m.run(self.root, self.now)['tasks'][5]['status'], 'blocked')
        cfg['publishing_policy'] = dict(enabled=True, charter_approved=True, channel='test-channel')
        m.save(self.root / 'office/config.json', cfg)
        self.assertEqual(m.run(self.root, self.now)['tasks'][5]['status'], 'ready')
        pub = a['tasks'][5]
        self.submit(pub)
        m.save(self.root / pub['expected_output'], dict(url='https://example.org/post'))
        self.assertEqual(m.run(self.root, self.now)['tasks'][6]['status'], 'ready')
    def test_symlink_cannot_complete(self):
        a = m.run(self.root, self.now)
        self.submit(a['tasks'][0])
        target = self.root / a['tasks'][0]['expected_output']
        target.unlink()
        target.symlink_to(self.root / 'office/config.json')
        self.assertEqual(m.run(self.root, self.now)['tasks'][0]['status'], 'invalid')

if __name__ == '__main__':
    unittest.main()
