### CLASE 6 ###

    # MODULOS (conjunto de funciones)

    print("Hola Mundo")
    print("Python para peleles")
    dia = "Lunes"
    var = 10
    dia = "Martes"
    print("Hola Mundo")
    print("Python para peleles")
    aux = var + 5
    print(aux)
    dia = "Miercoles"
    print("Hola Mundo")
    print("Python para peleles")
    resultado = aux ** 2
    dia = "Jueves"
    
    # muy costoso realizar cambios, engorroso ....
    # para solucionar esto: utilizamos las FUNCIONES
    # Las FUNCIONES arupan una porcion de codigo y se le asigna un nombre
    # para definirla utilizo DEF + nombre de funcion
    # def nombre  (parametros) :

    def saludo():
        print("Hola Mundo")
        print("Python para peleles")

    # INVOCO la funcion >>>
    saludo()

    def imprimir_datos (titulo, dato) :
        print(titulo)
        for d in dato :
            print(d)

    personas = ["Tomas","Flor","Luli","Loli"]
    edades = [19,20,21,22]

    imprimir_datos("Nombres: ",personas)
    imprimir_datos("Edades: ",edades)
    imprimir_datos("Nro CUIT: ", [22222, 44444,55555,6666])

    # Funciones con valores de retorno

    def sumar (num1, num2):
        return num1 + num2

    # Range (inicio, fin) --> (inicio, ... , fin -1)

    def rango(inicio, fin) :
        resultado = []
        while inicio < fin :
            resultado.append(inicio)
            inicio = inicio + 1
        return resultado

    print(rango(1,6))

## LABORATORIO ##
matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

def imprimir_matriz(matriz):
    for m in matriz:
            for i in m:
                print(i)
                
imprimir_matriz(matriz)

def sumar(num1, num2, num3, num4, num5):
    return num1 + num2 + num3 + num4 + num5

print(sumar(1,2,3,4,5))













    
