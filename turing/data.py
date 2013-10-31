import sqlite3


def load_data(filename):
    data = []
    
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    
    query = "SELECT state, symbol, state_new, symbol_new, action"
    query += " FROM action ORDER BY state"
    
    cursor.execute(query)
    
    for row in cursor:
        data.append(row)
    
    cursor.close()
    db.close()
    
    return data