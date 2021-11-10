import unittest
from app import app

class TestHelloWorld(unittest.TestCase):

    def test_status_ok(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='application/json')
        self.assertIsNotNone(response.json.get("status"))
        self.assertEqual(response.json.get("status"), 'OK')