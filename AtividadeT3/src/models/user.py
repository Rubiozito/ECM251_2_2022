class User():

    def __init__(self, name, email, password ):
        self._name = name
        self._email = email
        self._password = password

    def __str__(self) -> str:
        return f'User (name:{self.name}, email:{self.email}, password:{self.password})'

    def get_name(self):
        return self._name

    def get_password(self):
        return self._password

    def get_email(self):
        return self._email

    