import random

prefix = random.choice(["[Deus do Destino]", "[Deus do Caos]", "[Deus da Ruina]"])

start = random.choice(["Syl","Zor","Ter","Ari","Zar","Gor","Kra"])
middle = random.choice(["go","thar","thul","lot","kam","mi","dra"])
end = random.choice(["ylg","let", "phyr", "jar", "gsar", "iuyl", "jonl"])


boss_name = f"{start}{middle}{end} {prefix}"
print(boss_name)