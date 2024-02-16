import time

def convertir(valor):
    while True:
        try:
            valor = float(valor)
            break
        except ValueError:
            print("Valor no valido!")
        valor = input("Ingrese nuevamente: ")
    return valor

def verificar(dato):
    while dato == "":
        print("Error! Campo vacio ")
        dato = input("Ingrese nuevamente el dato: ")
    return dato

def yesno(respuesta):
    while respuesta.lower() != "y" and respuesta != "n":
        print("Error!")
        respuesta = input("Ingrese unicamente y / n: ")  
    return respuesta

def guardar(persona, indice, legajo):
    fecha = time.asctime()
    f = open(legajo + ".txt", "a")
    f.write(fecha + "" + persona + "" + str(indice) + "\n")
    f.close()
    print("Evento salvado")

def leer(socio):
    try:
        f = open( socio + ".txt", "r")
        data = f.read()
        f.close()
        print(data)
    except FileNotFoundError:
        print("No se encuentra el socio " + socio)

""" ALT + SHIF + A para realizar comentarios """
""" La funcion ayuda sirve para transmitir cuales son las herramientas con las que cuenta nuestro modulo """
def ayuda():
    print("""
    1 - 
    """)