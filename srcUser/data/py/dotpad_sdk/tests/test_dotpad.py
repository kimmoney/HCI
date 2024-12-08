import unittest
from dotpad.bindings import DotPad

class TestDotPad(unittest.TestCase):
    def test_initialization(self):
        dp = DotPad(port_number=1, device_type=0)
        self.assertEqual(dp.error_code, 0)

    def test_display_file(self):
        dp = DotPad(port_number=1, device_type=0)
        result = dp.display_file("example.dtm")
        self.assertEqual(result, 0)
        dp.deinit()
