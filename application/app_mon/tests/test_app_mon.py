import unittest

import app_mon


class App_monTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app_mon.app.test_client()

    def test_index(self):
        rv = self.app.get("/")
        self.assertIn("Welcome to Application Monitoring Demo", rv.data.decode())


if __name__ == "__main__":
    unittest.main()
