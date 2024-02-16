# TRY & EXCEPT rescata el programa de posibles errores

edad = input("Ingrese su edad: ")

try:
    edad = int(edad)
    if edad < 18:
        print("Menor")
    else:
        print("Mayor")
# en except puedo declararle que error puedo esperar    
except (ValueError, TypeError):
    print("Ese valor no es una edad cachorro!")
except TypeError:
    print("Escribiste como el ogt!")