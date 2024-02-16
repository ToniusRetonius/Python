class Persona():
    def __init__(self):
        self.altura = 1.8

    def hablar(self):
        print("Hola perrito!")

class Alumno(Persona):
    def __init__(self):
        """ cuando se ejecute el init de la clase Alumno, llama a su clase padre >>> con SUPER() """
        super().__init__()
        self.promedio = 8
    
    def estudiar():
        print('Estudiando...')


