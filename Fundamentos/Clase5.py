### CLASE 5 ###

## LABORATORIO ##

longitud = int(input("Ingrese la longitud de la lista: "))
lista = []

while len(lista) < longitud :
    dato = int(input("Ingrese un dato: "))
    lista.append(dato)
    
print("Los datos de la lista son: ", lista)

### BUCLE  ###

    # El for se repite tantas veces como elemento haya en la lista
    clientes = ["Mateo", "Silvia", "Lucia"]

    # AUX es una variable auxiliar que contiene cada uno de los
    # elementos a medida que los recorre, en gral usamos el
    # singular del nombre de la lista
    # IN determina en que lista voy a ejecutar el bucle for
    
        #for aux in lista :
        #    print(...)
    for cliente in clientes :
        print(cliente)

    # Puedo definir una lista dentro del for
    for aux in [1,2,3,4,5,6,7,8,9,10]:
        print(aux)

    # Range: es una funcion en la que defino
    # range(inicio, fin) ...
    # esta funcion comienza en "inicio" y finaliza
    # en "FIN" - 1
    
    print(list(range(1,11))) 

### LABORATORIO ###
    longitud = int(input("Ingrese la longitud de la lista: "))
    lista = []

    while len(lista) < longitud :
        dato = int(input("Ingrese un dato: "))
        lista.append(dato)
        if dato % 3 :
            print("Fizz!")
        elif dato % 5:
            print("Buzz")
        else:
            print("FizzBuzz")

    print(lista)

### LABORATORIO ###
    longitud = int(input("Ingrese la longitud de la lista: "))
    lista = []

    while len(lista) < longitud :
        dato = int(input("Ingrese un dato: "))
        lista.append(dato)
       
    for dato in lista:
        if dato % 3 :
            print("Fizz!")
        elif dato % 5:
            print("Buzz")
        elif dato % 3 and dato % 5:
            print("FizzBuzz")
        else :
            print(dato)
            
    print(lista)  

### LABORATORIO ###

    #Tabla de multiplicacion
    numero = int(input("Ingrese un numero: "))
    lista = list(range(1,11))
    tabla = []

    for i in lista:
        producto = (numero * i)
        tabla.append(producto)

    print(tabla)    
    ## otra forma ##
    numero = int(input("Ingrese un numero: "))

    tabla = []

    for i in list(range(1,11)):
        producto = (numero * i)
        tabla.append(producto)

    print(tabla)    

## LABORATORIO ##

matriz = []

filas = int(input("Ingrese cantidad de filas: "))
columnas = int(input("Ingrese cantidad de columnas: "))

# un ciclo para el nro de filas
    # y dentro de este, otro para el nro de columnas

















