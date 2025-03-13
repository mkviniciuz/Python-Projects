import random
from monstersCreation import character

#Tabela de RANKS
# S - 100%
# A - 75%
# B - 50%
# C - 25%
# D - -15%
# E - -30%




def eventSouls():
    character_luckyEffect = int(character.lucky * 15) / 100 #Efeito da sorte do personagem

    dice_roll = random.randint(1, 20) + character_luckyEffect #Rolar um dado de 20 lados e adicionar o efeito da sorte do personagem
    print(f"Evento sorteado: {dice_roll}")

    #Evento rank S (100% a mais de almas necessarias)
    if dice_roll == 20:
        character.souls += int(character.nSouls + (character.nSouls * 1))
        print(f"Você possui {character.souls} almas!")


    #Evento rank A (75% a mais de almas necessarias)
    elif dice_roll >= 15:
        character.souls += int(character.nSouls + (character.nSouls * 0.75))
        print(f"Você possui {character.souls} almas!")

    #Evento rank B (50% a mais de almas necessarias)
    elif dice_roll >= 13:
        character.souls += int(character.nSouls + (character.nSouls * 0.50))
        print(f"Você possui {character.souls} almas!")

    #Evento rank C (25% a mais de almas necessarias)
    elif dice_roll >= 10:
        character.souls += int(character.nSouls + (character.nSouls * 0.25))
        print(f"Você possui {character.souls} almas!")

    #Evento rank D (-15% a mais de almas necessarias)
    elif dice_roll <= 5:
        character.souls -= int(character.nSouls - (character.nSouls * 0.15))
        print(f"Você possui {character.souls} almas!")

    #Evento rank D (-30% a mais de almas necessarias)
    elif dice_roll <= 0:
        character.souls -= int(character.nSouls - (character.nSouls * 0.30))
        print(f"Foi sorteado um evento de azar! Você possui {character.souls} almas!")

eventSouls()
