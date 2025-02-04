import unittest
from ..challenge1 import simplify


class TestChallenge1(unittest.TestCase):
    def test_correct_login_credentials(self):
        self.assertEqual(simplify(True, True), "Access granted")

    def test_incorrect_login_credentials(self):
        self.assertEqual(simplify(False, True), "Access blocked")


if __name__ == '__main__':
    unittest.main()
