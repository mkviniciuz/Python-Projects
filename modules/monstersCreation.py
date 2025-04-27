import os
import random

#Classe para criar monstros
class monsterType():

    def __init__(self, maxhealth, attack, defense, souls, extra_defense, defense_turn, type):


        self.type = type
        self.maxhealth = maxhealth
        self.actual_health = maxhealth
        self.attack = attack
        self.defense = defense
        self.souls = souls
        self.extra_defense = extra_defense
        self.defense_turn = defense_turn
    

    def showMonsterStats(self):
        bar = int((self.actual_health / self.maxhealth) * 20)
        print(f"""
      +{'='*38}+
      |         x STATUS DO MONSTRO x        |
      +{'='*38}+
      \______________________________________/

      
          Tipo: {self.type}
      🖤 HP: [{'█' * bar}{'░' * (20 - bar)}] {self.actual_health}/{self.maxhealth}
      ⚔️  Ataque: {self.attack:<27}
      🛡️  Defesa: {self.defense:<27}
      👻 Almas: {self.souls:<29}
      +{'='*38}+
""")
        sleeper = input("")
        os.system('cls')

    def monsterAttack(self, target):
        target.actual_health = max(0, target.actual_health - (self.attack - target.defense*0.2))
        bar = int((target.actual_health / target.maxhealth) * 20)
        print(f"""
          [MONSTRO]
          O monstro atacou!
          Você sofreu 🗡️  {int(self.attack - (target.defense*0.2))} de dano!
          
          Sua vida:
          [{'█' * bar}{'_' * (20 - bar)}] {target.actual_health:.2f}/{target.maxhealth}
                
              """)
        self.monsterExtraRemoves()
        sleeper = input("")
        os.system('cls')
        

    def monsterDefense(self, target):

        if self.defense_turn > 0:
            self.monsterAttack(target)
        
        else:
            self.extra_defense = self.defense*0.5
            self.defense_turn = 2
            self.defense += self.extra_defense
            print(f"""
          [MONSTRO]
          O Monstro defendeu-se!
          Defesa aumentada para {self.defense} DEF!
          (Duração de {self.defense_turn} Turnos)
            """)
            sleeper = input("")
            os.system('cls')
    
    def monsterExtraRemoves(self):

        # REDUÇÃO DOS PONTOS DE DEFESA EXTRA
        self.defense_turn = max(0, self.defense_turn - 1)
        if self.defense_turn == 0:
            self.defense -= self.extra_defense
            self.extra_defense = 0


#Criação de monstros aleatorios

# MONSTRO DE NIVEL BASICO
def basicMonster():

    generator = random.choice(["Slime","Goblin","Troll","Orc","Rato"])
    if generator == "Rato":

        type = "Rato"
        maxhealth=60 #Vida do monstro
        attack=16 #Ataque do monstro
        defense=0 #Defesa do monstro
        souls=120 #Almas que o monstro dropa
        extra_defense = 0
        defense_turn = 0

        monster = monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Orc":

        type = "Orc"
        maxhealth=90 #Vida do monstro
        attack=28 #Ataque do monstro
        defense=2 #Defesa do monstro
        souls=240 #Almas que o monstro dropa
        extra_defense = 0
        defense_turn = 0

        monster = monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Troll":
        type = "Troll"
        maxhealth=120 #Vida do monstro
        attack=16 #Ataque do monstro
        defense=4 #Defesa do monstro
        souls=290 #Almas que o monstro dropa
        extra_defense = 0
        defense_turn = 0

        monster = monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Goblin":
        type = "Goblin"
        maxhealth=90 #Vida do monstro
        attack=15 #Ataque do monstro
        defense=4 #Defesa do monstro
        souls=140 #Almas que o monstro dropa
        extra_defense = 0
        defense_turn = 0

        monster = monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Slime":
        type = "Slime"
        maxhealth=150 #Vida do monstro
        attack=13 #Ataque do monstro
        defense=15 #Defesa do monstro
        souls=260 #Almas que o monstro dropa
        extra_defense = 0
        defense_turn = 0

        monster = monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster

# MONSTRO DE NIVEL MEDIO
def MediumMonster():

    
    generator = random.choice(["Hydra", "Dragon Lord", "Cyclops", "Ghoul", "Blue Djinn", "Giant Spider", "Black Demon"])
    if generator == "Hydra":
        type = "Hydra"
        maxhealth=325
        attack=32
        defense=12
        souls=640
        
        extra_defense = 0
        defense_turn = 0

        monster = monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Dragon Lord":
        type = "Dragon Lord"
        maxhealth=190
        attack=22
        defense=10
        souls=690
        
        extra_defense = 0
        defense_turn = 0

        monster = monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Cyclops":
        type = "Cyclops"
        maxhealth=245
        attack=26
        defense=16
        souls=710
        
        extra_defense = 0
        defense_turn = 0

        monster = monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Ghoul":
        type = "Ghoul"
        maxhealth=210
        attack=14
        defense=13
        souls=610
        
        extra_defense = 0
        defense_turn = 0

        monster = monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Blue Djinn":
        type = "Blue Djinn"
        maxhealth=450
        attack=9
        defense=8
        souls=805
        
        extra_defense = 0
        defense_turn = 0

        monster = monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Giant Spider":
        type = "Giant Spider"
        maxhealth=90
        attack=24
        defense=11
        souls=745
        
        extra_defense = 0
        defense_turn = 0

        monster = monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Black Demon":
        type = "Black Demon"
        maxhealth=165
        attack=18
        defense=12
        souls=710
        
        extra_defense = 0
        defense_turn = 0

        monster = monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster

# MONSTRO DE NIVEL DEUS
def BossMonster():

    #PREFIXOS SEGUIDOS DO NOME DO MONSTRO NIVEL DEUS
    prefix = random.choice(["[Deus do Destino]", "[Deus do Caos]", "[Deus da Ruina]"])

    start = random.choice(["Syl","Zor","Ter","Ari","Zar","Gor","Kra", "Ka", "As"])
    middle = random.choice(["go","thar","thul","lot","kam","mi","dra", "la", "ke"])
    end = random.choice(["ylg","let", "phyr", "jar", "gsar", "iuyl", "jonl", "meth", "ladd"])


    boss_name = f"{start}{middle}{end} {prefix}"

    if prefix == "[Deus do Destino]":
        type = boss_name
        maxhealth=1000
        attack=64
        defense=45
        souls=2480
        
        extra_defense = 0
        defense_turn = 0

        monster = monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    
    elif prefix == "[Deus do Caos]":
        type = boss_name
        maxhealth=2000
        attack=32
        defense=20
        souls=2480
        
        extra_defense = 0
        defense_turn = 0

        monster = monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    
    elif prefix == "[Deus da Ruina]":
        type = boss_name
        maxhealth=980
        attack=55
        defense=50
        souls=2145
        
        extra_defense = 0
        defense_turn = 0

        monster = monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
