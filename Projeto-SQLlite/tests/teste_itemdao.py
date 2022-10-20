from src.dao.item_dao import ItemDAO

items = ItemDAO.get_instance().get_all()

for item in items:
    print(item)

item = ItemDAO.get_instance().pegar_item("OLA1")
item.nome = "NVIDIA RTX40490"
item.preco = 13500
print(ItemDAO.get_instance().atualizar_item(item))