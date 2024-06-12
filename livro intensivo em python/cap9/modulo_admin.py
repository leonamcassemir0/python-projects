from modulo_user import User


class Privilege():
    def __init__(self, elogio=['can add post', 'can delete post', 'can ban user']):
        self.elogio = elogio

    def show_privilege(self):
        print(self.elogio)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privilege()
