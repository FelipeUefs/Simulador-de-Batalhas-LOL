from campeao import Campeao

class Jinx(Campeao):
    def __init__(self, nome, nivel, vida, estrategia):
        super().__init__(nome, "Jinx", nivel, vida, "Adc", estrategia)

    def usar_R(self):
        return f"Jinx usou Super Mega Míssil da Morte!"
    
        
        
    