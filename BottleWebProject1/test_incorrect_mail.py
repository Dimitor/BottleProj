import unittest
import checkers

class StringTestCase(unittest.TestCase):
    def setUp(self):
        self.data = ["", "1", "m1@", "@mail", "gmail@some", "mail@hmm@ftp.com", "mail.gd@gm.cl", "some@mail..ru", "some@.any", "some @mail.su", "some@many.","some@mail.com.many"]
    def test_incorrect(self):
        for i in self.data:
            self.assertFalse(checkers.check_mail(i))

if __name__ == '__main__':
    unittest.main()