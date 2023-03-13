class Salida:
    def __init__(self,Lugar):
        self.Lugar=Lugar
salida1= Salida("El tunco")
salida2= Salida("El cuco")

class Novia1(Salida):
    pass
    def vacil():
        return"Ir de paseo a {}".format(salida1.Lugar)
    
class Novia2(Salida):
    pass
    def vacil():
        return"Ir de paseo a {}".format(salida2.Lugar)
    
salidita1 =Novia1
salidita2 =Novia2
print(salidita1.vacil())
print(salidita2.vacil())
