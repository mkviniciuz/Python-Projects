import random
import json
import os

def cardShopping(character):

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
            select = data["ATAQUE"]
            select_choose = random.choice(select)
            disposs_cards.append(select_choose[0])
            pointsRequimerent.append(select_choose[1])

        elif item == cards[1]:
            select = data["DEFESA"]
            select_choose = random.choice(select)
            disposs_cards.append(select_choose[0])
            pointsRequimerent.append(select_choose[1])

        elif item == cards[2]:
            select = data["VIDA"]
            select_choose = random.choice(select)
            disposs_cards.append(select_choose[0])
            pointsRequimerent.append(select_choose[1])

        elif item == cards[3]:
            select = data["SORTE"]
            select_choose = random.choice(select)
            disposs_cards.append(select_choose[0])
            pointsRequimerent.append(select_choose[1])

    deck.append(disposs_cards)
    deck.append(pointsRequimerent)

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
    [1]~ {deck[0][0]} -> {deck[1][0]} Pontos  
    [2]~ {deck[0][1]} -> {deck[1][1]} Pontos  
    [3]~ {deck[0][2]} -> {deck[1][2]} Pontos

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

                # Após a compra d
                for check in character.deck:
                    if check == "Pacto Neorato":
                        character.towerEffects["pactoNeorato"] = True
                        character.roundEffects["pactoNeorato"] = True
                    elif check == "Ultimo Suspiro":
                        character.towerEffects["ultimoSuspiro"] = True
                        character.roundEffects["ultimoSuspiro"] = True
                    elif check == "Trato Sanguinario":
                        character.towerEffects["tratoSanguinario"] = True
                        character.roundEffects["tratoSanguinario"] = True
                    elif check == "Sentença Final":
                        character.towerEffects["sentencaFinal"] = True
                        character.roundEffects["sentencaFinal"] = True
                        
                os.system('cls')
                break
        except ValueError:
            print("Algo deu errado!")

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
