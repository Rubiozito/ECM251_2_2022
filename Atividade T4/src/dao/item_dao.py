import sqlite3
from src.models.item import Item

class ItemDAO:

    _instance = None

    def __init__(self):
        self._conn = sqlite3.connect()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ItemDAO()
        return cls._instance

    def connect(self):
        self.conn = sqlite3.connect('../databases/atividadeT4.sqlite')

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Itens;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Item(id=resultado[0], name=resultado[1], price=resultado[2], description=resultado[3]))
        self.cursor.close()
        return resultados

    def get_by_id(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Itens WHERE id = ?;
        """, (id))
        resultado = self.cursor.fetchone()
        self.cursor.close()
        return Item(id=resultado[0], name=resultado[1], price=resultado[2], description=resultado[3])

    def insert_item(self, item):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                INSERT INTO Itens (id, name, price, description)
                VALUES (?, ?, ?, ?);
            """, (item.get_id(), item.get_name(), item.get_price(), item.get_description()))
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def update_item(self, item):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            UPDATE Itens SET name = ?, price = ?, description = ? WHERE id = ?;
        """, (item.get_name(), item.get_price(), item.get_description(), item.get_id()))
        self.conn.commit()
        self.cursor.close()

    def delete_item(self, item):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            DELETE FROM Itens WHERE id = ?;
        """, (item.get_id()))
        self.conn.commit()
        self.cursor.close()

    def search_item(self, name):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Itens WHERE name LIKE ?;
        """, (name))
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Item(id=resultado[0], name=resultado[1], price=resultado[2], description=resultado[3]))
        self.cursor.close()
        return resultados