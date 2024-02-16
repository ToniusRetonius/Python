### Clase 7 ###

##  COLECCIONES ##

    #   LISTAS
    clientes = ["nombre1","nombre2","nombre3"]

    #   TUPLA (inmutable)
    #   sirven para enviar datos inmutables entre usuario-servidor
    varios = ("Python", True, 120)

    #   DICCIONARIOS (elementos no-indexados)
    #   pares (clave : valor)
    cliente = ("Nombre":"Mateo", "Edad":19, "Cuit":203020102)

    # se puede agregar un par clave:valor >>>
    ciente["Direccion"] = "San Martin 200"

    # se puede borrar un par clave:valor >>>
    del cliente["Direccion"]


## LABORATORIO ##
def rango(inicio, fin, intervalo) :
        resultado = []
        while inicio < fin :
            resultado.append(inicio)
            inicio = inicio + intervalo
        return resultado

print(rango(1,20,3))

## LABORATORIO ##
def estrellas(cantidad):
    for i in range(0, cantidad + 1):
        print("*" * i) 
estrellas(5)


## OPERADORES DE PERTENENCIA ##

    # IN (nos permite saber si un elemento pertenece a un array,... )
    # devuelve un boolean

    print("john" in clientes)
    
    # NOT IN 
    print("john" not in clientes)
    
