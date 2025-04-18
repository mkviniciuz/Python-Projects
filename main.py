import json
from modules import monstersCreation
from modules import characterObject
import random
import time
import os

os.system('cls')


def gameEvents(target, enemy):

    target
    enemy
    
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

def BossMonter(target):
    maxhealth=random.randint(int(target.maxhealth * 4), int(target.maxhealth * 5)) #Vida do monstro baseada na vida do personagem
    attack=random.randint(int(target.attack * 1.30), int(target.attack * 1.8)) #Ataque do monstro baseado no ataque do personagem
    defense=random.randint(int(target.defense * 1.2), int(target.defense * 1.6)) #Defesa do monstro baseada na defesa do personagem
    souls=random.randint(int(target.nSouls), int(target.nSouls * 4)) #Almas que o monstro dropa baseado na quantidade de almas necessarias para upar
    extra_defense = 0
    defense_turn = 0

    monster = monstersCreation.monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn)
    return monster


def battleSystem():

    character = characterObject.characterCreation()
    
    monsterkilled = 0
    tower_level = 1

    playing = True

    boss_level = 10
    semigod_level = 3
    


    while playing:

        

        while tower_level != semigod_level and tower_level != boss_level:
            monster = basicMonster()
            actual_event = gameEvents(character, monster)
            print(actual_event)
            character.action_display(monster, actual_event, monsterkilled)
            tower_level += 1
            monsterkilled += 1

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
            tower_level += 1
            monsterkilled += 1
            semigod_level += 3
            character.level_upgrade()

        if tower_level == boss_level:
            print(f"""
          \033[103m[EVENTO]\033[0m
          Um monstro nivel DEUS apareceu!
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