lugares = []
active = False

while active != True:
    place = input("Digite o lugar das ferias dos sonhos: ")
    lugares.append(place)
    message = input("continua ou para? ")
    if message == 'continua':
        active = False 
    elif message == 'para':
        active = True
    else:
        continue

    print(lugares)
