import unittest
from ..challenge2 import access_control


class TestChallenge2(unittest.TestCase):
    def test_employees_with_access_both(self):
        self.assertEqual(access_control("E7642"),
                         "Access to both financial and technical data")

    def test_admin_access(self):
        self.assertEqual(access_control("E0001"),
                         "Access to both financial and technical data")

    def test_employees_with_access_only_finance_access(self):
        self.assertEqual(access_control("E1021"),
                         "Exclusive access to financial data")

    def test_employees_with_access_only_tech_access(self):
        self.assertEqual(access_control("E9812"),
                         "Exclusive access to technical data")


if __name__ == '__main__':
    unittest.main()
