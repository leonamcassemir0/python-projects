message = ''
pizza = []
active = False

while active == False:
    ingrediente = input("Digite o ingrediente da pizza: ")
    pizza.append(ingrediente)
    print("Adicionamos " + ingrediente + " a sua pizza!")
    print("Essa é sua pizza até agora: ", pizza)
    message = input("continue ou quit? ")
    if message == "quit":
        active = True
    else:
        active = False

print(pizza)
