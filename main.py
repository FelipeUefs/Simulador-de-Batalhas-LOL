#Time 1
from Champs.zed import Zed
from Champs.warwick import Warwick
from Champs.blitzcrank import Blitzcrank
from Champs.jinx import Jinx
from Champs.mordekaiser import Mordekaiser

#Time 2
from Champs.galio import Galio
from Champs.thresh import Thresh
from Champs.gwen import Gwen
from Champs.ekko import Ekko
from Champs.missFortune import MissFortune

from Time import Time
from EstrategiaDeAtaque import AtaqueEmArea, AtaqueCritico, RouboDeVida
import random
from Observer import NeedHealer

def pancadariaGeneralizada(time1, time2, observer_time1):#, observer_time2):
    print("TIME 1")
    time1.listar_Time()
    print("\nTIME 2")
    time2.listar_Time()


    print("\n---COMEÇA A PANCADARIA---")
    #inicio da gameplay
    inic = random.randint(1,2)
    while time1.time_vivo() and time2.time_vivo():
        if inic % 2 == 1:
            print("\n-Time 1 ataca-")

            bate = random.choice(time1.campeoes)
            while bate.vida <= 0:
                bate = random.choice(time1.campeoes)

            apanha = random.choice(time2.campeoes)
            while apanha.vida <= 0:
                apanha = random.choice(time2.campeoes)

            bate.atk_basico(apanha, time2)
            #observer_time2.update()
        else:
            print("\n-Time 2 ataca-")

            bate = random.choice(time2.campeoes)
            while bate.vida <= 0:
                bate = random.choice(time2.campeoes)

            apanha = random.choice(time1.campeoes)
            while apanha.vida <= 0:
                apanha = random.choice(time1.campeoes)

            bate.atk_basico(apanha, time1)
            observer_time1.update()
        inic += 1
    print("FIM DE JOGO!")
    if time1.time_vivo():
        print("\nTime 1 venceu!\n")
        
    else:
        print("\nTime 2 venceu!\n")
    
    time1.ranking()
    time2.ranking()
        

def main():

    sombra = Zed(nome="Zeca_Urubu", nivel=10, vida=2000, estrategia= AtaqueCritico())
    loboPidao = Warwick(nome="Juninho002", nivel=13, vida=2500, estrategia= RouboDeVida())
    grab = Blitzcrank(nome="CG", nivel=5, vida=2500, estrategia= AtaqueEmArea())
    maluca = Jinx(nome="Loola", nivel=7, vida=1500, estrategia= AtaqueCritico())
    morto_vivo = Mordekaiser(nome="20matar", nivel=12, vida=3000, estrategia= AtaqueEmArea())
    
    galo_depedra = Galio(nome="Galileu", nivel=11, vida=3000, estrategia= AtaqueEmArea())
    ceifador = Thresh(nome="Corrente", nivel=9, vida=2000, estrategia= RouboDeVida())
    costureira = Gwen(nome="Agulhinha", nivel=8, vida=2500, estrategia= RouboDeVida())
    viajante = Ekko(nome="Tempus", nivel=10, vida= 2100, estrategia= AtaqueCritico())
    atiradora = MissFortune("MFzinha", nivel=7, vida=1800, estrategia= AtaqueCritico())

#----------------------Time 1------------------------------------------------#
    time1 = Time()
    time1.adicionar_campeao(sombra)
    time1.adicionar_campeao(loboPidao)
    time1.adicionar_campeao(grab)
    time1.adicionar_campeao(maluca)
    time1.adicionar_campeao(morto_vivo)
    observer_time1 = NeedHealer(time1.campeoes)
#----------------------Time 2------------------------------------------------#
    time2 = Time()
    time2.adicionar_campeao(galo_depedra)
    time2.adicionar_campeao(ceifador)      
    time2.adicionar_campeao(costureira)
    time2.adicionar_campeao(viajante)
    time2.adicionar_campeao(atiradora)
    #observer_time2 = NeedHealer(time2.campeoes)

    pancadariaGeneralizada(time1, time2, observer_time1) #observer_time2)

main()


