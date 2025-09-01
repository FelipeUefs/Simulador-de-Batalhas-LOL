from campeao import Campeao

class Zed(Campeao): 
    def __init__(self, nome, nivel, vida, estrategia):
        super().__init__(nome, "Zed", nivel, vida, "Mid", estrategia)
        
    def usar_R(self):
        return f"Zed usou Marca Fatal"
    

