import unittest
import sys
sys.path.append("..") # allows use of following import statement

from e4stypes.user import User

class TestExample(unittest.TestCase):

    def test_get_email(self):
        email = "billyfoshilly2000@aol.net"
        example_user = User("billybobjr", email, "billysworld")
        self.assertEqual(email, example_user.get_email())

if __name__ == "__main__":
    unittest.main()