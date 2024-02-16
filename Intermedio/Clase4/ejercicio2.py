import sqlite3
import os


def verificar(dato):
    while dato == "":
        print("Error de dato vacio")
        dato = input("Ingrese nuevamente: ")
    return dato

def convertir(valor):
    while True:
        try:
            valor = int(valor)
            break
        except ValueError:
            print("Error! Solo enteros")
        valor = input("Ingrese nuevamente")
    return valor


def guardar(i,n,p):
    conn = sqlite3.connect("comercio.sqlite")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO productos VALUES(?,?,?)", (i,n,p))
    except sqlite3.OperationalError:
        cursor.execute("CREATE TABLE productos (id INT, nombre TEXT, precio INT )")
        cursor.execute("INSERT INTO productos VALUES (?,?,?)", (i,n,p))
    conn.commit()
    conn.close()


def ver():
    conn = sqlite3.connect("comercio.sqlite")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()
        for n in datos:
            print(n[0], " | ", n[1], " | ", n[2], " | ")
    except sqlite3.OperationalError:
            print("No existe la tabla productos")
   
##########################

os.system("cls")

while True:
    print(" 1 - Agregar producto")
    print(" 2 - Ver productos")
    print(" 3 - Salir")

    opcion = input(">>>")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        nombre = verificar(nombre)

        precio = input("Ingrese precio: ")
        precio = convertir(precio)

        codigo = input("Ingrese codigo del producto")
        codigo = convertir(codigo)

        guardar(codigo, nombre, precio)
    
    elif opcion == "2":
        ver()
    elif opcion == "3":
        print("Gracia por utilizar el programa!")
        break
    else:
        print("Error de opcion")
    
    input("Toque enter para continuar...")
    os.system("cls")



"""  pass
# el pass es para que no salte error en un lugar que voy a llenar luego
#agregar producto a base de datos """