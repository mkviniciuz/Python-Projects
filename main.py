import monstersCreation
import random
from monstersCreation import character
import time


killcount = 0
floor_level = 1
good_events = {

                #Almas encontradas
                "1": "Você encontrou um baú de tesouro! Você ganhou 50 almas!",

                #Alterações de status
                "11": "Os deuses estão ao seu favor! Você ganhou +10 de ataque!",

                #Debuff em monstros
                "21": "Você encontrou um pergaminho de maldição! O monstro perdeu 10 de ataque!", #Debuff rank C
                }


#Criação de monstros aleatorios
def monstersCreationFunction():
    for i in range(1):

        health=random.randint(character.health - int((character.health * 20) / 100), int((character.health * 75) / 100) + character.health) #Vida do monstro baseada na vida do personagem
        attack=random.randint(character.attack, int((character.attack * 50) / 100) + character.attack) #Ataque do monstro baseado no ataque do personagem
        defense=random.randint(character.defense, int((character.defense * 75) / 100) + character.defense) #Defesa do monstro baseada na defesa do personagem
        souls=random.randint(int(character.nSouls / 5), int(character.nSouls / 3)) #Almas que o monstro dropa baseado na quantidade de almas necessarias para upar
        speed=random.randint(1,2) #Velocidade do monstro

        monster = monstersCreation.monsterType(health, attack, defense, speed, souls)

    return monster

monster = monstersCreationFunction()


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
            
            time.sleep(2)

            print(f"""
            x Narrador x
            |
            | You are in the first floor of the Cursed Tower, {character.name}.
            """)

            time.sleep(2)

        except ValueError:
            print("Você morreu!")
            playing = False
            break
main()