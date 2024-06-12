guests = ["Einstein", "Tesla", "Turin"]

print("Ola! Estou te convidando para meu jantar", guests[0], "! Abracos")
print("Ola! Estou te convidando para meu jantar", guests[1], "! Abracos")
print("Ola! Estou te convidando para meu jantar", guests[2], "! Abracos")
print()
print("Ah que pena", guests[0] + ", sua presença sera sentida.")

guests[0] = "Carlo Rovelli"
print()
print("Ola! Estou te convidando para meu jantar", guests[0], "! Abracos")
print("Ola! Estou te convidando para meu jantar", guests[1], "! Abracos")
print("Ola! Estou te convidando para meu jantar", guests[2], "! Abracos")
print()
print("Noticia boa! Conseguimos uma mesa maior de jantar!")
print()
guests.insert(0, "Carla Madeira")
guests.insert(2, "Machado de Assis")
guests.append("Stephen Hawking")

print()
print("Ola! Estou te convidando para meu jantar", guests[0], "! Abracos")
print("Ola! Estou te convidando para meu jantar", guests[1], "! Abracos")
print("Ola! Estou te convidando para meu jantar", guests[2], "! Abracos")
print("Ola! Estou te convidando para meu jantar", guests[3], "! Abracos")
print("Ola! Estou te convidando para meu jantar", guests[4], "! Abracos")
print("Ola! Estou te convidando para meu jantar", guests[5], "! Abracos")

print()
print("Pessoal infelizmente só posso convidar duas pessoas")

print()
print("Infelizmente não posso te chamar,", guests.pop(0))
print("Infelizmente não posso te chamar,", guests.pop(4))
print("Infelizmente não posso te chamar,", guests.pop(2))
print("Infelizmente não posso te chamar,", guests.pop(1))

print()
print("Ola! Estou te convidando para meu jantar", guests[0], "! Abracos")
print("Ola! Estou te convidando para meu jantar", guests[1], "! Abracos")

del guests[0]
del guests[0]
print()
print(guests)
