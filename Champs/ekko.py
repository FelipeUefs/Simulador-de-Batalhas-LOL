from campeao import Campeao
import random

class Ekko(Campeao):
    def __init__(self, nome, nivel, vida, estrategia):
        super().__init__(nome, "Ekko", nivel, vida, "Jungle", estrategia)

    def usar_R(self):
        return f"Ekko usou Cronoquebra temporal e voltou no tempo!"
    



    


    