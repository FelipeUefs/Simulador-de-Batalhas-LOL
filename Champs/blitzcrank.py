from campeao import Campeao
import random

class Blitzcrank(Campeao):
    def __init__(self, nome, nivel, vida, estrategia):
        super().__init__(nome, "Blitzcrank", nivel, vida, "Suporte", estrategia)

    def usar_R(self):
        return f"Blitzcrank usou Campo Estático!"
    
        
