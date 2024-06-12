import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

# Criando um dado de seis lados
seis_lados = Die()

# Lançando o dado de seis lados dez vezes
print("Lançando um dado de seis lados dez vezes:")
for _ in range(10):
    print(seis_lados.roll_die())

# Criando um dado de dez lados
dez_lados = Die(sides=10)

# Lançando o dado de dez lados dez vezes
print("\nLançando um dado de dez lados dez vezes:")
for _ in range(10):
    print(dez_lados.roll_die())

# Criando um dado de vinte lados
vinte_lados = Die(sides=20)

# Lançando o dado de vinte lados dez vezes
print("\nLançando um dado de vinte lados dez vezes:")
for _ in range(10):
    print(vinte_lados.roll_die())
