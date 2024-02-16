############# CLASE 2 ############# 
#   Time ; os y sys son librerias

import time 
import os
import sys

for n in range(10, -1, -1):
    print(n)
    time.sleep(1)


def verificar(dato):
    while dato == "":
        print("Error! Campo vacio ")
        dato = input("Ingrese nuevamente el dato: ")
    return dato

def guardar(persona, tipo):
    fecha = time.asctime()
    f = open("control.txt", "a")
    f.write(fecha + "" + persona + "" + tipo + "\n")
    # \n hace un salto de linea
    f.close()
    print("Evento salvado")

def leer():
    f = open("control.txt", "r")
    datos = f.read()
    f.close()
    print(datos)


while True:
    print(""" 
    1 - Ingreso
    2 - Egreso
    3 - Ver eventos
    4 - Salir del sistema
    """)
    opcion = input(" >>> ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del visitante que ingresa: ")
        nombre = verificar(nombre)
        guardar(nombre, "ingreso")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del visitante que sale: ")
        nombre = verificar(nombre)
        guardar(nombre, "egreso")
    elif opcion == "3":
        leer()
    elif opcion == "4":
        print("Gracias por usar nuestro programa")
        break
    else:
        print("Error de opcion!")
    input('Toque ENTER para continuar...')
    os.system("cls")

# La manera correcta de cerrar el programa es a traves de >>>
sys.exit()


