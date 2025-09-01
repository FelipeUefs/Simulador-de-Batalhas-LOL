
## 👨‍💻 Autores
**Felipe Gomes e João Pedro**  
Projeto desenvolvido no contexto do **Desafio do Módulo 1 - Curso de DEV Mobile**.
# 🥊 Simulador de Batalha entre Campeões
## 📌 Sobre o Projeto
Este projeto foi desenvolvido como parte do **Desafio do Módulo 1** . Curso de DEV MOBILE
A proposta é simular batalhas entre campeões inspirados no jogo *League of Legends*, aplicando os conceitos de:

- **Herança**
- **Polimorfismo**
- **Classes abstratas e concretas**
- **Coleção de Objetos**
- **Tratamento de Exceções (try/except)**
- **Padrões de Projeto: Strategy e Observer**

O sistema cria dois times, cada um composto por campeões com **funções distintas**, que lutam entre si até restar apenas um time vencedor.

---

## ⚔️ Funcionalidades
- Criação de dois times de campeões, com papéis específicos (Top, Mid, Jungle, ADC, Suporte).  
- Cada campeão possui:
  - Nome
  - Nível
  - Vida
  - Função (role)
  - Estratégia de ataque (**Crítico, Roubo de Vida ou Ataque em Área**)  
- Implementação de **polimorfismo** para habilidades especiais dos campeões.  
- Método `receberDano()` que controla a vida e evita valores negativos.  
- Uso de **try/except** para impedir que dois campeões da mesma função entrem no mesmo time.  
- Simulação de batalha com ataques alternados até que um dos times seja derrotado.  
- Padrão **Observer** para monitorar eventos como perda de vida e necessidade de cura.  
- Ranking final mostrando desempenho dos campeões.  

---

## 🛠️ Estrutura do Projeto
```Projeto/
│── Champs/
│ ├── zed.py
│ ├── warwick.py
│ ├── blitzcrank.py
│ ├── jinx.py
│ ├── mordekaiser.py
│ ├── galio.py
│ ├── thresh.py
│ ├── gwen.py
│ ├── ekko.py
│ └── missFortune.py
│
│── Time.py
│── EstrategiaDeAtaque.py
│── Observer.py
│── main.py
```
