import sqlite3
from src.models.user import User

class UserDAO():

    _instance = None

    def __init__(self)-> None:
        self.connect()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = UserDAO()
        return cls._instance

    def connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db')

    def get_all():
        self.cursor = self.conn.cursor()
        self.cursor.execute("""SELECT * FROM Users;""")
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(name=resultado[0], email=resultado[1], password=resultado[2], id_carrinho=resultado[3]))
        self.cursor.close()
        return resultados

    def get_by_email(self, email):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""SELECT * FROM Users WHERE email = ?;""", (email,))
        resultado = self.cursor.fetchone()
        self.cursor.close()
        return User(name=resultado[0], email=resultado[1], password=resultado[2], id_carrinho=resultado[3])

    def insert(self, user):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""INSERT INTO Users VALUES (name, email, password);""", (user.get_name(), user.get_email(), user.get_password()))
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def update(self, user):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""UPDATE Users SET name = ?, email = ?, password = ? WHERE email = ?;""", (user.get_name(), user.get_email(), user.get_password(), user.get_email()))
        self.conn.commit()
        self.cursor.close()

    def delete(self, user):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""DELETE FROM Users WHERE email = ?;""", (user.get_email(),))
        self.conn.commit()
        self.cursor.close()