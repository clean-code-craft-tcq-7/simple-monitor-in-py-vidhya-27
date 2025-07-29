import unittest
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):
    def vital_are_ok(self):
      self.assertTrue(vitals_ok(98, 72, 99))
      self.assertTrue(vitals_ok(102, 100, 90)) #boundary conditions test
      self.assertTrue(vitals_ok(95, 60, 90)) #boundary conditions test
    def vital_not_ok(self):
       self.assertFalse(vitals_ok(105, 120, 80))
       self.assertFalse(vitals_ok(103, 101, 89)) #boundary conditions test
       self.assertFalse(vitals_ok(94, 59, 89))
       


if __name__ == '__main__':
  unittest.main()
