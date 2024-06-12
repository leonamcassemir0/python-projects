class Restaurant:
    def __init__(self, restaurante_name, cuisine_name, served):
        self.name = restaurante_name
        self.cuisine = cuisine_name
        self.number_served = served

    def describe_restaurant(self):
        print(self.name)
        print(self.cuisine)
        print(str(self.number_served))

    def open_restaurant(self):
        print("O restaurante esta aberto!")

    def set_number_served(self, update):
        self.number_served = update

    def increment(self, sum):
        self.number_served += sum
