magicos = ['Houdini', 'Leonam', 'Bruxo']


def make_great(grande):
    m = []
    for d in range(len(grande)):
        k = grande.pop()
        m.append('O grande ' + k)
    print(m)


def show_magicians(magic):
    make_great(magic)


show_magicians(magicos)
