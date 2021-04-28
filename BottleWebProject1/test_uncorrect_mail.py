import unittest
import test_mail

class StringTestCase(unittest.TestCase):
    def setUp(self):
        self.data = ["", "1", "m1@", "@mail", "gmail@some","mail@hmm@ftp.com"]
    def test_uncorrect(self):
        for i in self.data:
            self.assertFalse(test_mail.check_mail(i))

if __name__ == '__main__':
    unittest.main()