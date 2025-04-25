import os


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
        target.actual_health -= max(0, self.attack - target.defense*0.2)
        bar = int((target.actual_health / target.maxhealth) * 20)
        print(f"""
          [MONSTRO]
          O monstro atacou!
          Você sofreu 🗡️  {int(self.attack - (target.defense*0.2))} de dano!
          
          Sua vida:
          [{'█' * bar}{'_' * (20 - bar)}] {int(target.actual_health)}/{target.maxhealth}
                
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


