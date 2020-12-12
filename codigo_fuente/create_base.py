import sqlite3
conn = sqlite3.connect('archivos/base/database.db')
c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS registro(usuario TEXT, clave TEXT)')
    conn.commit()
    c.close()
    conn.close()
create_table()