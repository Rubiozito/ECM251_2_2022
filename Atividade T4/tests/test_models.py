from src.models.user import User
from src.models.item import Item

user1 = User(name="user1", email="user1email", password="user1password")
item1 = Item(id= "001", name="item1", price=1.0, description="item1description")

print(user1)
print(item1)