import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)


"""
dados = Die()
print("Dado com seis lados:")
for x in range(10):
    print(dados.roll_die())

print("Dado com 10 lados:")
for x in range(10):
    dez_lados = Die(sides=10)
    print(dez_lados.roll_die())
"""

vinte_lados = Die(sides=20)
for x in range(10):
    print(vinte_lados.roll_die())

