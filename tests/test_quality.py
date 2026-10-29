import hashlib
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'office'))
from quality import validate_sources, validate_review

class QualityTest(unittest.TestCase):
    def setUp(self):
        self.now = datetime.fromisoformat('2026-10-29T16:00:00+07:00')
    def test_booleans_without_evidence_do_not_pass(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'video.mp4'; p.write_bytes(b'test fixture')
            with self.assertRaises(ValueError):
                validate_review({'content_pass':True,'rights_checked':True},'reviewer',['creative','production'],p,'video.mp4',self.now)
    def test_unknown_claim_source_rejected(self):
        data={'sources':[{'id':'S1','url':'https://example.org','publisher':'Test','title':'Fixture','kind':'primary','retrieved_at':self.now.isoformat(),'verification':'checked','evidence_locator':'Section 1'}], 'claims':[{'id':'C1','statement':'Test','source_ids':['MISSING'],'support':'direct','verified_by':'radar','checked_at':self.now.isoformat()}]}
        with self.assertRaises(ValueError): validate_sources(data,self.now)
    def test_self_review_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'video.mp4'; p.write_bytes(b'test fixture')
            with self.assertRaises(ValueError): validate_review({'reviewer':'art'},'art',['art'],p,'video.mp4',self.now)
    def test_video_changed_after_review_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'video.mp4'; p.write_bytes(b'new version')
            data={'reviewer':'qa','checked_at':self.now.isoformat(),'decision':'pass','risk':'green','issues':[], 'reviewed_artifacts':[{'path':'video.mp4','sha256':hashlib.sha256(b'old version').hexdigest()}]}
            with self.assertRaises(ValueError): validate_review(data,'qa',['art','production'],p,'video.mp4',self.now)

if __name__=='__main__': unittest.main()
