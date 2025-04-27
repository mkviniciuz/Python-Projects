from modules.monstersCreation import *
from modules.gameMechanics import *
from modules import characterObject
import time
import os


os.system('cls')

def game():

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
            cardShopping(character)

game()

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