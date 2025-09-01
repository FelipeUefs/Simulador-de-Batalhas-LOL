from campeao import Campeao
import random
class Gwen(Campeao):
    def __init__(self, nome, nivel, vida, estrategia):
        super().__init__(nome, "Gwen", nivel, vida, "Top", estrategia)

    def usar_R(self):
        return f"Gwen usou Ponto-Cruz!"
    
       