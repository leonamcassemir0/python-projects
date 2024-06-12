class Employee:
    def __init__(self, first_name, last_name, bill):
        self.first_name = first_name
        self.last_name = last_name
        self.bill = bill

    def give_raise(self, aumento=5000):
        self.bill += aumento


"""
empregado = Employee("Leonam", "Cassemiro", 1730)
print(f"{empregado.first_name} {empregado.last_name} recebe {empregado.bill}")
empregado.give_raise()
print(f"{empregado.first_name} {empregado.last_name} recebe {empregado.bill}")
"""