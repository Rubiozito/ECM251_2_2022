class Carrinho():

    def __init__(self, quantidade, id):
        self.quantidade = quantidade
        self.id = id
    
    def __str__(self):
        return f"Carrinho: {self.quantidade}, {self.id}"

    def get_quantidade(self):
        return self.quantidade

    def get_id(self):
        return self.id

    def set_quantidade(self, quantidade):
        self.quantidade = quantidade