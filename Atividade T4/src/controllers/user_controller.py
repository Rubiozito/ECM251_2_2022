from src.models.user import User
from src.dao.user_dao import UserDAO

class UserController:

    def __init__(self) -> None:
        pass

    def get_user_by_email(self, email) -> User:
        return UserDAO().get_instance().get_by_email(email)

    def get_all_users(self) -> list:
        return UserDAO().get_instance().get_all()

    def insert_user(self, user: User) -> bool:
        return UserDAO().get_instance().insert(user)

    def update_user(self, user: User) -> None:
        UserDAO().get_instance().update(user)

    def delete_user(self, user: User) -> None:
        UserDAO().get_instance().delete(user)

    def search_user(self, name: str) -> list:
        return UserDAO().get_instance().search(name)