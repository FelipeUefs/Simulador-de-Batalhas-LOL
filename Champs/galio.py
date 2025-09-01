from campeao import Campeao
import random

class Galio(Campeao):
    def __init__(self, nome, nivel, vida, estrategia):
        super().__init__(nome, "Galio", nivel, vida, "Mid", estrategia)

    def usar_R(self):
        return f"Galio usou Entrada Heroica!"
    
       