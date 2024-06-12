import random

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
count = 0

for i in range(12):
    count += 1
    x = random.randint(1, 6)
    if x == 1:
        n1 += 1
    elif x == 2:
        n2 += 1
    elif x == 3:
        n3 += 1
    elif x == 4:
        n4 += 1
    elif x == 5:
        n5 += 1
    elif x == 6:
        n6 += 1

print(f"Apos {count} rodadas de dados, obtivemos os seguintes resultados:")
print(f"Tivemos {str(n1)} numero 1")
print(f"Tivemos {str(n2)} numero 2")
print(f"Tivemos {str(n3)} numero 3")
print(f"Tivemos {str(n4)} numero 4")
print(f"Tivemos {str(n5)} numero 5")
print(f"Tivemos {str(n6)} numero 6")
