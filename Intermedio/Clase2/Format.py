# La funcion FORMAT me permite armar un string con variables ya declaradas

    # Nombre = "Juan"
    # Edad = 50
    # "Tu nombre es" + nombre + "tu edad es " + str(edad)
# el format me permite posicionar datos 

nombre = "Juan"
edad = 50
mensaje = "Tu nombre es {0} y tu edad es {1}"
mensaje.format(nombre, edad)

# otra forma es >>
mensaje2 = f"Tu nombre es {nombre} y tu edad es {edad}"

# tambien del lenguaje C tomamos el operador %
    # %s : para string
    # %d : para enteros
