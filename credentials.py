# credentials class object
import pyperclip

class Credentials:
    """Class that defines the properties and methods for account credentials"""
    accounts = [] # accounts db

    def __init__(self, account_name, password):
        """this initializes the properties for our class/object
        Args:
            account_name: the name of the account
            password: the password for the account
        """
        self.account_name = account_name
        self.password = password


    def save_credentials(self):
        """method that saves credentials objects into the credentials list"""
        return Credentials.accounts.append(self)

    def delete_credentials(self):
        """method that deletes a saved credentials from the credentials list"""
        return Credentials.accounts.remove(self)

    @classmethod
    def find_by_name(self, name):
        """method that takes in a name and returns a credentials that matches that name
        Args:
            name: name to search for
        Returns:
            Credentials of account that matches the name.   
        """
        for credentials in Credentials.accounts:
            if credentials.account_name == name:
                return credentials

    @classmethod
    def display_credentials(cls):
        """method that returns the credentials list"""
        return cls.accounts

    @classmethod
    def copy_credentials(cls, account_name):
        """method that copies a credentials password to the clipboard
        Args:
            account_name: name of the account to copy
        """
        credentials_found = Credentials.find_by_name(account_name)
        pyperclip.copy(credentials_found.password)

