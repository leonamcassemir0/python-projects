pizza = ["calabresa", "portuguesa", "caipira"]

friend_pizza = pizza[:]
print(friend_pizza)
pizza.append("cannoli")
friend_pizza.append("ice cream")

print("Minhas pizzas favoritas sao:")
for x in pizza:
    print(x, end=", ")

print()
print("As pizzas preferidas do meu amigo sao:")
for t in friend_pizza:
    print(t, end=" ")

"""
for x in pizza:
    print("Eu amo pizza de", x)

print("Esses sao meus sabores preferidos!")
"""

"""
print(pizza[:3])
print(pizza[3:6])
print(pizza[-3:])
"""
