import json
from modules import monstersCreation
from modules import characterObject
import random
import time
import os

os.system('cls')


def gameEvents(target, enemy):

    
    def eventSouls(target):
        character_luckyEffect = int(target.lucky * 0.15) #Efeito da sorte do personagem

        dice_roll = random.randint(1, 20) + character_luckyEffect #Rolar um dado de 20 lados e adicionar o efeito da sorte do personagem

        #Evento rank S (100% a mais de almas necessarias)
        if dice_roll >= 20:
            
            eBonus = int(target.nSouls + target.nSouls) #Calculo de almas ganhas
            message = f"""
          x EVENTO DE SORTE x (RANK S)     
          |     
          |   Você recebeu {eBonus} almas!
                """ #Mensagem de evento de sorte
            target.souls += eBonus #Adiciona as almas ganhas ao personagem
            return message


        #Evento rank A (75% a mais de almas necessarias)
        elif dice_roll >= 15:
            eBonus = int(target.nSouls + (target.nSouls * 0.75)) #Calculo de almas ganhas
            message = f"""
          x EVENTO DE SORTE x (RANK A)    
          |     
          |   Você recebeu {eBonus} almas!
                """ #Mensagem de evento de sorte
            target.souls += eBonus #Adiciona as almas ganhas ao personagem
            return message

        #Evento rank B (50% a mais de almas necessarias)
        elif dice_roll >= 13:
            eBonus = int(target.nSouls + (target.nSouls * 0.50)) #Calculo de almas ganhas
            message = f"""
          x EVENTO DE SORTE x (RANK B)  
          |     
          |   Você recebeu {eBonus} almas!
                """ #Mensagem de evento de sorte
            target.souls += eBonus #Adiciona as almas ganhas ao personagem
            return message

        #Evento rank C (25% a mais de almas necessarias)
        elif dice_roll >= 10:
            eBonus = int(target.nSouls + (target.nSouls * 0.25))
            message = f"""
          x EVENTO DE SORTE x (RANK C)
          |     
          |   Você recebeu {eBonus} almas!
                """
            target.souls += eBonus #Adiciona as almas ganhas ao personagem
            return message

        #Evento rank D (-15% a mais de almas necessarias)
        elif dice_roll <= 5:
            eBonus = int(target.nSouls * 0.15) #Calculo de almas perdidas
            message = f"""
          x EVENTO DE AZAR x (RANK D)
          |     
          |   Você perdeu {eBonus} almas!
                """ #Mensagem de evento de azar
            target.souls = max(0, target.souls - eBonus) #Remove as almas ganhas ao personagem
            return message

        #Evento rank D (-30% a mais de almas necessarias)
        elif dice_roll <= 0:

            eBonus = int(target.nSouls + (target.nSouls * 0.15)) #Calculo de almas perdidas
            message = f"""
          x EVENTO DE AZAR x (RANK E)
          |     
          |   Você perdeu {eBonus} almas!
                """ #Mensagem de evento de azar
            target.souls = max(0, target.souls - eBonus) #Remove as almas ganhas ao personagem
            return message
        
        else:
            message = f"""
          x EVENTO DE SORTE x (RANK F)
          |
          |   Nada aconteceu!
                """ #Mensagem de evento de sorte
            target.souls += 0 #Adiciona as almas ganhas ao personagem
            return message
        
    def eventStatus(target):

        statusList = ["ATAQUE", "DEFESA", "SORTE", "VIDA", "AZAR"] #Lista de status
        selectedStatus = random.choice(statusList) #Seleciona um status aleatorio


        character_luckyEffect = int(target.lucky * 15) / 100 #Efeito da sorte do personagem
        dice_roll = random.randint(1, 20) + character_luckyEffect #Rolar um dado de 20 lados

        if selectedStatus == "ATAQUE":

            if dice_roll >= 20: 
                eBonus = int(10 * (target.maxhealth / 100)) #Calculo de bonus
                message = f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """
                target.attack += eBonus #Adiciona o bonus ao status
                return message
            

            elif dice_roll >= 15 and dice_roll < 20: 
                eBonus = int(5 * (target.maxhealth / 100)) #Calculo de bonus
                message = f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """
                target.attack += eBonus #Adiciona o bonus ao status
                return message
            
            
            elif dice_roll < 15:

                eBonus = int(2.5 * (target.maxhealth / 100)) #Calculo de bonus
                message = f"""                                                                                
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """
                target.attack += eBonus #Adiciona o bonus ao status
                return message
            
        elif selectedStatus == "DEFESA":

            if dice_roll >= 20: 
                eBonus = int(10 * (target.maxhealth / 100)) #Calculo de bonus
                message = f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """
                target.defense += eBonus #Adiciona o bonus ao status
                return message
            

            elif dice_roll >= 15 and dice_roll < 20: 
                eBonus = int(5 * (target.maxhealth / 100)) #Calculo de bonus
                message = f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """
                target.defense += eBonus #Adiciona o bonus ao status
                return message
            
            
            elif dice_roll < 15:

                eBonus = int(2.5 * (target.maxhealth / 100)) #Calculo de bonus
                message = f"""                                                                           
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """
                target.defense += eBonus #Adiciona o bonus ao status
                return message

        elif selectedStatus == "SORTE":
            
            if dice_roll >= 20: 
                eBonus = int(10 * (target.maxhealth / 100)) #Calculo de bonus
                message = f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """
                target.lucky += eBonus #Adiciona o bonus ao status
                return message
            

            elif dice_roll >= 15 and dice_roll < 20: 
                eBonus = int(5 * (target.maxhealth / 100)) #Calculo de bonus
                message = f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """
                target.lucky += eBonus #Adiciona o bonus ao status
                return message
            
            
            elif dice_roll < 15:

                eBonus = int(2.5 * (target.maxhealth / 100)) #Calculo de bonus
                message = f"""                                                                                  
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """
                target.lucky += eBonus #Adiciona o bonus ao status
                return message

        elif selectedStatus == "VIDA":

            if dice_roll >= 20: 
                eBonus = int(10 * (target.maxhealth / 100)) #Calculo de bonus
                message = f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """
                target.maxhealth += eBonus #Adiciona o bonus ao status
                return message
            

            elif dice_roll >= 15 and dice_roll < 20: 
                eBonus = int(5 * (target.maxhealth / 100)) #Calculo de bonus
                message = f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!  
                    """
                target.maxhealth += eBonus #Adiciona o bonus ao status
                return message
            
            
            elif dice_roll < 15:

                eBonus = int(2.5 * (target.maxhealth / 100)) #Calculo de bonus
                message = f"""                                                                                   
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """
                target.maxhealth += eBonus #Adiciona o bonus ao status
                return message
            
        else:
            message = f"""
          x EVENTO DE SORTE x
          |
          |   Nada aconteceu!
                """ #Mensagem de evento de sorte
            target.souls += 0 #Adiciona as almas ganhas ao personagem
            return message
        
    def eventMonster(enemy):

        with open("data/eventMessages.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        eventWin = random.choice(data["ganho"]) #Evento de ganho
        eventLose = random.choice(data["perda"]) #Evento de perda
        eventList = [eventWin, eventLose] #Lista de eventos
        selectedEvent = random.choice(eventList) # Seleciona um evento aleatorio

        statusList = ["VIDA", "ATAQUE", "DEFESA"] #Lista de status do monstro
        eStatus = random.choice(statusList) #Seleciona um status aleatorio do monstro para ser alterado
        eBonus = int(10 * (enemy.maxhealth / 100)) #Calculo de bonus

        final_event = selectedEvent.format(eBonus=eBonus, eStatus=eStatus) #Formata a string com o status do monstro


        if selectedEvent == eventWin:

            if eStatus == "VIDA":
                enemy.maxhealth += eBonus
                enemy.actual_health = enemy.maxhealth
                message = f"""
          x EVENTO DE MONSTRO x
          |
          |    {final_event}
                    """
                return message
                
            elif eStatus == "ATAQUE":
                enemy.attack += eBonus
                message = f"""
          x EVENTO DE MONSTRO x
          |
          |    {final_event}
                    """
                return message
            
            elif eStatus == "DEFESA":
                enemy.defense += eBonus
                message = f"""
          x EVENTO DE MONSTRO x
          |
          |    {final_event}
                    """
                return message


        elif selectedEvent == eventLose:

            if eStatus == "VIDA":
                enemy.actual_health = max(0, enemy.actual_health - eBonus)
                message = f"""
          x EVENTO DE MONSTRO x
          |
          |    {final_event}
                    """
                return message
                
            elif eStatus == "ATAQUE":
                enemy.attack = max(0, enemy.attack - eBonus)
                message = f"""
          x EVENTO DE MONSTRO x
          |
          |    {final_event}
                    """
                return message
            
            elif eStatus == "DEFESA":
                enemy.defense = max(0, enemy.defense - eBonus)
                message = f"""
          x EVENTO DE MONSTRO x
          |
          |    {final_event}
                    """
                return message
                    
    events = [eventSouls, eventStatus, eventMonster] #Lista de eventos
    selectedEvent = random.choice(events) #Seleciona um evento aleatorio

    if selectedEvent != eventMonster:
        return selectedEvent(target)
        
    if selectedEvent == eventMonster:
        return selectedEvent(enemy)
def cardShopping(character, target, round):

    def pactoNeorato(character, target):
        message = f"""
            [GANHO]
            A cada andar o portador regenera +5% da vida atual -> (+{int(character.actual_health*0.05)} HP)

            [PERDA]
            Monstros do tipo rato tem seus status aumentados em 4x
                """
        character.actual_health += int(character.actual_health*0.05)

        if target.type == "Rato":
            target.type = "Neorato [MUTADO]"
            target.maxhealth *= 4
            target.actual_health = target.maxhealth
            target.attack *= 4
            target.defense *= 4
            target.souls *= 4
        return message

    def ultimoSuspiro(character, target, round):

        message = f"""
            [GANHO]
            Ao atingir -15% da sua VIDA, regenera +2% VIDA -> (+{int(character.actual_health*0.02)} HP por rodada)

            [PERDA]
            Todos os monstros ganham +15% de VIDA MAXIMA -> (+{int(target.maxhealth*0.15)} HP do monstro)
                """
        round_needed = 1

        if round == round_needed:
            if character.actual_health <= character.maxhealth*0.15:
                character.actual_health += character.maxhealth*0.02
                round_needed += 1

        if round == 1:
            target.maxhealth += target.maxhealth*0.15

        return message

    def tratoSanguinario(character):
        message = f"""
            [GANHO]
            Seu ataque é escalado com 35% do seu HP maximo -> ({int(character.maxhealth*0.35)} ATAQUE)
            (Melhorar o ataque não funcionará mais!)

            [PERDA]
            Você sua defesa é reduzida para +(0)DEF Permanentemente
                """
        
        character.attack = int(character.maxhealth*0.35)
        character.defense = 0
        return message

    def sentencaFinal( target):
        message = f"""
            [GANHO]
            Caso o monstro tenha -20% de VIDA, ele é finalizado

            [PERDA]
            Monstros de nivel SEMI-DEUS tem VIDA MÁXIMA aumentada em +20%
                """
        avaibleMonsters = ["Hydra", "Dragon Lord", "Cyclops", "Ghoul", "Blue Djinn", "Giant Spider", "Black Demon"]

        if target.type in avaibleMonsters:
            target.maxhealth += int(target.maxhealth*0.2)

        if target.actual_health <= target.maxhealth*0.2:
            target.actual_health = 0
        return message


    cards = ["""
        [ATAQUE]    
    X--------------X
    |              |
    |     ZZZZ     |
    |      TT      |
    |      ||      |
    |      ||      |
    |   ========   |
    |     |  |     |
    X--------------X
    """.splitlines(),

    """
        [DEFESA]    
    X--------------X
    |              |
    |  .________.  |
    |  |        |  |
    |  |        |  |
    |  |.      .|  |
    |   \.    ./   |
    |    ▬▬▬▬▬▬    |
    X--------------X
    """.splitlines(),

    """
        [VIDA]     
    X--------------X
    |  ___   ___   |
    | /   \./   \  |
    | |         |  |
    |  \       /   |
    |   \     /    |
    |    \   /     |
    |     \./      |
    X--------------X
    """.splitlines(),

    """
    [SORTE/AZAR]  
    X--------------X
    |              |
    |     ZZZZ     |
    |   xxZZZxZ    |
    | ZZZx ○ ZZZZ  |
    |   xx / ZZZ   |
    |     /        |
    |   _/         |
    X--------------X
    """.splitlines()]
    random_cards = [random.choice(cards) for _ in range(3)]

    deck = []
    disposs_cards = []
    pointsRequimerent = []

    with open("data/cardsEvents.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for item in random_cards:
        if item == cards[0]:
            disposs_cards.append(random.choice(data["ATAQUE"]))
            pointsRequimerent.append(random.randint(5, 15))

        elif item == cards[1]:
            disposs_cards.append(random.choice(data["ATAQUE"]))
            pointsRequimerent.append(random.randint(5, 15))

        elif item == cards[2]:
            disposs_cards.append(random.choice(data["VIDA"]))
            pointsRequimerent.append(random.randint(5, 15))

        elif item == cards[3]:
            disposs_cards.append(random.choice(data["VIDA"]))
            pointsRequimerent.append(random.randint(5, 15))

    deck.append(disposs_cards)
    deck.append(pointsRequimerent)


    # FAZER VINCULAÇÃO COM ATRIBUTO DO PERSONAGEM
    # FAZER VINCULAÇÃO COM PONTOS DO PERSONAGEM

    while True:
        try:
            print(f"""
    +{'='*51}+
    | Troque seus pontos por cartas, [{character.distribuitonPoints}] Pontos atual! |
    +{'='*51}+
    \_________________________________________________/
            """)

            for linhas in zip(*random_cards):
                print("   ".join(linhas))
            choose = int(input(f"""
    [1]~{deck[0][0]} -> {deck[1][0]} Pontos  
    [2]~{deck[0][1]} -> {deck[1][1]} Pontos  
    [3]~{deck[0][2]} -> {deck[1][2]} Pontos
    [4]~Sair
                            
                                            

        ESCOLHA: """))
            if choose == 1:
                if character.distribuitonPoints < deck[1][0]:
                    print("""
                
        [ERROR]
        Você não tem pontos o suficiente!
                
                        """)
                    sleeper = input("")
                    os.system('cls')
                    continue
                else:
                    
                    confirm = int(input(f"""
                
        [CONFIRMAÇÃO]
        Você deseja adquirir [{deck[0][0]}] por {deck[1][0]} Pontos?

        Escolha [1]Sim / [2]Não: """))
            
                    if confirm == 1:
                        print(f"""

        {deck[0][0]} foi adicionado ao seu DECK!
                                """)
                        character.deck.append(deck[0][0])
                        character.distribuitonPoints -= deck[1][0]
                        sleeper = input("")
                        os.system('cls')
                        

            elif choose == 2:
                if character.distribuitonPoints < deck[1][1]:
                    print("""
                
        [ERROR]
        Você não tem pontos o suficiente!
                
                        """)
                    sleeper = input("")
                    os.system('cls')
                    continue
                else:
                    
                    confirm = int(input(f"""
                
        [CONFIRMAÇÃO]
        Você deseja adquirir [{deck[0][1]}] por {deck[1][1]} Pontos?

        Escolha [1]Sim / [2]Não: """))
            
                    if confirm == 1:
                        print(f"""

        {deck[0][1]} foi adicionado ao seu DECK!
                                """)
                        character.deck.append(deck[0][1])
                        character.distribuitonPoints -= deck[1][1]
                        sleeper = input("")
                        os.system('cls')

            elif choose == 3:
                if character.distribuitonPoints < deck[1][2]:
                    print("""
                
        [ERROR]
        Você não tem pontos o suficiente!
                
                        """)
                    sleeper = input("")
                    os.system('cls')
                    continue
                else:
                    
                    confirm = int(input(f"""
                
        [CONFIRMAÇÃO]
        Você deseja adquirir [{deck[0][2]}] por {deck[1][2]} Pontos?

        Escolha [1]Sim / [2]Não: """))
            
                    if confirm == 1:
                        print(f"""

        {deck[0][2]} foi adicionado ao seu DECK!
                                """)
                        character.deck.append(deck[0][2])
                        character.distribuitonPoints -= int(deck[1][2])
                        sleeper = input("")
                        os.system('cls')
            
            else:
                os.system('cls')
                break
        except ValueError:
            print("Algo deu errado!")



#Criação de monstros aleatorios 
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

        monster = monstersCreation.monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Orc":

        type = "Orc"
        maxhealth=90 #Vida do monstro
        attack=28 #Ataque do monstro
        defense=2 #Defesa do monstro
        souls=240 #Almas que o monstro dropa
        extra_defense = 0
        defense_turn = 0

        monster = monstersCreation.monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Troll":
        type = "Troll"
        maxhealth=120 #Vida do monstro
        attack=16 #Ataque do monstro
        defense=4 #Defesa do monstro
        souls=290 #Almas que o monstro dropa
        extra_defense = 0
        defense_turn = 0

        monster = monstersCreation.monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Goblin":
        type = "Goblin"
        maxhealth=90 #Vida do monstro
        attack=15 #Ataque do monstro
        defense=4 #Defesa do monstro
        souls=140 #Almas que o monstro dropa
        extra_defense = 0
        defense_turn = 0

        monster = monstersCreation.monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Slime":
        type = "Slime"
        maxhealth=150 #Vida do monstro
        attack=13 #Ataque do monstro
        defense=15 #Defesa do monstro
        souls=260 #Almas que o monstro dropa
        extra_defense = 0
        defense_turn = 0

        monster = monstersCreation.monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster

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

        monster = monstersCreation.monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Dragon Lord":
        type = "Dragon Lord"
        maxhealth=190
        attack=22
        defense=10
        souls=690
        
        extra_defense = 0
        defense_turn = 0

        monster = monstersCreation.monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Cyclops":
        type = "Cyclops"
        maxhealth=245
        attack=26
        defense=16
        souls=710
        
        extra_defense = 0
        defense_turn = 0

        monster = monstersCreation.monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Ghoul":
        type = "Ghoul"
        maxhealth=210
        attack=14
        defense=13
        souls=610
        
        extra_defense = 0
        defense_turn = 0

        monster = monstersCreation.monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Blue Djinn":
        type = "Blue Djinn"
        maxhealth=450
        attack=9
        defense=8
        souls=805
        
        extra_defense = 0
        defense_turn = 0

        monster = monstersCreation.monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Giant Spider":
        type = "Giant Spider"
        maxhealth=90
        attack=24
        defense=11
        souls=745
        
        extra_defense = 0
        defense_turn = 0

        monster = monstersCreation.monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster
    elif generator == "Black Demon":
        type = "Black Demon"
        maxhealth=165
        attack=18
        defense=12
        souls=710
        
        extra_defense = 0
        defense_turn = 0

        monster = monstersCreation.monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
        return monster

def BossMonster(target):
    type = "Deus"
    maxhealth=random.randint(int(target.maxhealth * 4), int(target.maxhealth * 5)) #Vida do monstro baseada na vida do personagem
    attack=random.randint(int(target.attack * 1.30), int(target.attack * 1.8)) #Ataque do monstro baseado no ataque do personagem
    defense=random.randint(int(target.defense * 1.2), int(target.defense * 1.6)) #Defesa do monstro baseada na defesa do personagem
    souls=random.randint(int(target.nSouls), int(target.nSouls * 4)) #Almas que o monstro dropa baseado na quantidade de almas necessarias para upar
    extra_defense = 0
    defense_turn = 0

    monster = monstersCreation.monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn, type)
    return monster


def battleSystem():

    character = characterObject.characterCreation()
    
    monsterkilled = 0
    tower_level = 1

    playing = True

    boss_level = 10
    semigod_level = 3
    cards_shop_level = 9
    fight_round = 0
    


    while playing:

        

        while tower_level != semigod_level and tower_level != boss_level:
            monster = basicMonster()
            actual_event = gameEvents(character, monster)
            print(actual_event)
            character.action_display(monster, actual_event, monsterkilled)
            tower_level += 1
            monsterkilled += 1
            

        if tower_level == cards_shop_level:
                cardShopping(character, monster, fight_round)
                cards_shop_level += 10

        if tower_level == semigod_level:
            print(f"""
          \033[45m[SEMI-DEUS]\033[0m
                  
          Um monstro nivel \033[95mSEMI-DEUS\033[0m apareceu!
          enfrete-o e colete suas recompensas
""")
            monster = MediumMonster()
            actual_event = gameEvents(character, monster)
            print(actual_event)
            character.action_display(monster, actual_event, monsterkilled)
            character.level_upgrade()
            tower_level += 1
            monsterkilled += 1
            semigod_level += 3
            
        
        

        if tower_level == boss_level:
            print(f"""
          \033[103m[DEUS]\033[0m
          Um monstro nivel \033[93mDEUS\033[0m apareceu!
          enfrete-o e receba suas recompensas
""")
            monster = basicMonster()
            actual_event = gameEvents(character, monster)
            print(actual_event)
            character.action_display(monster, actual_event, monsterkilled)
            tower_level += 1
            boss_level += 10


battleSystem()


def main():
    playing = True
    while playing:
        try:
            print(f"""
            x Narrador x
            |
            | Find your lost SOUL!
            | This is your unique chance, {character.name}. Welcome to the Cursed Tower!
                    """)
            
            time.sleep(1)

            print(f"""
            x Narrador x
            |
            | You are in the first floor of the Cursed Tower, {character.name}.
            """)

            time.sleep(1)

            time.sleep(4)

        except ValueError:
            print("Você morreu!")
            playing = False
            break