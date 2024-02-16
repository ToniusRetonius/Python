import requests
import time
import os

pagina = ""

for n in range(0,10,1):
    
    r = requests.get(pagina)

    datos = r.text

    inicio_etiqueta = datos.find("")
    inicio_precio = inicio_etiqueta + len('')
    final = datos[inicio_precio:].find('')

    precio = datos[inicio_precio:inicio_precio+final]

    time.sleep(3)

    f = open("", "")
    f.write(time.asctime() + "" + precio + "\n")
    print(time.asctime() + "" + precio + "\n")
    f.close()