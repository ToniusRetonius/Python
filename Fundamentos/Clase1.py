#PRINT imprime en la consola un dato tipo string,...
#una operacion de tipo int
print("Hola mundo")
print (3 + 2)

#Declaro una variable como
# (nombre de la variable) = (dato)
a = 3
b = 4*10
saludo = "Hola mundo!"

    #OPERACIONES ARITMETICAS
    
#   *
#   /
#   **
#   +
#   -

hola = "Hola"
mundo = "Mundo!"

print(hola + mundo)

    #OPERaCACIONES DE COMPARACION (RETORNAN BOOLEANOS)

# a > b ; a >= b
# a < b ; a <= b
# a == b ; a != b  (igual ; distinto)

    #OPERACIONES LOGICAS (RETORNA BOOLEANO)

# CONJUNCION (Y) :   AND  (ambas comparaciones deben ser verdaderas)
a > 1 and b > 5

# DISYUNCION (O) :   OR (basta con que una sea verdadera)
a > 10 or b > 5

# NEGACION : NOT (devuelve el contrario)
not False 
not True

    #CONDICIONALES

# IF (CONDICION) :
#    (ejecuto esta sentencia)
# ELSE : 
#    (ejecuto esta sentencia)

edad = 20
if edad > 16:
    print("puede comprar alcohol")
else:
    print("No puede comprar alcohol")

    #Para condicionales multiples 
    
# variable = dato
# IF (CONDICION primera) :
#    (ejecuto esta sentencia)
# ELIF (CONDICION segunda) : 
#    (ejecuto esta sentencia)
# ELSE :
# (ejecuto esta sentencia)

if edad >= 65:
    print("Votacion opcional")
elif edad >= 16:
    print("Puede votar")
elif edad < 5:
    print ("Sos muy chico")
else:
    print("No puede votar")
    
    #CONDICIONAL ANIDADO

# IF (CONDICION) :
#    (ejecuto esta sentencia)
#   IF (CONDICION) :
#    (ejecuto esta sentencia)
#   ELSE : 
#    (ejecuto esta sentencia)
# ELSE : 
#    (ejecuto esta sentencia)
#   IF (CONDICION) :
#    (ejecuto esta sentencia)
#   ELSE : 
#    (ejecuto esta sentencia)  
  

if edad >= 16:
    if edad >= 65:
        print("Votacion opcional")
    else
        print("Puede votar")
    
else :
    if edad < 5:
        print ("Sos muy chico")
    else:
        print("No puede votar")    
    
    
    
    
    
    
    
    
    
    
    
    
