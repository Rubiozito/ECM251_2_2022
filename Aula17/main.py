from item import Item
from carrinho import Carrinho


item1 = Item('Carregador','Carrega iphone e android', 200.0)

item2 = Item(valor=350, nome='Stray', descricao='Gato')

item3 = Item(valor=350, nome='Stray', descricao='Gato')

carrinho = Carrinho()

print(item1)
print(item2)

print(item1 == item2)
print(item1 == item1)
print(item2 == item3)

