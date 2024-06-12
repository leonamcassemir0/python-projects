users = ["Leonam", "Yuri", "Eneia", "Manoel", "Admin"]

for x in range(len(users)):
    if users[x].lower() == "admin":
        print("Ola admin, gostaria de ver um relatorio de status?")
    else:
        print("Ola,", users[x] , "obrigado por fazer login novamente.")

users.clear()
if users == []:
    print("Precisamos encontrar alguns usuarios!")