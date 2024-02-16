import requests
import os


if os.name == "nt":
    borrar = "cls"
else:
    borrar = "clear"

while True:
    print("""
    1 - Variables climaticas
    2 - Predecir clima
    3 - Salir del programa
    """)

    opcion = input(" >>> ")

    if opcion == "1":
        r = requests.get("http://wttr.in/Buenos%20Aires,AR?format=j1")
        
        if r.status.code == 200:
            datos = r.json()
            print("Temperatura actual", datos["current condition"][0]['temp_C'])
            print("Humedad actual", datos["current condition"][0]['humidity'])
            print("Presion", datos["current condition"][0]['pressure'])
        else:
            print("Servicio no disponible!")
    
    elif opcion == "2":
        
        r = requests.get("http://wttr.in/Buenos%20Aires,AR?format=j1")
        
        if r.status.code == 200:
            datos = r.json()
            h = float(datos["current condition"][0]['humidity'])
            p = float(datos["current condition"][0]['pressure']) 

            if h > 80 and p < 1013:
                print("Lluvia cerca!")
            else:
                print("No hay posibilidad de lluvia")

    elif opcion == "3":
        print("Gracias por utilizar nuestro programa!")
        break
    else:
        print("Error de opcion")
    
    input("Toque ENTER para continuar...")
    os.system(borrar)    

