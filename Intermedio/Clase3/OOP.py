""" OOP (Object Oriented Programming) """
    # las Clases son las creadoras de Objetos
    # las variables son Atributos
    # las funciones son Metodos

class FabricaPelotas():
    """ __init__ es el constructor. Y en el pongo los atributos del objeto """
    def __init__(self,c,d,m="Plastico"):
        """ si le paso a un parametro un valor, le asigno uno por default (ex. m="Plastico") """
        """ para asignar un atributo privado, utilizo el doble guion bajo ( __ ) """
        self.color = c
        self.diametro = d
        self.__material = m
        print("Objeto creado")
    
    def picar(self):
        print("pim pam pum")

    """ creamos una funcion GETTER """
    def get_material(self):
        return self.__material
    
    """ creamos un SETTER """
    def set_material(self, nm):
        self.__material = nm

###############

pelota1 = FabricaPelotas("Rojo", 20 )

pelota2 = FabricaPelotas()

""" con el print, un atributo privado no lo puedo obtener """
print(pelota1.__material)

""" con la funcion getter puedo obtener el material """
print(pelota1.get_material())

""" con la funcion setter, le modificamos el material """
print(pelota1.set_material("Algodon"))



