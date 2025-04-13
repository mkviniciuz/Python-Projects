
# Teste de Logica Progressão na torre

""" import time


tower_level = 1

playing = True

boss_level = 10
semigod_level = 3



while playing:

    while tower_level != semigod_level and tower_level != boss_level:
        print("Batalha comum acontencendo!...")
        time.sleep(2)
        print("Batalha comum acontencendo!...")
        time.sleep(1)
        print("Jogador venceu!")
        print("")
        tower_level += 1


    if tower_level == semigod_level:
        print("Batalha Semideus acontencendo!...")
        time.sleep(2)
        print("Batalha Semideus acontencendo!...")
        time.sleep(1)
        print("Jogador venceu!")
        print("")
        tower_level += 1
        semigod_level += 3

    if tower_level == boss_level:
        print("Batalha Deus acontencendo!...")
        time.sleep(2)
        print("Batalha Deus acontencendo!...")
        time.sleep(1)
        print("Jogador venceu!")
        print("")
        boss_level += 10

"""""

def mostrar_cores_ansi():
    print("Cores normais:")
    for i in range(30, 38):
        print(f"\033[{i}m Código {i} \033[0m", end="  ")
    print("\n")

    print("Cores claras (brilhantes):")
    for i in range(90, 98):
        print(f"\033[{i}m Código {i} \033[0m", end="  ")
    print("\n")

    print("Fundos coloridos:")
    for i in range(40, 48):
        print(f"\033[{i}m Fundo {i} \033[0m", end="  ")
    print("\n")

    print("Fundos claros:")
    for i in range(100, 108):
        print(f"\033[{i}m Fundo {i} \033[0m", end="  ")
    print("\n")

mostrar_cores_ansi()
