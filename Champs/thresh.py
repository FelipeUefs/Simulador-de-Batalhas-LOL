from campeao import Campeao

class Thresh(Campeao):
    def __init__(self, nome, nivel, vida, estrategia):
        super().__init__(nome, "Thresh", nivel, vida, "Suporte", estrategia)

    def usar_R(self):
        return f"Thresh usou A Caixa!"
    

            
        