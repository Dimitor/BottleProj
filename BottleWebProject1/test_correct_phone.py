import unittest
import checkers

bad_phones = ["+79999999999", "+546-993-536-77-33", "+812234241241", "+5 (334)-344-43-34", "84564333457", "+9 (345) 671-23-44", "+7 (955)-234-53-34"];

class Test_test_correct_phone(unittest.TestCase):
    def test_A(self):
        for i in bad_phones:
            self.assertTrue(checkers.check_phone(i))

if __name__ == '__main__':
    unittest.main()
