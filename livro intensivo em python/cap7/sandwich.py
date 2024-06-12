sandwich_orders = ['pastrami', 'presunto', 'queijo', 'pastrami', 'frango', 'pastrami']

print("Estamos sem sanduiche de pastrami :(")
finished_sandwich = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for x in range(len(sandwich_orders)):
    print("Ja preparei seu sanduiche de " + sandwich_orders[x])
    finished_sandwich.append(sandwich_orders[x])

print(finished_sandwich)
