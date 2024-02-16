### LABORATORIO 1 ###

numeros = [10,20,30,40]

""" i = 0
suma = 0
while i < len(numeros)-1:
    suma = suma + numeros[i]
    i = i + 1

print(suma) """

### LABORATORIO 2 ###

numeros = [10,20,30,40]

while len(numeros) > 0:
    print(numeros[0])
    del numeros[0]

print(numeros)

# Ejercicio 1
def multiplos(limite):
    numeros = []
    for n in range(1,limite + 1, 1):
        contador = 0
        if n % 3 == 0 and n % 5 == 0:
            numeros.append(n)
    return numeros


# Ejercicio 2

def primos(limite):
    p = []
    for n in range(1,limite+1,1):
        contador = 0
        for x in range(1,n+1,1):
            if n % x == 0:
                contador = contador + 1
        if contador <=2:
            p.append(n)
    return p

