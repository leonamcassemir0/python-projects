class User:
    def __init__(self, first_name, last_name, *caracteristicas):
        self.nome = first_name
        self.sobrenome = last_name
    attempts = 0

    def describe_user(self):
        print(self.nome)
        print(self.sobrenome)
        print(str(self.attempts))

    def increment_login_attempts(self):
        self.attempts += 1

    def reset_login_attempts(self):
        self.attempts = 0

    def greet_user(self):
        print("Seja bem-vindo!")
