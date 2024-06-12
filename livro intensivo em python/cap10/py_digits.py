with open('cap10/py.txt') as file_object:
    # contents = file_object.read()
    # print(contents)
    for line in file_object:
        print(line.rstrip())
