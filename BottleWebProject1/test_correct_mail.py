import unittest
import test_mail

class StringTestCase(unittest.TestCase):
    def setUp(self):
        self.data = ["mm@mail.ru", "m1@gmail.com", "somemail@domain.any.com"]
    def test_correct(self):
        for i in self.data:
            self.assertTrue(test_mail.check_mail(i))
if __name__ == '__main__':
    unittest.main()