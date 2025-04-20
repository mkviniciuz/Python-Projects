import random
import json
import os
# def mostrar_cores_ansi():
#     print("Cores normais:")
#     for i in range(30, 38):
#         print(f"\033[{i}m Código {i} \033[0m", end="  ")
#     print("\n")

#     print("Cores claras (brilhantes):")
#     for i in range(90, 98):
#         print(f"\033[{i}m Código {i} \033[0m", end="  ")
#     print("\n")
 
#     print("Fundos coloridos:")
#     for i in range(40, 48):
#         print(f"\033[{i}m Fundo {i} \033[0m", end="  ")
#     print("\n")

#     print("Fundos claros:")
#     for i in range(100, 108):
#         print(f"\033[{i}m Fundo {i} \033[0m", end="  ")
#     print("\n")

# mostrar_cores_ansi()

# X--------------X
# |              |
# |     ZZZZ     |
# |      TT      |
# |      ||      |
# |      ||      |
# |   ========   |
# |     |  |     |
# X--------------X
#  \____________/

# FUNÇÕES

def cardShopping(character, target, round, characterdeck, distribuitionPoints):

    character
    target

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
    | Troque seus pontos por cartas, [{distribuitionPoints}] Pontos atual! |
    +{'='*51}+
    \_________________________________________________/
            """)

            for linhas in zip(*random_cards):
                print("   ".join(linhas))
            choose = int(input(f"""
    [1]~{deck[0][0]} -> {deck[1][0]} Pontos  
    [2]~{deck[0][1]} -> {deck[1][1]} Pontos  
    [3]~{deck[0][2]} -> {deck[1][2]} Pontos
                            
                                            

        ESCOLHA: """))
            if choose == 1:
                if distribuitionPoints < deck[1][0]:
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
                        characterdeck.append(deck[0][0])
                        distribuitionPoints -= deck[1][0]
                        sleeper = input("")
                        os.system('cls')

            elif choose == 2:
                if distribuitionPoints < deck[1][1]:
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
                        characterdeck.append(deck[0][1])
                        distribuitionPoints -= deck[1][1]
                        sleeper = input("")
                        os.system('cls')

            elif choose == 3:
                if distribuitionPoints < deck[1][2]:
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
                        characterdeck.append(deck[0][2])
                        distribuitionPoints -= deck[1][2]
                        sleeper = input("")
                        os.system('cls')
            
            else:
                print("""
                [ERROR]
                Parece que algo deu errado! tente novamente.
            """)
                sleeper = input("")
                os.system('cls')
                continue
        except ValueError:
            print("Algo deu errado!")





