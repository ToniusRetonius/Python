import sqlite3

""" Creamos una interfaz (API) para poder manipular con Python, ua base de datos """

""" CONN es un conector a la base de datos """

""" CURSOR  """

conn = sqlite3.connect("ejemplo.sqlite")

try:
    cursor = conn.cursor()
except sqlite3.OperationalError:
    print("Bienvenido nuevamente!")

""" Ejecuto y creo una TABLE """
cursor.execute("CREATE TABLE personas (id INT, nombre TEXT, edad INT)")

""" Cargamos datos desde Python : creo una tupla con datos """
datos = ((1),("Robert"),(40),(2),("Jaz"),(20),(3),("Romi"),(21) )

""" Recorro la tupla con un for para insertar los valores """
# ? representa un parametro
for aux in datos:
    cursor.execute("INSERT INTO personas VALUES (?,?,?)",aux)

""" o ... con  UNPACKING>>> """
for i,n,e in datos:
    cursor.execute("INSERT INTO personas VALUES (?,?,?)",(i,n,e))


cursor.execute("SELECT * FROM personas")

""" el FETCHALL me permite capturar informacion SQL para manipularla en Python. Tengo que hacer la consulta y con eso, la traigo a Python """
tabla = cursor.fetchall()

""" El COMMIT guarda los cambios """
conn.commit()

""" El CLOSE termina de guardar los cambios """
conn.close()


""" Inyeccion SQL es una manera de insertar un dato con una sentencia maliciosa """