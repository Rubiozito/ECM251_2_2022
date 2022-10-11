class Product():

    def __init__(self, name, price, descricao):
        self._name = name
        self._price = price
        self._descricao = descricao


    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_descricao(self):
        return self._descricao

    def __str__(self) -> str:
        return f'Product(name:{self.name}, price{self.price}, url:{self.url}'