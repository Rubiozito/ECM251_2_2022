from src.dao.user_dao import UserDAO

users = UserDAO.get_instance().get_all()

for user in users:
    print(user)