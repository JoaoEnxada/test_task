import unittest
from smartcut import SmartCut


class TestCutter(unittest.TestCase):
    def setUp(self):
        self.cutter = SmartCut()
    
    # Case for string with 25 symbols
    def test_25_symbols(self):
        self.assertEqual(self.cutter.cut('Hello, my name is Arsenij'), 'Hello, my name is Arsenij')

    # Case for string with less than 25 symbols
    def test_under_25_symbols(self):
        self.assertEqual(self.cutter.cut('These donuts are wow!'), 'These donuts are wow!')

    # Case for string with more than 25 symbols
    def test_upper_25_symbols(self):
        self.assertEqual(self.cutter.cut('This text contains more than 25 symbols!'), 'This text contains more...')

    # Case for string with more than 25 symbols, where 25th symbol is "!" or "?"
    def test_upper_25_symbols_25th_is_interrobang(self):
        self.assertEqual(self.cutter.cut("Hello, my name is Marina! Here's my new course, check it out!"),
                         "Hello, my name is Marina!...")

    # Case for string with more than 25 symbols, where 25th symbol is ".", "," or " "
    def test_upper_25_symbols_25th_is_dot(self):
        self.assertEqual(self.cutter.cut("Hello, my name is Marina, here's my new course, check it out!"),
                         "Hello, my name is Marina...")


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
