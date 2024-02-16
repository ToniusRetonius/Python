import sqlite3

conn = sqlite3.connect("comercio.sqlite")

cursor = conn.cursor()

cursor.execute("CREATE TABLE productos (id INT, nombre TEXT, precio INT)")

objetos = ( (1, "Teclado", 500), (2, "Mouse", 600), (3, "Monitor", 6000), (4, "Parlantes", 3000) )

for i,n,p in objetos:
    cursor.execute("INSERT INTO productos VALUES(?,?,?)", (i,n,p))

conn.commit()
conn.close()