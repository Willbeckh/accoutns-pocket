# create user class here
class User:
    """creates new instaces of User."""
    user_account = [] # user accounts db
    
    def __init__(self, username, login):
        """"defines properties for our subject
        Args:
            username: for identifying a user
            login: a password for a user account
        """
        self.username = username
        self.login = login

    def new_user(self):
        return f'Success: { self.username } - { self.login }'

    def save_user(self):
        """saves user account to user_account list"""
        User.user_account.append(self)
        return self

    @classmethod
    def display_users(cls):
        """Displays a list of all available users"""
        cls.user_account
        return cls.user_account
        