from campeao import Campeao

class Mordekaiser(Campeao):
    def __init__(self, nome, nivel, vida, estrategia):
        super().__init__(nome, "Mordekaiser", nivel, vida, "Top", estrategia)

    def usar_R(self):
        return f"Moderkaiser usou Reino da Morte!"
    
        

    


        

        