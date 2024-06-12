while True:
    filename = input('Digite o diretório do arquivo: ')

    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(content)
