# READ LINES es un metodo para 

rl = open("control.txt", "r")
datos = rl.readlines()
rl.close()

# imprimimos los ultimos 10 elementos
print(datos[-10:])

# aca los visualizamos mejor
for n in datos[-10:]:
    print(n.strip())
    # el metodo .strip() logramos quitar saltos de lineas o caracteres especiales de tipo \n
     
