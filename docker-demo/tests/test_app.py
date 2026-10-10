import unittest

from app import response_for_path


class TestApp(unittest.TestCase):

    def test_homepage(self):
        self.assertEqual(
            response_for_path("/"),
            (200, "Hello from Docker + GitHub Actions!")
        )

    def test_health_endpoint(self):
        self.assertEqual(
            response_for_path("/health"),
            (200, "OK")
        )

    def test_unknown_path(self):
        self.assertEqual(
            response_for_path("/unknown"),
            (404, "Not found")
        )


if __name__ == "__main__":
    unittest.main()