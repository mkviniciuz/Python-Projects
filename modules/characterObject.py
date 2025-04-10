import random
import os

class CharacterObject():

    def __init__(self, name, maxhealth, attack, defense, speed, level, souls, nSouls, distribuitonPoints, lucky):
        self.name = name #Nome do personagem
        self.maxhealth = maxhealth #Vida maxima do personagem
        self.actual_health = maxhealth
        self.attack = attack #Ataque do personagem
        self.defense = defense #Defesa do personagem
        self.speed = speed #Velocidade do personagem
        self.level = level #Nivel do personagem
        self.souls = souls #Quantidade de almas que o personagem possui
        self.nSouls = nSouls #Quantidade de almas necessarias para upar
        self.distribuitonPoints = distribuitonPoints
        self.lucky = lucky
        self.extra_defense = 0
        self.defense_turn = 0

    def level_upgrade(self):
    
        while True:    
            try:
                print(f"""          
                    
                        {self.name} |-------------------x
                        Você possui {self.souls} almas
                        Você precisa de {self.nSouls} almas para upar!
                    
                    """)
                
                print("Deseja upar de nivel?")
                print("1 - Sim / 2 - Não")
                choose = int(input("Escolha: "))
                if choose == 1:
                    if self.souls >= self.nSouls: #Verifica se a quantidade de almas é suficiente
                        self.level += 1 #Aumenta o nivel do personagem
                        self.souls -= self.nSouls #Diminui a quantidade de almas
                        self.nSouls += (self.nSouls * 0.15) + (self.level * 10) #Aumenta a quantidade de almas necessarias para upar
                        self.distribuitonPoints += 1 #Aumenta a quantidade de pontos de distribuição

                        
                        #Exibir informações do personagem apos upar!
                        print(f"""
                        {self.name} |-------------------x
                        Você upou de nivel!
                        Seu nivel atual é {self.level }LvL
                        Você possui {self.souls} almas
                        Você precisa de {int(self.nSouls)} almas para upar!
                        Você possui {self.distribuitonPoints} pontos de distribuição
                        """) 
                        break


                    else:
                        print("Você não possui almas suficientes para upar!")

            except ValueError:
                print("Valor invalido")

    def show_status(self):

        bar = int((self.actual_health / self.maxhealth) * 20)
        print(f"""
      +{'='*38}+
      |       x STATUS DO PERSONAGEM x       |
      +{'='*38}+
      \______________________________________/
            Nome: {self.name:<30}
        ⭐ Nível: {self.level:<28}
        ❤️  HP: [{'█' * bar}{'░' * (20 - bar)}] {self.actual_health}/{self.maxhealth}
        ⚔️  Ataque: {self.attack:<27}
        🛡️  Defesa: {self.defense:<27}
        🍀 Sorte: {self.lucky:<29}
        👻 Almas: {self.souls:<29}
            Almas Necessarias: {self.nSouls:<16}
            Pontos para Distribuir: {self.distribuitonPoints:<10}
      +{'='*38}+
""")
        sleeper = input("")
        os.system('cls')

    def action_attack(self, target):
        target.actual_health -= int((self.attack - (target.defense*0.2)))
        bar = int((target.actual_health / target.maxhealth) * 20)
        print(f"""
          [HEROI]
          Você atacou!
          Você infligiu 🗡️  {int(self.attack - (target.defense*0.2))} de dano!
          
          Vida do monstro:
          [{'█' * bar}{'░' * (20 - bar)}] {target.actual_health}/{target.maxhealth}
                
                  """)
        sleeper = input("")
        os.system('cls')

    def action_defense(self):
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

        # REDUÇÃO DOS PONTOS DE DEFESA EXTRA
        self.defense -= self.extra_defense
        self.defense_turn -= 1
        if self.defense_turn == 0:
            print(f"""
                  
                  Pontos de DEFESA EXTRA reduzidos!
                  
                  """)
            
    def action_display(self, target):
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

                [1] Atacar          
                [2] Defender-se

                [3] SEUS STATUS
                [4] STATUS INIMIGO
                
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
                    self.show_status()

                elif action == 4:
                    target.showMonsterStats()


                else:
                    print("Você digitou um valor inválido! Tente novamente.")
                    sleeper = input("")
                    os.system('cls')

            except ValueError:
                print("Algo deu errado! Tente novamente")
                sleeper = input("")
                os.system('cls')
            
        print(f"""
          [PARABENS!]
          Você derrotou o monstro!
          {target.souls} almas foram obtidas.
        """)
        self.souls += target.souls
        sleeper = input("")
        os.system('cls')

#Função para criar o personagem
def characterCreation():
    print("""
        x---------------------------------------------x     
        |                                             |
        |      Defina um nome para seu personagem!    |
        |                                             |
        x---------------------------------------------x
        """)

    name = input("""   
        --> Nome: """)
    maxhealth = 200
    attack = 35
    defense = 10
    speed = 10
    level = 1
    souls = 210
    nSouls = 210
    lucky = 0
    distribuitonPoints = 0

    character = CharacterObject(name, maxhealth, attack, defense, speed, level, souls, nSouls, distribuitonPoints, lucky)
    os.system('cls')
    return character
    