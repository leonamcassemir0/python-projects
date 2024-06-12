print("Digite sua idade e veja quanto pagara pelo ingresso.")
print()

for x in range(10):
    age = input("Digite a idade: ")
    idade = int(age)

    if idade > 0:
        if idade < 3:
            print("Gratis!")
        elif idade >= 3 and idade < 12:
            print("10 dolares!")
        elif idade >= 12:
            print("15 dolares")
    else:
        print("Não existe idade negativa!")
