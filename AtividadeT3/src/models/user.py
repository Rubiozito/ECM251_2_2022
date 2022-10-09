class User():

    def __init__(self, name, email, password ):
        self._name = name
        self._email = email
        self._password = password

    def login(self, email_login, password_login):
        if email_login == self._email & password_login == self._password:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f'User (name:{self.name}, email:{self.email}, password:{self.password})'

    def get_name(self):
        return self._name

    def get_password(self):
        return self._password

    def get_email(self):
        return self._email

    