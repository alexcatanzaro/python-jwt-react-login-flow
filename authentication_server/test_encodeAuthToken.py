import unittest
from server import encodeAuthToken;

groups = ["user1, user2, admin"]
user_id = 'alex_cat'

class EATTestCase(unittest.TestCase):

    def test_is_EAT_valid(self):
        self.assertTrue(encodeAuthToken(user_id, groups))

if __name__ == "__main__":
    unittest.main()
