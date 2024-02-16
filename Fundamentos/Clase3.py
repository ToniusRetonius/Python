### OPERACIONES LOGICAS ###

# Evalua ambas operaciones y devuelve BOOLEAN

    # AND #
        #(conjuncion => para que sea TRUE, TODOS los
        # miembros de la operacion deben ser TRUE :
        
        var = 5
        var >= 1 and var <=10
        #   true         true
        #   ==> TRUE
    
    # OR #
        #(Disyuncion => para que sea TRUE, AL MENOS UNO de
        # los miembros debe ser TRUE : 
        
        var = 5
        var >= 1 or var <4
        #   true        false
        #   ==> TRUE
    
    # NOT #
        #Negacion => invierto su valor logico
        duerme = True
        print(not duerme)
        # ---> False
    
# CONDICIONALES

    # Los condicionales difieren la lectura del interprete 
    #(cierta parte del codigo la lee en funcion de una condicion,
    # modifica el flujo del programa) 
    # Ejecutara una sentencia SI se cumple la condicion establecida
    
    num = 15
    if num > 10 :
        print ("La variable es mayor que diez")
        # ~ a = 8
        # ~ if a == 8 or a == 10 : 
            # ~ print ("La variable a es igual a 8 o es igual a 10")
    else :
        print ("La variable es menor a 10")
        
    
    # ~ if nombre == "Jorge" : 
        # ~ print("Hola Jorgito")
    # ~ else if nombre == "Maria" :
        # ~ print("Hola Maria")
    # ~ else if nombre == "Tomas" : 
        # ~ print ("Hola Tomi")
    # ~ else :
        # ~ print("Ni idea quien sos perri, pero aca no entras")
    
    # INPUT siempre devuelve TIPO STRING:
    nombre = input("Ingrese su nombre: ")
    
    # Si quiero ingresar un dato de tipo INT : 
    num = input ("Ingrese un valor para la suma: ")
    suma = 10 + int(num)
    
    if nombre == "Jorge" or nombre == "Maria" or nombre == "Tomas" :
        print ("Bienvenido " + nombre " a nuestro negocio ilicito")
    else :
        print("Toca de aca juguete!")
        

### Laboratorio ###
cadena1 = input("Ingrese una cadena: ")
cadena2 = input("Ingrese otra cadena: ")

if cadena1 == cadena2 :
    print("Las cadenas son iguales!")
else :
    print("Las cadenas son distintas!")

####################################

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

print(num1 + num2)

### LABORATORIO 2 ###
nota = int (input("Ingrese su nota: "))

if nota == 10 :
    print("Excelente!")
    
elif nota >= 7 and nota <= 9 :
    print("Muy bien!")
    
elif nota >=4 and nota <= 6 :
    print("Safaste!")
    
elif nota >10 : 
    print("Flasheaste perri!")
    
else :
    print("Desastre, te caes a pedazos!")

### LABORATORIO 3 ###

tiempotrabajado = int(input("Ingrese cuanto laburo: "))

jornada = 48
valorhora = 15
horaextra = 20

if tiempotrabajado == 48:
    salario1 = jornada * valorhora
    print (salario1)
    print("Un tipo muy laburador! Hiciste: ", salario1 ,"pesitos")
    
elif tiempotrabajado > 48:
    salario2 = (jornada * valorhora) + (tiempotrabajado - jornada)*horaextra 
    print(salario2) 
    print("Andasss manija che, hiciste", salario2, "pesitos")
    
elif tiempotrabajado < 48:
    salario3 = tiempotrabajado * valorhora
    print(salario3)
    print("Que vago que estamos ehh... Solo ganaste", salario3, "pesitos")
