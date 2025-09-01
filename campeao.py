from abc import ABC, abstractmethod
#Classe Mãe dos Campeões, aqui estará todos os atributos padrões
class Campeao(ABC):
    def __init__(self, nome, champ, nivel, vida, funcao, estrategia):
        self.nome = nome #Nome do Usuario
        self.champ = champ #Nome do Campeao usado
        self.nivel = nivel #Nivel do Campeao
        self.vida = vida #Vida do Campeão
        self.funcao = funcao #funçao do Campeão
        self.kills = 0 #Quantidade de Abates
        self.danoCausado = 0 #Dano Causado
        self.lifemax = vida #vida maxima ou seja o valor inicial da vida do campeao
        self.estrategia = estrategia

    @abstractmethod
    def usar_R(self): #Classe Abstrata para a Habilidade do Campeão
        pass
    
    def atk_basico(self, inimigo, time_inimigo): #Ataque Basico do Campeão
        self.estrategia.atacar(self, inimigo, time_inimigo)

    def exibir_status(self): #Classe para Exibição dos Status do Campeão
        return f"Nome: {self.champ}, Nivel: {self.nivel}, Vida: {self.vida}, Função: {self.funcao}"
    
    def exibir_k(self): #Classe para Exibição do KDA do Campeão
        return f"{self.champ} - Abates: {self.kills}, Dano Causado: {self.danoCausado}"
    
    
    def receber_dano(self, dano, inimigo):
        self.vida -= dano
        inimigo.danoCausado += dano
        if self.vida < 0:
            self.vida = 0
            inimigo.kills += 1
            print(f"{self.champ} recebeu {dano} de dano foi abatido por {inimigo.champ}!")
            return True
        
        print(f"{self.champ} recebeu {dano} de dano por {inimigo.champ}. Vida restante: {self.vida}")
        return False