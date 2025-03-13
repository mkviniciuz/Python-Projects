import monstersCreation
import random
from monstersCreation import character
import time


killcount = 0
floor_level = 1
good_events = {

                #Almas encontradas
                "1": "Você encontrou um baú de tesouro! Você ganhou 50 almas!",
                "2": "Você encontrou um baú de tesouro! Você ganhou 100 almas!",
                "3": "Você encontrou um baú de tesouro! Você ganhou 150 almas!",
                "4": "Você encontrou um baú de tesouro! Você ganhou 200 almas!",
                "5": "Você encontrou um baú de tesouro! Você ganhou 250 almas!",
                "6": "Você encontrou um baú de tesouro! Você ganhou 300 almas!",
                "7": "Você encontrou um baú de tesouro! Você ganhou 350 almas!",
                "8": "Você encontrou um baú de tesouro! Você ganhou 400 almas!",
                "9": "Você encontrou um baú de tesouro! Você ganhou 450 almas!",
                "10": "Você encontrou um baú de tesouro! Você ganhou 500 almas!"

                #Alterações de status
                "11": "Os deuses estão ao seu favor! Você ganhou +10 de ataque!",
                "12": "Os deuses estão ao seu favor! Você ganhou +10 de defesa!",
                "13": "Os deuses estão ao seu favor! Você ganhou +10 de vida!",
                "14": "Os deuses estão ao seu favor! Você ganhou +10 de velocidade!",
                "15": "Os deuses estão ao seu favor! Você ganhou +20 de ataque!",
                "16": "Os deuses estão ao seu favor! Você ganhou +20 de defesa!",
                "17": "Os deuses estão ao seu favor! Você ganhou +20 de vida!",
                "18": "Os deuses estão ao seu favor! Você ganhou +20 de velocidade!",
                "19": "Os deuses estão ao seu favor! Você ganhou +30 de ataque!",
                "20": "Os deuses estão ao seu favor! Você ganhou +30 de defesa!",

                #Debuff em monstros
                "21": "Você encontrou um pergaminho de maldição! O monstro perdeu 10 de ataque!",
                "22": "Você encontrou um pergaminho de maldição! O monstro perdeu 10 de defesa!",
                "23": "Você encontrou um pergaminho de maldição! O monstro perdeu 10 de vida!",
                "24": "Você encontrou um pergaminho de maldição! O monstro perdeu 10 de velocidade!",
                "25": "Você encontrou um pergaminho de maldição! O monstro perdeu 20 de ataque!",
                "26": "Você encontrou um pergaminho de maldição! O monstro perdeu 20 de defesa!",
                "27": "Você encontrou um pergaminho de maldição! O monstro perdeu 20 de vida!",
                "28": "Você encontrou um pergaminho de maldição! O monstro perdeu 20 de velocidade!",
                "29": "Você encontrou um pergaminho de maldição! O monstro perdeu 30 de ataque!",
                "30": "Você encontrou um pergaminho de maldição! O monstro perdeu 30 de defesa!"
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