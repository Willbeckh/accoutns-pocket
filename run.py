#!/usr/bin/env python3.8
from user import User
import random, string

def create_user(username, login):
    """"Creates a new user account"""
    new_user = User("billy", "#Pass123")
    return new_user

def save_user(account):
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
            for length in range(pass_length):
                passcode += random.choice(combinedChars)
            print(f"Your passcode is: {passcode}")
            break

# credentials code
def create_account(account_name, password):
    """Creates a new account"""
    new_credentials = Credentials("twitter", "#twitterPASS")

def save_credentials(credentials):
    """"""
    
    
