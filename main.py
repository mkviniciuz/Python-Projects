import characterObject
import monstersCreation
import random

def characterCreation():

    print("""
    x---------------------------------------------x     
    |                                             |
    |      Defina um nome para seu personagem!    |
    |                                             |
    x---------------------------------------------x
        """)

    name = input("""   --> Nome: """)
    health = 100
    attack = 10
    defense = 10
    speed = 10
    level = 1
    souls = 210
    gold = 0
    nSouls = 210
    distribuitonPoints = 0

    character = characterObject.characterObject(name, health, attack, defense, speed, level, souls, gold, nSouls, distribuitonPoints)
    return character

#Criação de monstros aleatorios


def monstersCreationFunction():
    monsters = []
    for i in range(9):

        health=random.randint(100,105) #Vida do monstro
        attack=random.randint(1,2) #Ataque do monstro
        defense=random.randint(0,1) #Defesa do monstro
        souls=random.randint(10, 20) #Almas que o monstro dropa
        speed=random.randint(1,2) #Velocidade do monstro

        monster = monstersCreation.monsterTypeA(health, attack, defense, speed, souls)
        monsters.append(monster)

    return monsters
    
monsters = monstersCreationFunction()
for monster in monsters:
    monster.showMonsterStats()
print(monsters)