class VerAnime:
    def __init__(self,nombre):
        self.nombre=nombre
anime1= VerAnime("Naruto")
anime2= VerAnime("Black Clover")

class Cristian(VerAnime):
    pass
    def verAnime():
        return"\033[;36m"+"Ver anime de {}".format(anime1.nombre)
    
class Pablo(VerAnime):
    pass
    def verAnime():
        return"Ver anime de {}".format(anime2.nombre)
    
Espectador1 =Cristian
Espectador2 =Pablo
print(Espectador1.verAnime())
print(Espectador2.verAnime())
