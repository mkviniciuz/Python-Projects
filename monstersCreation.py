class monsterTypeA():

    def __init__(self, health, attack, defense, speed, souls):

        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.souls = souls
    

    def showMonsterStats(self):
        print(f"""
        |---------------------------------------|
        |                                       |
        |   Vida: {self.health}                     |
        |   Ataque: {self.attack}                   |
        |   Defesa: {self.defense}                   |
        |   Velocidade: {self.speed}                |
        |   Almas: {self.souls}                      |
        |                                       |
        |---------------------------------------|
        """)