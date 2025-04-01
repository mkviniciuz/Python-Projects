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
    nSouls = 210
    lucky = 0
    distribuitonPoints = 0

    character = characterObject.characterObject(name, health, attack, defense, speed, level, souls, nSouls, distribuitonPoints, lucky)
    return character

character = characterCreation() #Criação do personagem


#Classe para criar monstros
class monsterType():

    def __init__(self, health, attack, defense, souls):

        self.health = health
        self.attack = attack
        self.defense = defense
        self.souls = souls
    

    def showMonsterStats(self):
        print(f"""

        |  --> Vida: {self.health}
        |  --> Ataque: {self.attack}
        |  --> Defesa: {self.defense}
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