import json

numbers = [2, 5, 7, 9, 2, 3, 6, 13]
with open('cap10/numbers.json', 'w') as f_obj:
    json.dump(numbers, f_obj)
