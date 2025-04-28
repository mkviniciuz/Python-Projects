import random
import os
import time

class CharacterObject():

    def __init__(self, name, maxhealth, attack, defense, level, souls, nSouls, distribuitonPoints, lucky):
        self.name = name #Nome do personagem
        self.level = level #Nivel do personagem
        self.maxhealth = maxhealth#Vida maxima do personagem
        self.actual_health = maxhealth
        self.attack = attack #Ataque do personagem
        self.defense = defense #Defesa do personagem
        self.souls = souls #Quantidade de almas que o personagem possui
        self.nSouls = nSouls #Quantidade de almas necessarias para upar
        self.distribuitonPoints = distribuitonPoints
        self.lucky = lucky


        self.deck = []
        self.critical = 0
        self.extra_defense = 0
        self.defense_turn = 0
        self.eventHistory = []
        self.battleRound = 1
        self.extra_health = 0

        self.towerEffects = {
            "pactoNeorato": False,
            "ultimoSuspiro": False,
            "tratoSanguinario": False,
            "sentencaFinal": False
        }

        self.roundEffects = {
    "[VIDA] Ultimo suspiro": False,
    "[VIDA] Pacto Neorato": False,
    "[VIDA] Bênção dos Ancestrais": False,
    "[VIDA] Essência Renovada": False,
    "[VIDA] Renascimento Lunar": False,
    "[VIDA] Flor da Vitalidade": False,
    "[VIDA] Lágrima da Fênix": False,
    "[VIDA] Ritual da Cura": False,
    "[VIDA] Sopro da Esperança": False,
    "[VIDA] Vigília dos Antigos": False,
    "[VIDA] Alma Restaurada": False,
    "[ATAQUE] Trato sanguinário": False,
    "[ATAQUE] Sentença final": False,
    "[ATAQUE] Lâmina dos Condenados": False,
    "[ATAQUE] Rajada Infernal": False,
    "[ATAQUE] Golpe Carmesim": False,
    "[ATAQUE] Fúria do Dragão": False,
    "[ATAQUE] Tempestade de Lâminas": False,
    "[ATAQUE] Martelo dos Deuses": False,
    "[ATAQUE] Espada do Eclipse": False,
    "[ATAQUE] Chamas Profanas": False,
    "[ATAQUE] Garras da Besta": False,
    "[DEFESA] Herói defensor": False,
    "[DEFESA] Escudo sagrado": False,
    "[DEFESA] Barreira de Alvorada": False,
    "[DEFESA] Muralha de Ébano": False,
    "[DEFESA] Reflexo Protetor": False,
    "[DEFESA] Armadura de Gaia": False,
    "[DEFESA] Véu da Redenção": False,
    "[DEFESA] Guardião dos Portões": False,
    "[DEFESA] Fortaleza Espiritual": False,
    "[DEFESA] Aegis Eterna": False,
    "[DEFESA] Bastião Celeste": False,
    "[SORTE] Sorte de Mikyealaar": False,
    "[SORTE] Sorte dos Reinos": False,
    "[SORTE] Bênção da Fortuna": False,
    "[SORTE] Dados do Destino": False,
    "[SORTE] Amuleto do Inesperado": False,
    "[SORTE] Olho da Providência": False,
    "[SORTE] Roda dos Sortilégios": False,
    "[SORTE] Canção da Fortuna": False,
    "[SORTE] Corrente da Sorte": False,
    "[SORTE] Trébol do Caos": False,
    "[SORTE] Mão Oculta": False
}


    def level_upgrade(self):
    
        while True:    
            try:
                print(f"""          
                    
            +{'='*38}+
            |          x LEVEL UPGRADE x           |
            +{'='*38}+
            \______________________________________/ 
                
              Você possui {int(self.souls)} almas
              Você precisa de {int(self.nSouls)} almas para upar!
                    
              Deseja subir de nivel?
              [1] Sim / [2] Não
                    """)
                choose = int(input("              Escolha: "))
                
                if choose == 1:
                    if self.souls >= self.nSouls: #Verifica se a quantidade de almas é suficiente
                        self.level += 1 #Aumenta o nivel do personagem
                        self.souls -= self.nSouls #Diminui a quantidade de almas
                        self.nSouls += (self.nSouls * 0.15) + (self.level * 10) #Aumenta a quantidade de almas necessarias para upar
                        self.distribuitonPoints += 1 #Aumenta a quantidade de pontos de distribuição
                        os.system('cls')
                        
                        print(f"""
                              
              Qual Status deseja Aprimorar?
                              
              [1] Vida   | {self.maxhealth} HP   -> ({self.maxhealth + 25})  | +25 HP ❤️
              [2] Ataque | {self.attack} ATAQUE  -> ({self.attack + 10}) | +10 ATQ ⚔️
              [3] Defesa | {self.defense} DEFESA -> ({self.defense + 2})  | +2 DEF 🛡️
                
                            """)
                        choose = int(input("              Escolha: "))

                        if choose == 1:
                            self.maxhealth += 25
                            self.actual_health = self.maxhealth
                            os.system('cls')
                            continue

                        elif choose == 2:
                            self.attack += 10
                            os.system('cls')
                            continue

                        elif choose == 3:
                            self.defense += 2
                            os.system('cls')
                            continue


                    else:
                        os.system('cls')
                        print("Você não possui almas suficientes para upar!")
                        break

                else:
                    os.system('cls')
                    break

            except ValueError:
                os.system('cls')
                print("Valor invalido")

    def show_status(self, actual_event, kills):
        color = "\033[91m" if self.actual_health < self.maxhealth * 0.3 else "\033[92m"
        bar = int((self.actual_health / self.maxhealth) * 20)
        print(f"""
      +{'='*38}+
      |       x STATUS DO PERSONAGEM x       |
      +{'='*38}+
      \______________________________________/

        Nome: {self.name}

        ⭐ Nível: {self.level}
        ❤️  HP: {color}{'█' * bar}{'_' * (20 - bar)}\033[0m {self.actual_health}/{self.maxhealth}
        ⚔️  Ataque: {self.attack}
        🛡️  Defesa: {self.defense}
        🍀 Sorte: {self.lucky}
        👻 Almas: {int(self.souls)}

        🃏 Deck: {self.deck}

        Almas Necessarias: {int(self.nSouls)}
        Pontos para Distribuir: {self.distribuitonPoints}

        \033[91mMonstros derrotados:\033[0m  \033[31m{kills}\033[0m
      +{'='*38}+

      {actual_event}
""")
        sleeper = input("")
        os.system('cls')

    def action_attack(self, target):
        target.actual_health = max(0, target.actual_health - (self.attack - target.defense*0.2))
        bar = int((target.actual_health / target.maxhealth) * 20)
        print(f"""
          [HEROI]
          Você atacou!
          Você infligiu 🗡️  {int(self.attack - (target.defense*0.2))} de dano!
          
          Vida do monstro:
          [{'█' * bar}{'_' * (20 - bar)}] {target.actual_health:.2f}/{target.maxhealth}
                
                  """)
        self.extra_remove()
        sleeper = input("")
        os.system('cls')

    def action_defense(self):
        if self.defense_turn > 0:
            print(f"""
          [ERROR]
          Efeito de 🛡️  {self.defense} [DEFESA] já esta aplicado
                Restam {self.defense_turn} turnos restantes
        """)
            sleeper = input("")
            os.system('cls')
        
        else:
            self.extra_defense = self.defense*0.5
            self.defense_turn = 2
            self.defense += self.extra_defense
            print(f"""
            [HEROI]
            Você defendeu-se!
            Defesa aumentada para {self.defense} DEF!
            (Duração de {self.defense_turn} Turnos)
            """)
            sleeper = input("")
            os.system('cls')
    
    def extra_remove(self):

        self.defense_turn = max(0, self.defense_turn - 1)
        if self.defense_turn == 0:
            self.defense -= self.extra_defense
            self.extra_defense = 0
            
    def action_display(self, target, actual_event, kills):
        rounds = 1
        while target.actual_health > 0:
            try:
                if (rounds % 2) == 0:
                    monster_action = [target.monsterAttack, target.monsterDefense]
                    sorted_action = random.choice(monster_action)
                    sorted_action(self)
                    rounds += 1
                
                else:
                    print("...")


                print(f"""
            +{'='*38}+
            |          x PAINEL DE AÇÃO x          |
            +{'='*38}+
            \______________________________________/ 

              [1] Atacar          [5] Historico
              [2] Defender-se         de Eventos

              [3] Status          [6] Sair
                        
              [4] Status | MONSTRO

                
            +======================================+
""")
                action = int(input(f"""
          Escolha a opção: """))
                os.system('cls')

                if action == 1:
                    self.action_attack(target)
                    rounds += 1

                elif action == 2:
                    self.action_defense()
                    rounds += 1

                elif action == 3:
                    self.show_status(actual_event, kills)

                elif action == 4:
                    target.showMonsterStats()
                
                elif action == 5:
                    self.showEventHistory()


                else:
                    print("Você digitou um valor inválido! Tente novamente.")
                    sleeper = input("")
                    os.system('cls')

            except ValueError:
                print("Algo deu errado! Tente novamente")
                sleeper = input("")
                os.system('cls')
            
        print(f"""
          \033[92m[PARABENS!]\033[0m
          Você derrotou o monstro!
          \033[97m{target.souls}\033[0m almas foram obtidas.
        """)
        self.eventHistory.append(actual_event)
        self.souls += target.souls
        sleeper = input("")
        os.system('cls')

    def showEventHistory(self):
        print(f"""
            +{'='*38}+
            |       x HISTORICO de EVENTOS x       |
            +{'='*38}+
            \______________________________________/ """)
        position = 1
        for _ in self.eventHistory:
            print(f"""
            [{position}º] Acontecimento""")
            position +=1
            print(_)
        sleeper = input("")
        os.system('cls')

    def cardEvent(self, target):

            def ultimosuspiro():
                message = f"""
                [ULTIMO SUSPIRO]
                
                [GANHO]
                Caso atinja -30% da vida máxima, ganha 2% de vida por turno.

                [PERDA]
                Todo monstro encontrado tem seu HP aumentado em 10% 
                """

                if self.actual_health < self.maxhealth*0.30:
                    self.actual_health += self.maxhealth*0.02
                
                if self.battleRound == 1:
                    target.maxhealth += target.maxhealth*0.10
                    target.actual_health = target.maxhealth

                return message
            
            def pactoneorato():
                message = f"""
                [ULTIMO SUSPIRO]
                
                [GANHO]
                A cada andar o portador regenera +5% da vida atual.

                [PERDA]
                Todo monstro do tipo [Rato] se transforam em [Neoratos],
                tendo seus status aumentados em x4.
                """

                if self.battleRound == 1:
                    self.actual_health += int(self.actual_health*0.05)

                    if target.type == "Rato":
                        target.type = "Neorato [MUTADO]"
                        target.maxhealth *= 4
                        target.actual_health = target.maxhealth
                        target.attack *= 4
                        target.defense *= 4
                        target.souls *= 4

                return message
            
            def bencaoancetrais():
                message = f"""
                [BENÇÃO DOS ANCESTRAIS]
                
                [GANHO]
                Ganha +2 pontos de vida maxima por rodada.
                (Resetando após cada batalha contra um monstro nivel Deus)

                [PERDA]
                Todo monstro do tipo [Rato] se transforam em [Neoratos],
                tendo seus status aumentados em x4.
                """

                

                self.maxhealth 
                
                if self.battleRound == 1:
                    self.actual_health += int(self.actual_health*0.05)

                    if target.type == "Rato":
                        target.type = "Neorato [MUTADO]"
                        target.maxhealth *= 4
                        target.actual_health = target.maxhealth
                        target.attack *= 4
                        target.defense *= 4
                        target.souls *= 4

                return message

#Função para criar o personagem
def characterCreation():
    mensagens = [
    ("""
        ______                                        _     
        | ___ \                                      | |    
        | |_/ /___   __ _ _   _  ___  ___  ___  _   _| |___ 
        |    // _ \ / _` | | | |/ _ \/ __|/ _ \| | | | / __|
        | |\ \ (_) | (_| | |_| |  __/\__ \ (_) | |_| | \__ \ 
        \_| \_\___/ \__, |\__,_|\___||___/\___/ \__,_|_|___/
                    __/  |                                  
                    |___/
    """, 1.5)
]

    for texto, pausa in mensagens:
        print(f"\n{texto}\n")
        time.sleep(pausa)
        os.system('cls')
    print(f"""
        +{'='*38}+
        |        x NOME DO PERSONAGEM x        |
        +{'='*38}+
        \______________________________________/ 
        """)

    name = input("""   
        --> Nome: """)
    maxhealth = 200
    attack = 35
    defense = 10
    level = 1
    souls = 210
    nSouls = 210
    lucky = 0
    distribuitonPoints = 5

    character = CharacterObject(name, maxhealth, attack, defense, level, souls, nSouls, distribuitonPoints, lucky)
    os.system('cls')
    return character
    