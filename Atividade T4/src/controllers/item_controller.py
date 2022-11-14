from models.item import Item

class ItemController():
    
    def __init__(self)-> None:
        pass 

    def get_all(self):
        return ItemDAO().get_instance().get_all()

    def get_by_id(self, id):
        return ItemDAO().get_instance().get_by_id(id)
     
    def insert_item(self, item):
        return ItemDAO().get_instance().insert_item(item)

    def update_item(self, item):
        return ItemDAO().get_instance().update_item(item)       

    def delete_item(self, id):
        return ItemDAO().get_instance().delete_item(id)
     
    def search(self, name):
        return ItemDAO().get_instance().search(name)