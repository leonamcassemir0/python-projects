def celsius():
    temperatura = int(input("Digite a temperatura (celsius): "))
    fahrenheit = 9/5*temperatura + 32
    print("A temperatura em fahrenheit é", fahrenheit)


celsius()


def fahrenheit():
    temperatura = int(input("Digite a temperatura (celsius): "))
    celsius = 5*(temperatura - 32) / 9
    print("A temperatura em celsius é", celsius)


fahrenheit()
