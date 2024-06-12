message = 'programming.txt'

with open(message, 'w') as file_object:
    file_object.write('I love programming')

with open(f'cap10/{message}', 'a') as file_object:
    file_object.write('I love python')
