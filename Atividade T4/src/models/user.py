class User():
    
    def __init__(self, name, email, password):
        self.name =  name
        self.email = email
        self.password = password
         
    def __str__(self):
        return f"User: {self.name}, {self.email}"
    
    def get_password(self):
        return self.password
    
    def set_password(self, password):
        self.password = password

    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def set_name(self, name):
        self.name = name
