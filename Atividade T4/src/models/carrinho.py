class Carrinho():

    def __init__(self, quantidade, id):
        self.quantidade = quantidade
        self.id = id
    
    def __str__(self):
        return f"Carrinho: {self.quantidade}, {self.id}"