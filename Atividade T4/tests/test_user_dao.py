from src.dao.user_dao import UserDAO
from src.models.user import User

users = UserDAO().get_instance().get_all()

for user in users:
    print(user)