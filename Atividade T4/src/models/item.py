class Item():

    def __init__(self, id, name, price, description):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        
    def __str__(self):
        return f"Item: {self.id}, {self.name}, {self.price}, {self.description}"

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price   

    def get_description(self):
        return self.description 

    
    