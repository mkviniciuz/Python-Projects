import json
import random

# Carregar o JSON
with open("eventMessages.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Escolher um evento aleatório
evento = random.choice(data["eventos"])

# Definir um valor para eBonus
eBonus = random.randint(1, 10)

# Formatar a string com o valor de eBonus
evento_formatado = evento.format(eBonus=eBonus)

print(evento_formatado)