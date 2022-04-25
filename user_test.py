import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        """method that sets the instructions that run before each test"""
        self.new_user = User("billy", "#Pass123")
    
    def test_init(self):
        self.assertEqual(self.new_user.username, "billy")
        self.assertEqual(self.new_user.login, "#Pass123")

    def tearDown(self):
        """Method to clean up after each test case."""
        User.user_account = []


    def test_save_user(self):
        """test_save_user test case to test if the user object is saved into the user list"""
        self.new_user.save_user()
        self.assertEqual(len(User.user_account), 1)

    def test_display_users(self):
        """"test_display_users test case to display a list of availbale users"""

        


if __name__ == '__main__':
    unittest.main()