from src.models.item import Item
from src.dao.item_dao import ItemDAO

class Item_controller:
    def __init__(self) -> None:
        pass

    def pegar_item(self, id) -> Item:
        item = algo()
        return item

    def inserir_item(self, item) -> None:
        algo2(item)

    def pegar_todos_itens(self) ->list[Item]:
        itens = ItemDAO.get_instance().get_all()
        return itens