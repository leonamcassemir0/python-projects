with open('cap10/learn_python.txt') as file_object:
    content = file_object.read()
    print(content)
    print(content)
    print(content)
    for line in file_object:
        print(line.rstrip())
    conteudo = file_object.readlines()
    print(conteudo)
