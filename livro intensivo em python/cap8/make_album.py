def make_album(artist, title, number=20):
    album = {'artista': artist,
             'titulo': title,
             'numero': number}
    print(album)


x = 0
while x <= 5:
    artista = input('Digite o nome do artista: ')
    titulo = input('Digite o nome do album: ')
    question = input('Deseja adicionar o numero de faixas? (S/N)')
    if question == 'S':
        numero = input('Quantas faixas tem? ')
        make_album(artista, titulo, number=int(numero))
    elif question == 'N':
        make_album(artista, titulo)
    else:
        print('Valor inválido!')
        continue


"""
make_album('Froid', 'O pior disco do ano')
make_album('Djonga', 'Heresia', 10)
make_album('Racionais', 'Sobrevivendo no inferno')
"""
