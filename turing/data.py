import sqlite3


class TableData(object):

    def __init__(self, filename):
        self.data = []
        
        db = sqlite3.connect(filename)
        cursor = db.cursor()
        
        query = "SELECT state, symbol, state_new, symbol_new, action"
        query += " FROM action ORDER BY state"
        
        cursor.execute(query)
        
        for row in cursor:
            self.data.append(row)
        
        cursor.close()
        db.close()
        
        
    def __call__(self):
        return self.data