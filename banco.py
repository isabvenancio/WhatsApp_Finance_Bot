import sqlite3

conn = sqlite3.connect("gastos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS gastos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor REAL,
    descricao TEXT,
    categoria TEXT,
    data TEXT
)
""")

conn.commit()
conn.close()

print("Banco criado!")