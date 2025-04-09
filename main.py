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
            print(f"""
          x EVENTO DE SORTE x (RANK S)     
          |     
          |   Você recebeu {eBonus} almas!
                """) #Mensagem de evento de sorte
            target.souls += eBonus #Adiciona as almas ganhas ao personagem
            return target.souls


        #Evento rank A (75% a mais de almas necessarias)
        elif dice_roll >= 15:
            eBonus = int(target.nSouls + (target.nSouls * 0.75)) #Calculo de almas ganhas
            print(f"""
          x EVENTO DE SORTE x (RANK A)    
          |     
          |   Você recebeu {eBonus} almas!
                """) #Mensagem de evento de sorte
            target.souls += eBonus #Adiciona as almas ganhas ao personagem
            return target.souls

        #Evento rank B (50% a mais de almas necessarias)
        elif dice_roll >= 13:
            eBonus = int(target.nSouls + (target.nSouls * 0.50)) #Calculo de almas ganhas
            print(f"""
          x EVENTO DE SORTE x (RANK B)  
          |     
          |   Você recebeu {eBonus} almas!
                """) #Mensagem de evento de sorte
            target.souls += eBonus #Adiciona as almas ganhas ao personagem
            return target.souls

        #Evento rank C (25% a mais de almas necessarias)
        elif dice_roll >= 10:
            eBonus = int(target.nSouls + (target.nSouls * 0.25))
            print(f"""
          x EVENTO DE SORTE x (RANK C)
          |     
          |   Você recebeu {eBonus} almas!
                """)
            target.souls += eBonus #Adiciona as almas ganhas ao personagem
            return target.souls

        #Evento rank D (-15% a mais de almas necessarias)
        elif dice_roll <= 5:
            eBonus = int(target.nSouls * 0.15) #Calculo de almas perdidas
            print(f"""
          x EVENTO DE AZAR x (RANK D)
          |     
          |   Você perdeu {eBonus} almas!
                """) #Mensagem de evento de azar
            target.souls = max(0, target.souls - eBonus) #Remove as almas ganhas ao personagem
            return target.souls

        #Evento rank D (-30% a mais de almas necessarias)
        elif dice_roll <= 0:

            eBonus = int(target.nSouls + (target.nSouls * 0.15)) #Calculo de almas perdidas
            print(f"""
          x EVENTO DE AZAR x (RANK E)
          |     
          |   Você perdeu {eBonus} almas!
                """) #Mensagem de evento de azar
            target.souls = max(0, target.souls - eBonus) #Remove as almas ganhas ao personagem
            return target.souls
        
        else:
            print(f"""
          x EVENTO DE SORTE x (RANK F)
          |
          |   Nada aconteceu!
                """) #Mensagem de evento de sorte
            target.souls += 0 #Adiciona as almas ganhas ao personagem
            return target.souls
        
    def eventStatus(target):

        statusList = ["ATAQUE", "DEFESA", "SORTE", "VIDA", "AZAR"] #Lista de status
        selectedStatus = random.choice(statusList) #Seleciona um status aleatorio


        character_luckyEffect = int(target.lucky * 15) / 100 #Efeito da sorte do personagem
        dice_roll = random.randint(1, 20) + character_luckyEffect #Rolar um dado de 20 lados

        if selectedStatus == "ATAQUE":

            if dice_roll >= 20: 
                eBonus = int(10 * (target.maxhealth / 100)) #Calculo de bonus
                print(f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """)
                target.attack += eBonus #Adiciona o bonus ao status
                return target.attack
            

            elif dice_roll >= 15 and dice_roll < 20: 
                eBonus = int(5 * (target.maxhealth / 100)) #Calculo de bonus
                print(f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """)
                target.attack += eBonus #Adiciona o bonus ao status
                return target.attack
            
            
            elif dice_roll < 15:

                eBonus = int(2.5 * (target.maxhealth / 100)) #Calculo de bonus
                print(f"""                                                                                
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """)
                target.attack += eBonus #Adiciona o bonus ao status
                return target.attack
            
        elif selectedStatus == "DEFESA":

            if dice_roll >= 20: 
                eBonus = int(10 * (target.maxhealth / 100)) #Calculo de bonus
                print(f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """)
                target.defense += eBonus #Adiciona o bonus ao status
                return target.defense
            

            elif dice_roll >= 15 and dice_roll < 20: 
                eBonus = int(5 * (target.maxhealth / 100)) #Calculo de bonus
                print(f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """)
                target.defense += eBonus #Adiciona o bonus ao status
                return target.defense
            
            
            elif dice_roll < 15:

                eBonus = int(2.5 * (target.maxhealth / 100)) #Calculo de bonus
                print(f"""                                                                           
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """)
                target.defense += eBonus #Adiciona o bonus ao status
                return target.defense

        elif selectedStatus == "SORTE":
            
            if dice_roll >= 20: 
                eBonus = int(10 * (target.maxhealth / 100)) #Calculo de bonus
                print(f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """)
                target.lucky += eBonus #Adiciona o bonus ao status
                return target.lucky
            

            elif dice_roll >= 15 and dice_roll < 20: 
                eBonus = int(5 * (target.maxhealth / 100)) #Calculo de bonus
                print(f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """)
                target.lucky += eBonus #Adiciona o bonus ao status
                return target.lucky
            
            
            elif dice_roll < 15:

                eBonus = int(2.5 * (target.maxhealth / 100)) #Calculo de bonus
                print(f"""                                                                                  
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """)
                target.lucky += eBonus #Adiciona o bonus ao status
                return target.lucky

        elif selectedStatus == "VIDA":

            if dice_roll >= 20: 
                eBonus = int(10 * (target.maxhealth / 100)) #Calculo de bonus
                print(f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """)
                target.maxhealth += eBonus #Adiciona o bonus ao status
                return target.maxhealth
            

            elif dice_roll >= 15 and dice_roll < 20: 
                eBonus = int(5 * (target.maxhealth / 100)) #Calculo de bonus
                print(f"""
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!  
                    """)
                target.maxhealth += eBonus #Adiciona o bonus ao status
                return target.maxhealth
            
            
            elif dice_roll < 15:

                eBonus = int(2.5 * (target.maxhealth / 100)) #Calculo de bonus
                print(f"""                                                                                   
          x EVENTO DE STATUS x
          |     
          |   O status {selectedStatus} aumentou em {eBonus}!
                    """)
                target.maxhealth += eBonus #Adiciona o bonus ao status
                return target.maxhealth
            
        else:
            print(f"""
          x EVENTO DE SORTE x
          |
          |   Nada aconteceu!
                """) #Mensagem de evento de sorte
            target.souls += 0 #Adiciona as almas ganhas ao personagem
            return target.souls
        
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
                print(f"""
          x EVENTO DE MONSTRO x
          |
          |    {final_event}
                    """)
                return enemy.maxhealth, enemy.actual_health
                
            elif eStatus == "ATAQUE":
                enemy.attack += eBonus
                print(f"""
          x EVENTO DE MONSTRO x
          |
          |    {final_event}
                    """)
                return enemy.attack
            
            elif eStatus == "DEFESA":
                enemy.defense += eBonus
                print(f"""
          x EVENTO DE MONSTRO x
          |
          |    {final_event}
                    """)
                return enemy.defense


        elif selectedEvent == eventLose:

            if eStatus == "VIDA":
                enemy.actual_health = max(0, enemy.actual_health - eBonus)
                print(f"""
          x EVENTO DE MONSTRO x
          |
          |    {final_event}
                    """)
                return enemy.actual_health
                
            elif eStatus == "ATAQUE":
                enemy.attack = max(0, enemy.attack - eBonus)
                print(f"""
          x EVENTO DE MONSTRO x
          |
          |    {final_event}
                    """)
                return enemy.attack
            
            elif eStatus == "DEFESA":
                enemy.defense = max(0, enemy.defense - eBonus)
                print(f"""
          x EVENTO DE MONSTRO x
          |
          |    {final_event}
                    """)
                return enemy.defense
                    
    events = [eventSouls, eventStatus, eventMonster] #Lista de eventos
    selectedEvent = random.choice(events) #Seleciona um evento aleatorio

    if selectedEvent != eventMonster:
        selectedEvent(target)
    if selectedEvent == eventMonster:
        selectedEvent(enemy)


#Criação de monstros aleatorios
def basicMonster(target):
    maxhealth=random.randint(int(target.maxhealth * 0.5), int(target.maxhealth * 0.75)) #Vida do monstro baseada na vida do personagem
    attack=random.randint(int(target.attack * 0.5), int(target.attack * 0.75)) #Ataque do monstro baseado no ataque do personagem
    defense=random.randint(int(target.defense * 0.3), int(target.defense * 0.5)) #Defesa do monstro baseada na defesa do personagem
    souls=random.randint(int(target.nSouls / 5), int(target.nSouls / 3)) #Almas que o monstro dropa baseado na quantidade de almas necessarias para upar
    extra_defense = 0
    defense_turn = 0

    monster = monstersCreation.monsterType(maxhealth, attack, defense, souls, extra_defense, defense_turn)
    return monster


def battleSystem():

    character = characterObject.characterCreation()
    monster = basicMonster(character)
    

    tower_level = 1

    playing = True

    boss_level = 10
    semigod_level = 3
    


    while playing:

        while tower_level != semigod_level and tower_level != boss_level:
            monster = basicMonster(character)
            gameEvents(character, monster)
            character.action_display(monster)
            tower_level += 1

        if tower_level == semigod_level:
            monster = basicMonster(character)
            gameEvents(character, monster)
            character.action_display(monster)
            tower_level += 1
            semigod_level += 3

        if tower_level == boss_level:
            monster = basicMonster(character)
            gameEvents(character, monster)
            character.action_display(monster)
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