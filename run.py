#!/usr/bin/env python3.8
import os
from user import User
from credentials import Credentials
import random, string

def create_user(username, login):
    """"Creates a new user account"""
    new_user = User(username, login)
    return new_user

def save_new_user(account):
    """Saves a new user to the user object"""
    return account.save_user()

def display_users(password):
    """Displays all saved accounts"""
    return User.display_users(password)

def generate_password(pass_length=8):
    """Method to generate random passwords"""
    while True:
        try:
            # REQUEST USER FOR PASS LENGTH
            pass_length = int(input("Input password length(min 8): "))

        except ValueError:
            print("Oops, you did not provide a number!")
            print("try again!")

        else:
            # join all items to form a password
            combinedChars = string.ascii_letters+ string.digits + string.punctuation

            passcode = ''
            if pass_length < 8:
                print("password length is too small!")
            # elif pass_length > 16:
            #     print("password length cannot be more than 16 characters.")
            #     print("-"*10)
            else: 
                for lentgh in range(pass_length):
                    passcode += random.choice(combinedChars)
                print(f"Your passcode is: {passcode}")
                return passcode

# credentials code
def create_account(account_name, password):
    """Creates a new account"""
    new_credentials = Credentials(account_name, password)
    return new_credentials

def create_credentials(details):
    """Saves a new credentials to the credentials object"""
    return details.save_credentials()
    
def delete_account_credentials(details):
    """Deletes a users account credentials
    """
    return details.delete_credentials()

def find_credentials(account):
    """Method to find a user's credentials"""
    return Credentials.find_by_name(account)

def display_credentials():
    """
    Returns all the saved account credentials.
    """
    return Credentials.display_credentials()

def copy_credentials(account_name):
    """Copy credentials to the clipboard
    """
    return Credentials.copy_credentials(account_name)

# main app runner
def main():
    os.system("clear")

    print("Hello! Welcome to Password Locker.\n Use command: c - to create account, q - to quit")
    while True:
        short_code = input("type code: ").lower()

        if short_code == 'c':
            print("Create account")
            print("-"*10)

            username = input("Please provide your username: ")
            if username == '':
                username = input("Please enter a username: ")
                print("-"*10)
            else: 
                print("-"*10)
                answer = input("would you like to generate a password? y/n? ").lower()
                password = ''
                if answer == 'y':
                    password = generate_password()
                
                elif answer == 'n':
                    password = input("Please provide your password: ")
            
                created_user = save_new_user(create_user(username, password))
                print("\n")
                print(f"Account Created Successfully: username: {username} - passcode: {password}")
                print("-"*10)
                print("\n")
                break
            
        elif short_code == 'q':
            print("Goodbye!")
            # ! this doesn't quit the app, just termintates the first while loop
            # TODO: make the code to close app.
            break
        
        elif short_code != 'c':
            print("please use available commands: c - to create account or e - to exit")
              
        # TODO: hide codes for interacting with locker if user is not authenticated
           
    # adding credentials
    while True:
        print("Use below codes: \n ca - create an account \n dc - display credentials \n fc - find account credentials \n d - to delete account credentials \n q - exit the application \n")

        short_code = input("type code: ").lower()
        if short_code == 'ca':
            print("New account")
            print("-"*10)
            account_name = input("Account name: ")
            
            choice = input("would you like to generate a password? Y/n .").lower()
            if choice == 'y':
                password = generate_password()
            else:
                password = input("Please create a password: ")
                
            create_credentials(create_account(account_name, password))
            print('-'*10)
            print(f"New account '{account_name}' created.")
            print('-'*10)
            print('\n')
       
        # display credentials
        elif short_code == 'dc':
            print("-"*10)
            print("\n")
                 
            if display_credentials():
                print("--- CREDENTIALS ---")

                for credentials in display_credentials():
                    print(f"Account: {credentials.account_name} - Password: {credentials.password}")
                print('-'*10)
                print("\n")
                
            else:
                print("You don't seem to have any credentials saved yet")
                print('\n') 
   
        # search for accounts
        elif short_code == 'fc':
            # NOTE: GET account using acc_name
            credentials = input("Enter the account name to search for: ")
            print('-'*10)
            # NOTE: condtion to check if account exists
            if display_credentials(): # displays all contacts available
                # NOTE: if account exists, display credentials
                result = find_credentials(credentials)
                print(f"Account name: {result.account_name}")
                print(f"password: {result.password}")
                print('-'*10)
                print("\n")
                
            else:
                print("*"*10)
                print("You don't seem to have any credentials saved yet")
                print('\n')

        # delete credentials.
        elif short_code == 'd':
            credentials = input("Enter the account name you want to search for: ")
            print("*"*10)
            if display_credentials():
                response = find_credentials(credentials)
                response.delete_credentials()
                print("successfully deleted an account")
            else:
                print("Cannot find an account with that name.")
                
            print("*"*10)
            print("\n")
            # pass
        
        # TODO: copy a password
        
        elif short_code == 'q':
            print("\n")
            print("****** Safely exiting the application ******")
            print("\n")
            break
        
# run the app
if __name__ == '__main__':
    main()
    
    
