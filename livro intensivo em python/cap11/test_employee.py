import unittest
from employee import Employee


class Empregado(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Leonam", "Cassemiro", 10000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.bill, 15000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.bill, 20000)


if __name__ == "__main__":
    unittest.main()
