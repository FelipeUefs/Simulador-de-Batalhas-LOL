class FunctionRepeat(Exception): #Exception personalizada
    pass

class Time():
    def __init__(self):
        self.campeoes = []
    
    def time_vivo(self):
        for i in self.campeoes:
            if i.vida > 0:
                return True
        return False
    
    def receber_dano(self, dano, inimigo):
        for i in self.campeoes:
            if i.vida > 0:
                i.receber_dano(dano, inimigo)


    def adicionar_campeao(self, campeao):
            try:
                for i in self.campeoes:
                    if i.funcao == campeao.funcao:
                        raise FunctionRepeat
                self.campeoes.append(campeao)
                print(f"{campeao.champ} Adicionado com sucesso!")       
                return True
            
            except FunctionRepeat:
                print(f"Erro: Função {campeao.funcao} já existe no time.")
                return False
    
  
    def listar_Time(self):
        print("STATUS DO TIME")
        for i in self.campeoes:
            print(i.exibir_status())

    def ranking(self):
        print("\nRANKING DO TIME")
        ranking = sorted(self.campeoes, key=lambda x: (x.kills, x.danoCausado), reverse=True)
        for i in ranking:
            print(i.exibir_k())
        
    def usarHabilidadesDeTodos(self):
        print("\nCOMBO DE ULTS")
        for i in self.campeoes:
            print(i.usar_R())
        