import unittest
import pyperclip
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    """test case that tests the behaviour of the credentials class methods."""

    def setUp(self):
        """method that sets up the credentials class before each test"""
        self.new_credentials = Credentials("twitter", "#twitterPASS")
    
    def test_init(self):
        """test to check if the object is initialized properly"""
        self.assertEqual(self.new_credentials.account_name, "twitter")
        self.assertEqual(self.new_credentials.password, "#twitterPASS")

    def test_save_credentials(self):
        """test to check if the credentials object is saved into the credentials list"""
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.accounts), 1)

    def test_save_multiple_credentials(self):
        """test to check if the save_multiple_credentials method saves multiple credentials"""
        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter", "#twitterPASS")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.accounts), 2)
        

    def tearDown(self):
        """method that cleans up after each test"""
        Credentials.accounts = []

    def test_display_credentials(self):
        """test to check if the display_credentials method returns the correct credentials"""
        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter", "#twitterPASS")
        test_credentials.save_credentials()
        self.assertEqual(Credentials.display_credentials(), Credentials.accounts)

    def test_display_all_credentials(self):
        """test to check if the display_all_credentials method returns all the saved credentials"""
        self.assertEqual(Credentials.display_credentials(), Credentials.accounts)

    def test_find_by_name(self):
        """test to check if the find_by_account_name method returns the correct credentials"""
        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter", "#twitterPASS")
        test_credentials.save_credentials()
        found_credentials = Credentials.find_by_name("twitter")
        self.assertEqual(found_credentials.password, test_credentials.password)

    def test_copy_credentials(self):
        """ test to check if the copy_credentials method copies the correct credentials"""
        self.new_credentials.save_credentials()
        Credentials.copy_credentials("twitter")
        self.assertEqual(self.new_credentials.password, pyperclip.paste())
        

# test runner
if __name__ == '__main__':
    unittest.main()