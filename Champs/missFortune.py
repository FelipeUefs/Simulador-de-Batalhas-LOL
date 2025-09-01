from campeao import Campeao
import random

class MissFortune(Campeao):
    def __init__(self, nome, nivel, vida, estrategia):
        super().__init__(nome, "Miss Fortune", nivel, vida, "Adc", estrategia)

    def usar_R(self):
        return f"Miss Fortune usou Metendo Bala!"
    



        