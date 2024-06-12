guest = 'convidado.txt'

with open(f'cap10/{guest}', 'w') as file_object:
    quest = input("Digite seu nome: ")
    file_object.write(quest)
