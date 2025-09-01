class Observador:
    def __init__(self):
        self._observadores = [] #guarda todo mundo que está observando o Sujeito
    
    def adicionar_observadores(self, lista_obs):
        self._observadores.append(lista_obs) #adiciona os observadores na lista

    def atualizar(self, evento):
        for observadores in self._observadores:
            observadores.atualiza(evento)

#Observadores

class NeedHealer:
    def __init__(self, campeoes):
        self.campeoes = campeoes

    def update(self):
        for champs in self.campeoes:
            if 0.30 * champs.lifemax <= champs.vida <= 0.4 * champs.lifemax:
                print(f"AVISO - ({champs.champ}) - PRECISA DE CURA!")
                

