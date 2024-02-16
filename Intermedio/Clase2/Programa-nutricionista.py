# Creamos un programa para un nutricionista ..

import time
import os

from modulo import *

#from modulo import (nombre de la funcion)


############################

while True:
    print("""
    1- Ingreso de paciente a historia clinica
    2- Ver historia clinica
    3- Salir del programa
    """)
    opcion = input(" >>> ")
    if opcion == "1":

        peso = input("Ingrese su peso(kg): ")
        peso = convertir(peso)

        altura = input("Ingrrese su altura(m): ")
        altura = convertir(altura)

        nombre = input("Ingrese su nombre: ")
        nombre = verificar(nombre)

        credencial = input("Ingrese su Nro. de credencial: ")
        credencial = verificar(credencial)

        imc = peso / (altura**2)
        imc = round(imc, 2)

        print(f"{nombre} tiene un imc de {imc}")
        print(f"Desea guardar los datos de {nombre}?")

        opcion = input(" 'Y' para guardar, 'N' para no guardar: ")
        opcion = yesno(opcion)

        if opcion == "y":
            # guardo los datos
            guardar(nombre,imc, credencial)
        else:
            print("No guardado!")

    elif opcion == "2":
        credencial = input("Ingrese nro. de credencial del socio: ")
        credencial = verificar(credencial)
        leer(credencial)

    elif opcion == "3":
        print("Gracias por usar el programa!")
        break
    else:
        print("Error de opcion!")
        input("Toque ENTER para reiniciar")
        os.system("cls")



