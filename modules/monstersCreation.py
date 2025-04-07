from modules import characterObject

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

    character = characterObject.characterObject(name, health, attack, defense, speed, level, souls, nSouls, distribuitonPoints, lucky)
    return character

character = characterCreation() #Criação do personagem


#Classe para criar monstros
class monsterType():

    def __init__(self, health, attack, defense, souls, extra_defense, defense_turn):

        self.health = health
        self.attack = attack
        self.defense = defense
        self.souls = souls
        self.extra_defense = extra_defense
        self.defense_turn = defense_turn
    

    def showMonsterStats(self):
        print(f"""
          x-------| STATUS MONSTRO
          |  --> Vida: {self.health}
          |  --> Ataque: {self.attack}
          |  --> Defesa: {self.defense} +[{self.extra_defense}] EXTRA DEF | Acaba em [{self.defense_turn}] Turnos
          |  --> Almas: {self.souls}
        """)

    def monsterAttack(self):
        print(f"""
          [MONSTRO]
          O monstro atacou!
          Você sofreu {max(0, self.attack - character.defense)} de dano  ({self.attack} Dano base - {character.defense} Sua DEF)! | Sua vida |{"█"*int((character.health/10))}| {character.health}
                """)
        character.health -= max(0, self.attack - character.defense)
        if self.defense_turn > 0:
            self.monsterExtraRemoves()
        

    def monsterDefense(self):

        if self.defense_turn > 0:
            self.monsterAttack()
        
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
    
    def monsterExtraRemoves(self):

        # REDUÇÃO DOS PONTOS DE DEFESA EXTRA
        self.defense_turn = max(0, self.defense_turn - 1)
        if self.defense_turn == 0:
            self.defense -= self.extra_defense
            self.extra_defense = 0


