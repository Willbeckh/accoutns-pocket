#!/usr/bin/env python3.8
from user import User
from credentials import Credentials
import random, string

def create_user(username, login):
    """"Creates a new user account"""
    new_user = User("billy", "#Pass123")
    return new_user

def save_new_user(account):
    """Saves a new user to the user object"""
    account.save_user()

def generate_password():
    """Method to generate random passwords"""
    CHARS = string.ascii_letters
    DIGITS = string.digits
    SYMBOLS = string.punctuation


    while True:
        try:
            # REQUEST USER FOR PASS LENGTH
            pass_length = int(input("Please provide the length of the password (min 8, max 16): "))

        except ValueError:
            print("Oops, you did not provide a number!")
            print("try again!")

        else:
            # join all items to form a password
            combinedChars = CHARS + DIGITS + SYMBOLS

            passcode = ''
            if pass_length < 8:
                print("password length is too small!")
            elif pass_length > 16:
                print("password length cannot be more than 16 characters.")
            else: 
                for lentgh in range(pass_length):
                    passcode += random.choice(combinedChars)
                print(f"Your passcode is: {passcode}")
                break

# credentials code
def create_account(account_name, password):
    """Creates a new account"""
    new_credentials = Credentials("twitter", "#twitterPASS")

def create_credentials(details):
    """Saves a new credentials to the credentials object"""
    details.save_credentials()
    
def delete_credentials(details):
    """Deletes a users account credentials
    """
    details.delete_credentials()

def find_credentials(account):
    """Method to find a user's credentials"""
    return Credentials.find_by_name(account)

def display_credentials(account_name):
    """Finds available accounts by account name
    Returns:
        the contact
    """
    return Credentials.find_by_name(account_name)

def copy_credentials(account_name):
    """Copy credentials to the clipboard
    """
    return Credentials.copy_credentials(account_name)

# main app runner
def main():
    print("Hello! Welcome to Password Locker. What is your name? ")
    user_name = input()
    print(f"Hello {user_name}. What would you like to do?")
    print('\n')

    while True:
        print("Here are available codes: \n ca - create an account \n dc - display credentials \n fc - find account credentials \n  ex - exit the application \n")
    
        short_code = input().lower()
        if short_code == 'ca':
            print("New account")
            print("-"*10)

            print("Account name: ")
            account_name = input()

            print("Password: ")
            password = input()

            save_new_user(create_user(user_name, password))
            print('\n')
            print(f"New account '{account_name}' created successfully")
            print('\n')

        

# run the app
if __name__ == '__main__':
    main()
    
    
