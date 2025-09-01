from campeao import Campeao

class Warwick(Campeao):
    def __init__(self, nome, nivel, vida, estrategia):
        super().__init__(nome, "Warwick", nivel, vida, "Jungle", estrategia)

    def usar_R(self):
        return f"Warwick usou Coerção Infinita!"
    
        