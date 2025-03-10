import characterObject
import monstersCreation
import random

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
for monster in monsters:
    monster.monsterAttack()