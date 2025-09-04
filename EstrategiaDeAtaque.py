from random import randint
from abc import ABC, abstractmethod

class EstrategiaDeAtaque(ABC):
    @abstractmethod
    def atacar(self, estrategia):
        pass

class AtaqueCritico(EstrategiaDeAtaque):
    def atacar(self, atacante, inimigo, time_inimigo):
        dano = 60 * atacante.nivel
        chance_critico = randint(1,100) 
        if chance_critico >= 80: 
            print("Ataque Crítico!")
            dano *= 2
        inimigo.receber_dano(dano, atacante)
        return dano

class RouboDeVida(EstrategiaDeAtaque):
    def atacar(self, atacante, inimigo, time_inimigo): 
        dano = 70 * atacante.nivel
        inimigo.receber_dano(dano, atacante)
        atacante.vida += dano * 0.1
        print(f"{atacante.champ} curou {dano * 0.1}!")
        return dano


class AtaqueEmArea(EstrategiaDeAtaque):
    def atacar(self, atacante, inimigo, time_inimigo):
        dano_area = 20 * atacante.nivel
        print(f"{atacante.champ} causou dano em area ao time inimigo")
        time_inimigo.receber_dano(dano_area, atacante)
        return dano_area



