q = input("Deseja adicionary nomes? (y/n)")

while q == 'y':
    with open('cap10/guest_book.txt', 'a') as file_object:
        name = input("Qual seu nome: ")
        file_object.write(f'{name} \n')
        print(f'Olá {name}, seja bem-vindo!')
    q = input("Deseja adicionar mais nomes? (y/n)")
