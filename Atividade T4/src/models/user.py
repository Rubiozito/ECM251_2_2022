class User():
    
    def __init__(self, name, email, password, id_carrinho):
        self.name =  name
        self.email = email
        self.password = password
        self.id_carrinho = id_carrinho
         
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

    def get_id_carrinho(self):
        return self.id_carrinho

    def set_id_carrinho(self, id_carrinho):
        self.id_carrinho = id_carrinho