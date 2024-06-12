try:
    with open('cap10\prideandprejudice.txt') as f_obj:
        content = f_obj.read()
except FileNotFoundError:
    print("I´m not founding the file, sorry!")
else:
    words = content.split()
    print(len(words))
