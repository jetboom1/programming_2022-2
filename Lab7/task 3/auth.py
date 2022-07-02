import hashlib

class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(self, username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExists(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass

class PermitError(Exception):
    pass

class NotLoggedIn(AuthException):
    pass

class User:
    def __init__(self, username, password):
        """Creating a new user. the password is encrypted before storing."""
        self.username = username
        self.password = self._encrypt_password(password)
        self.is_logged_in = False

    def _encrypt_password(self, password):
        return hashlib.sha256((password+self.username).encode()).hexdigest()

    def check_password(self, password):
        return self._encrypt_password(password) == self.password

    def __str__(self):
        return f'User {self.username}'

class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 0: #6
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise UsernameAlreadyExists(username)
        if not user.check_password(password):
            raise InvalidPassword(username, user)
        user.is_logged_in = True
        return True

    def logout(self, username):
        if username in self.users:
            self.users[username].is_logged_in = False
            return True
        return False

    def is_username_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False

class Authorizer:
    def __init__(self, authenticator):
        self.permissions = {}
        self.authenticator = authenticator

    def add_permission(self, perm_name):
        """Add a new permission to the permissions dictionary."""
        if perm_name not in self.permissions.keys():
            self.permissions[perm_name] = set()
        else:
            raise PermitError("Permission already exists")
    def permit_user(self, perm_name, username):
        """Grant the given permission to the user."""
        if perm_name not in self.permissions.keys():
            raise PermitError("Permission does not exist")
        if not username in self.authenticator.users.keys():
            raise InvalidUsername(username)
        if username not in self.permissions[perm_name]:
            self.permissions[perm_name].add(username)
        else:
            raise PermitError("User already has permission")
    def check_permission(self, perm_name, username):
        """Check if the user has permission."""
        if perm_name not in self.permissions.keys():
            raise PermitError("Permission does not exist")
        if not self.authenticator.is_username_logged_in(username):
            raise NotLoggedIn(username)
        if username in self.permissions[perm_name]:
            return True
        return False