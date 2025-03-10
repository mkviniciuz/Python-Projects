import monstersCreation
import random
from monstersCreation import character


#Criação de monstros aleatorios
def monstersCreationFunction():
    monsters = []
    for i in range(9):

        health=random.randint(100,105) #Vida do monstro
        attack=random.randint(10,15) #Ataque do monstro
        defense=random.randint(0,1) #Defesa do monstro
        souls=random.randint(10, 20) #Almas que o monstro dropa
        speed=random.randint(1,2) #Velocidade do monstro

        monster = monstersCreation.monsterTypeA(health, attack, defense, speed, souls)
        monsters.append(monster)

    return monsters

monsters = monstersCreationFunction()


def main():
    playing = True
    while playing:
        try:
            print(f"""
                x------------------| STATUS |-------------------x
                |     Vida                             Almas    |
                |   |{"█" * int(character.health / 12)}| {character.health}/200   |     {character.souls}      |
                |                                               |
                |     Ataque            Level          Defesa   |
                |     {character.attack}                {character.level}              {character.defense}       |
                x-----------------------------------------------x

                1 - Atacar      2 - Fugir      3 - Ver status
                                4 - Sair 
                """)
                
            of = int(input("Escolha uma opção: "))

        except ValueError:
            print("Você morreu!")
            playing = False
            break
main()