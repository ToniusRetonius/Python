########## CLASE 2  ##########

def funcion1 (*t):
    print(t)

## el paramentro "t" hace referencia a una tupla
# Tuplas : listas inmutables armadas con parentesis
# es decir, que los datos se adjuntan todos dentro de esta coleccion 
funcion1(10,20,30)

def funcion2 (*d):
    print(d)

## el parametro "d" hace referencia a un diccionario
# Diccionarios : entre llaves { clave : valor}
funcion2(a = 1, b = "Hola", c = True)

## funciones de orden superior : aquellas que toman de parametros a otras funciones; o devuelven una como resultado

def cuadrado(x):
    return x**2

def aplicar(funcion, lista):
    resultado = []
    for n in lista:
        resultado.append(funcion(n))
    return resultado

numeros = [1,2,3,4]

r = aplicar(cuadrado, numeros)

print(r)

## Funciones anonimas o LAMDA
# crear, utilizarla y descartarla 

lambda x : x**2

# esta lamda es identica a la funcion cuadrado
# las funciones lamda DEBEN SER DECLARADAS UNICAMENTE DENTRO COMO PARAMETRO DE UNA FUNCION DE ORDEN SUPERIOR

l = aplicar(lambda x: x**2, numeros)


##  Funcion OPEN()
# su funcion es abrir un archivo 

open = open(".txt", "(modo)")

# tipos de modos
    # w : write , si no existe lo crea, si existe, lo pisa
    # r : read , lo abre en modo lectura (read Only)
    # a : append , si no existe lo crea y sino, lo agrega al final

f = open("miarchivo.txt", "w")
f.write("Hoy hace frio")
f.close()

f = open("miarchivo.txt", "a")
f.write(", pero manana mejora seguro!")
f.close()

