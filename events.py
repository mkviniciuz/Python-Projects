import json
import random
from monstersCreation import character
from main import monster

#Tabela de RANKS
# S - 100%
# A - 75%
# B - 50%
# C - 25%
# D - -15%
# E - -30%
# F - 0% (Nada acontece)

def gameEvents():
    
    def eventSouls():
        character_luckyEffect = int(character.lucky * 15) / 100 #Efeito da sorte do personagem

        dice_roll = random.randint(1, 20) + character_luckyEffect #Rolar um dado de 20 lados e adicionar o efeito da sorte do personagem

        #Evento rank S (100% a mais de almas necessarias)
        if dice_roll >= 20:
            
            eBonus = int(character.nSouls + (character.nSouls * 1)) #Calculo de almas ganhas
            print(f"""

            x EVENTO DE SORTE x (RANK S)     
            |     
            |   Você recebeu {eBonus} almas!
                
                """) #Mensagem de evento de sorte
            character.souls += eBonus #Adiciona as almas ganhas ao personagem
            return character.souls


        #Evento rank A (75% a mais de almas necessarias)
        elif dice_roll >= 15:
            eBonus = int(character.nSouls + (character.nSouls * 0.75)) #Calculo de almas ganhas
            print(f"""

            x EVENTO DE SORTE x (RANK A)    
            |     
            |   Você recebeu {eBonus} almas!
                
                """) #Mensagem de evento de sorte
            character.souls += eBonus #Adiciona as almas ganhas ao personagem
            return character.souls

        #Evento rank B (50% a mais de almas necessarias)
        elif dice_roll >= 13:
            eBonus = int(character.nSouls + (character.nSouls * 0.50)) #Calculo de almas ganhas
            print(f"""

            x EVENTO DE SORTE x (RANK B)  
            |     
            |   Você recebeu {eBonus} almas!
                
                """) #Mensagem de evento de sorte
            character.souls += eBonus #Adiciona as almas ganhas ao personagem
            return character.souls

        #Evento rank C (25% a mais de almas necessarias)
        elif dice_roll >= 10:
            eBonus = int(character.nSouls + (character.nSouls * 0.25))
            print(f"""

            x EVENTO DE SORTE x (RANK C)
            |     
            |   Você recebeu {eBonus} almas!
                
                """)
            character.souls += eBonus #Adiciona as almas ganhas ao personagem
            return character.souls

        #Evento rank D (-15% a mais de almas necessarias)
        elif dice_roll <= 5:
            eBonus = int(character.nSouls + (character.nSouls * 0.15)) #Calculo de almas perdidas
            print(f"""

            x EVENTO DE AZAR x (RANK D)
            |     
            |   Você recebeu {eBonus} almas!
                
                """) #Mensagem de evento de azar
            character.souls -= eBonus #Remove as almas ganhas ao personagem
            return character.souls

        #Evento rank D (-30% a mais de almas necessarias)
        elif dice_roll <= 0:

            eBonus = int(character.nSouls + (character.nSouls * 0.15)) #Calculo de almas perdidas
            print(f"""

            x EVENTO DE AZAR x (RANK E)
            |     
            |   Você perdeu {eBonus} almas!
                
                """) #Mensagem de evento de azar
            character.souls -= eBonus #Remove as almas ganhas ao personagem
            return character.souls
        
        else:
            print(f"""

            x EVENTO DE SORTE x (RANK F)
            |
            |   Nada aconteceu!
                
                """) #Mensagem de evento de sorte
            character.souls += 0 #Adiciona as almas ganhas ao personagem
            return character.souls
        
    def eventStatus():

        statusList = ["ATAQUE", "DEFESA", "SORTE", "VIDA", "AZAR"] #Lista de status
        selectedStatus = random.choice(statusList) #Seleciona um status aleatorio


        character_luckyEffect = int(character.lucky * 15) / 100 #Efeito da sorte do personagem
        dice_roll = random.randint(1, 20) + character_luckyEffect #Rolar um dado de 20 lados

        if selectedStatus == "ATAQUE":

            if dice_roll >= 20: 
                eBonus = int(10 * (character.health / 100)) #Calculo de bonus
                print(f"""

                x EVENTO DE STATUS x
                |     
                |   O status {selectedStatus} aumentou em {eBonus}!
                    
                    """)
                character.attack += eBonus #Adiciona o bonus ao status
                return character.attack
            

            elif dice_roll >= 15 and dice_roll < 20: 
                eBonus = int(5 * (character.health / 100)) #Calculo de bonus
                print(f"""

                x EVENTO DE STATUS x
                |     
                |   O status {selectedStatus} aumentou em {eBonus}!
                    
                    """)
                character.attack += eBonus #Adiciona o bonus ao status
                return character.attack
            
            
            elif dice_roll < 15:

                eBonus = int(2.5 * (character.health / 100)) #Calculo de bonus
                print(f"""
                                                                                                            
                x EVENTO DE STATUS x
                |     
                |   O status {selectedStatus} aumentou em {eBonus}!
                    
                    """)
                character.attack += eBonus #Adiciona o bonus ao status
                return character.attack
            
        elif selectedStatus == "DEFESA":

            if dice_roll >= 20: 
                eBonus = int(10 * (character.health / 100)) #Calculo de bonus
                print(f"""

                x EVENTO DE STATUS x
                |     
                |   O status {selectedStatus} aumentou em {eBonus}!
                    
                    """)
                character.defense += eBonus #Adiciona o bonus ao status
                return character.defense
            

            elif dice_roll >= 15 and dice_roll < 20: 
                eBonus = int(5 * (character.health / 100)) #Calculo de bonus
                print(f"""

                x EVENTO DE STATUS x
                |     
                |   O status {selectedStatus} aumentou em {eBonus}!
                    
                    """)
                character.defense += eBonus #Adiciona o bonus ao status
                return character.defense
            
            
            elif dice_roll < 15:

                eBonus = int(2.5 * (character.health / 100)) #Calculo de bonus
                print(f"""
                                                                                                            
                x EVENTO DE STATUS x
                |     
                |   O status {selectedStatus} aumentou em {eBonus}!
                    
                    """)
                character.defense += eBonus #Adiciona o bonus ao status
                return character.defense

        elif selectedStatus == "SORTE":
            
            if dice_roll >= 20: 
                eBonus = int(10 * (character.health / 100)) #Calculo de bonus
                print(f"""

                x EVENTO DE STATUS x
                |     
                |   O status {selectedStatus} aumentou em {eBonus}!
                    
                    """)
                character.lucky += eBonus #Adiciona o bonus ao status
                return character.lucky
            

            elif dice_roll >= 15 and dice_roll < 20: 
                eBonus = int(5 * (character.health / 100)) #Calculo de bonus
                print(f"""

                x EVENTO DE STATUS x
                |     
                |   O status {selectedStatus} aumentou em {eBonus}!
                    
                    """)
                character.lucky += eBonus #Adiciona o bonus ao status
                return character.lucky
            
            
            elif dice_roll < 15:

                eBonus = int(2.5 * (character.health / 100)) #Calculo de bonus
                print(f"""
                                                                                                            
                x EVENTO DE STATUS x
                |     
                |   O status {selectedStatus} aumentou em {eBonus}!
                    
                    """)
                character.lucky += eBonus #Adiciona o bonus ao status
                return character.lucky

        elif selectedStatus == "VIDA":

            if dice_roll >= 20: 
                eBonus = int(10 * (character.health / 100)) #Calculo de bonus
                print(f"""

                x EVENTO DE STATUS x
                |     
                |   O status {selectedStatus} aumentou em {eBonus}!
                    
                    """)
                character.health += eBonus #Adiciona o bonus ao status
                return character.health
            

            elif dice_roll >= 15 and dice_roll < 20: 
                eBonus = int(5 * (character.health / 100)) #Calculo de bonus
                print(f"""

                x EVENTO DE STATUS x
                |     
                |   O status {selectedStatus} aumentou em {eBonus}!
                    
                    """)
                character.health += eBonus #Adiciona o bonus ao status
                return character.health
            
            
            elif dice_roll < 15:

                eBonus = int(2.5 * (character.health / 100)) #Calculo de bonus
                print(f"""
                                                                                                            
                x EVENTO DE STATUS x
                |     
                |   O status {selectedStatus} aumentou em {eBonus}!
                    
                    """)
                character.health += eBonus #Adiciona o bonus ao status
                return character.health
            
        else:
            print(f"""

            x EVENTO DE SORTE x
            |
            |   Nada aconteceu!
                
                """) #Mensagem de evento de sorte
            character.souls += 0 #Adiciona as almas ganhas ao personagem
            return character.souls
        
    def eventMonster():

        with open("eventMessages.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        eventWin = random.choice(data["ganho"]) #Evento de ganho
        eventLose = random.choice(data["perda"]) #Evento de perda
        eventList = [eventWin, eventLose] #Lista de eventos
        selectedEvent = random.choice(eventList) # Seleciona um evento aleatorio

        statusList = ["VIDA", "ATAQUE", "DEFESA"] #Lista de status do monstro
        eStatus = random.choice(statusList) #Seleciona um status aleatorio do monstro para ser alterado
        eBonus = int(10 * (monster.health / 100)) #Calculo de bonus

        final_event = selectedEvent.format(eBonus=eBonus, eStatus=eStatus) #Formata a string com o status do monstro


        if selectedEvent == eventWin:

            if eStatus == "VIDA":
                monster.health += eBonus
                print(f"""

                x EVENTO DE MONSTRO x
                |
                |    {final_event}

                    """)
                return monster.health
                
            elif eStatus == "ATAQUE":
                monster.attack += eBonus
                print(f"""

                x EVENTO DE MONSTRO x
                |
                |    {final_event}

                    """)
                return monster.attack
            
            elif eStatus == "DEFESA":
                monster.defense += eBonus
                print(f"""

                x EVENTO DE MONSTRO x
                |
                |    {final_event}

                    """)
                return monster.defense


        elif selectedEvent == eventLose:

            if eStatus == "VIDA":
                monster.health -= eBonus
                print(f"""

                x EVENTO DE MONSTRO x
                |
                |    {final_event}

                    """)
                return monster.health
                
            elif eStatus == "ATAQUE":
                monster.attack -= eBonus
                print(f"""

                x EVENTO DE MONSTRO x
                |
                |    {final_event}

                    """)
                return monster.attack
            
            elif eStatus == "DEFESA":
                monster.defense -= eBonus
                print(f"""

                x EVENTO DE MONSTRO x
                |
                |    {final_event}

                    """)
                return monster.defense
                    
    events = [eventSouls, eventStatus, eventMonster] #Lista de eventos
    selectedEvent = random.choice(events) #Seleciona um evento aleatorio
    selectedEvent() #Executa o evento selecionado