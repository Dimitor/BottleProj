import unittest
import checkers

bad_phones = ["", "9999", "+81223424124143241243123", "+565 ((334)-344-43-34", "84f56433345", "-+9345671234", "+7 (955) 234---53-34"];

class Test_test_correct_phone(unittest.TestCase):
    def test_A(self):
        for i in bad_phones:
            self.assertFalse(checkers.check_phone(i))

if __name__ == '__main__':
    unittest.main()
