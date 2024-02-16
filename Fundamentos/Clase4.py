## CLASE 4 ##

## Laboratorio ##

nombre = input("Ingrese su nombre: ")
if nombre == "" :
    print("Tu nombre es un campo vacio")
elif nombre != "" :
    print("Tu nombre es : ", nombre)
    
####################

# Utilizar una variable como un contenedor 
# la finalidad es almacenar datos y luego poder acceder a ellos

    # LISTAS
        
        # Definir una variable de tipo LISTA (ARRAY)
        
            # array = [elemento1, elemento2,..., elementoN]
            var_numeros = [1, 2, 3, 4, 5]
            empleados = ["Juan", "Sofia", "Michael"]
            varios = [True, "Hola mundo", 3.12]
            
        # Para acceder a sus elementos
        
            # array[indice]
            print(varios[1]) ===> "Hola mundo"
            
        # Para agregar un nuevo elemento al final
        
            # array.append(elemento)
            var_numeros.append(6)
        
        # Para agregar un elemento en una posicion especifica
        
            # array.insert(posicion, elemento)
            
        # Eliminar elemento 
        
            # del array[indice]
        
        # Calcular la longitud (cant. de elementos)
        
            # len (arrar)
            print (len(empleados))
        
        #Calcular indices 
        
            print (empleados[len(empleados)] - 1) 
    
            
    # MATRICES
     
    # son estructuras de datos compuestas, es decir listas de listas
    
    matriz = [["hola", 1 , True],["mundo", 2, True],["python", 3, True]]

    #Acceder a la matriz
        print(matriz[2][3]) ==> True
        
#### Laboratorio ####
matriz = [   [3.3, 6.1, 4.0],[4.9, 5.7, 6.4] ]

fila = int(input("Ingrese el numero de fila: "))
columna = int(input("Ingrese el numero de columna: "))

if (fila == 0 or fila == 1) and (columna >= 0 or columna <= 2):
    print(matriz[fila][columna])
else :
    print("error")


### BUCLES ###

    # WHILE
    
    # Repite una porcion de codigo de
    # acuerdo al resultado de una operacion logica TRUE
    # luego de evaluar la condicion verdadera, vuelve a ejecutar 
    # HASTA que la condicion sea FALSE 
    var = 1
    while var < 3 :
        print("Clase de python", var)
        var = var + 1
    
    # la palabra reservada BREAK permite cortar la linea de
    # ejecucion del ciclo 
    
    var = 1
    while True:
        if var < 3 :
            print("Clase de python", var)
            var = var + 1 
        else :
            break



















