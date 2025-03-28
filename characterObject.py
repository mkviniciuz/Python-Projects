class characterObject(object):  # Inherit from object


    def __init__(self, name, health, attack, defense, speed, level, souls, gold, nSouls, distribuitonPoints, lucky):
        self.name = name #Nome do personagem
        self.health = health #Vida do personagem
        self.attack = attack #Ataque do personagem
        self.defense = defense #Defesa do personagem
        self.speed = speed #Velocidade do personagem
        self.level = level #Nivel do personagem
        self.souls = souls #Quantidade de almas que o personagem possui
        self.gold = gold #Quantidade de ouro que o personagem possui
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

                Você atacou!
          Você infligiu {int(self.attack - (target.defense*0.2))} de dano !

                """)
        target.health -= int((self.attack - (target.defense*0.2)))