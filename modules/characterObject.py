import random
import time

class characterObject():  # Inherit from object

    def __init__(self, name, health, attack, defense, speed, level, souls, nSouls, distribuitonPoints, lucky):
        self.name = name #Nome do personagem
        self.health = health #Vida do personagem
        self.attack = attack #Ataque do personagem
        self.defense = defense #Defesa do personagem
        self.speed = speed #Velocidade do personagem
        self.level = level #Nivel do personagem
        self.souls = souls #Quantidade de almas que o personagem possui
        self.nSouls = nSouls #Quantidade de almas necessarias para upar
        self.distribuitonPoints = distribuitonPoints
        self.lucky = lucky

    def LevelUpgrade(self):
    
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

    def characterStatus(self):
        print(f"""
    x------------------| STATUS |-------------------x
    |     Vida                             Almas    |
    |   |{"█" * int(self.health / 12)}| {self.health}/200   |     {self.souls}      |
    |                                               |
    |     Ataque            Level          Defesa   |
    |     {self.attack}                {self.level}              {self.defense}       |
    x-----------------------------------------------x
    """)

    def characterAttack(self, target):
        print(f"""
          [HEROI]
          Você atacou!
          Você infligiu {int(self.attack - (target.defense*0.2))} de dano !  | Vida do monstro |{"█"*int((target.health/10))}| {target.health}
                """)
        target.health -= int((self.attack - (target.defense*0.2)))

    def characterDefense(self):
        self.extra_defense = self.defense*0.5
        self.defense_turn = 2
        self.defense += self.extra_defense
        print(f"""
          [HEROI]
          Você defendeu-se!
          Defesa aumentada para {self.defense} DEF!
          (Duração de {self.defense_turn} Turnos)
        """)
    
    def characterExtraRemove(self):

        # REDUÇÃO DOS PONTOS DE DEFESA EXTRA
        self.defense -= self.extra_defense
        self.defense_turn -= 1
        if self.defense_turn == 0:
            print(f"""
                  
                  Pontos de DEFESA EXTRA reduzidos!
                  
                  """)
            
    def characterActionDisplay(self, target):
        rounds = 1
        while target.health > 0:
            print(f"""
          x-----------| SUA VEZ |---------------x
          |                                     |
          | [1] Atacar          [2] Defender-se |
          |                                     |
          | [3] Seu status   [4] Status inimigo |
          |                                     |
          x-------------------------------------x
""")
            try:
                action = int(input(f"""
          Escolha a opção: """))

                if action == 1:
                    self.characterAttack(target)
                    rounds += 1
                    time.sleep(2)

                elif action == 2:
                    self.characterDefense()
                    rounds += 1
                    time.sleep(2)

                elif action == 3:
                    self.characterStatus()
                    time.sleep(2)
                
                elif action == 4:
                    target.showMonsterStats()
                    time.sleep(2)


                else:
                    print("Você digitou um valor inválido! Tente novamente.")
                

                if (rounds % 2) == 0:
                    monster_action = [target.monsterAttack, target.monsterDefense]
                    sorted_action = random.choice(monster_action)
                    sorted_action()
                    rounds += 1
                    time.sleep(2)
                
                else:
                    print("Sua vez!")
                    time.sleep(2)



            except ValueError:
                print("Algo deu errado! Tente novamente")


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
    health = 200
    attack = 35
    defense = 10
    speed = 10
    level = 1
    souls = 210
    nSouls = 210
    lucky = 0
    distribuitonPoints = 0

    character = characterObject(name, health, attack, defense, speed, level, souls, nSouls, distribuitonPoints, lucky)
    return character
    
character = characterCreation() #Criação do personagem