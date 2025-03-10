import characterObject

#Função para criar o personagem
def characterCreation():

    print("""
    x---------------------------------------------x     
    |                                             |
    |      Defina um nome para seu personagem!    |
    |                                             |
    x---------------------------------------------x
        """)

    name = input("""   --> Nome: """)
    health = 200
    attack = 10
    defense = 10
    speed = 10
    level = 1
    souls = 210
    gold = 0
    nSouls = 210
    distribuitonPoints = 0

    character = characterObject.characterObject(name, health, attack, defense, speed, level, souls, gold, nSouls, distribuitonPoints)
    return character

character = characterCreation() #Criação do personagem


#Classe para criar monstros
class monsterTypeA():

    def __init__(self, health, attack, defense, speed, souls):

        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.souls = souls
    

    def showMonsterStats(self):
        print(f"""

        |  --> Vida: {self.health}
        |  --> Ataque: {self.attack}
        |  --> Defesa: {self.defense}
        |  --> Velocidade: {self.speed}
        |  --> Almas: {self.souls}

        """)

    def monsterAttack(self):
        print(f"""

                          O monstro atacou!
          Você sofreu {self.attack - character.defense} de dano  ({self.attack} Dano base - {character.defense} Sua DEF)!

                """)
        character.health -= (self.attack - character.defense)
        print(f"""
              Vida restante:
              |{"█" * int(character.health / 12)}| {character.health}/200

              """)