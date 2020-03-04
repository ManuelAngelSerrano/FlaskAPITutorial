import sqlite3

class dbBroker:
    db = './tasks.db'

    def __init__(self):
        self.conn = sqlite3.connect(self.db)
        self.conn.row_factory = self.dict_factory
        self.cursor = self.conn.cursor()

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
    
    def query(self, consulta):
        return self.cursor.execute(consulta).fetchall()

    def execute(self, consulta):
        self.cursor.execute(consulta)
        self.cursor.commit()
