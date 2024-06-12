from modulo_restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurante_name, cuisine_name, served, *flavors):
        super().__init__(restaurante_name, cuisine_name, served)
        self.flavors = flavors

    def sabores(self):
        print(list(self.flavors))


my_Order = IceCreamStand('asder', 'werredf', 45, 'Caramelo', 'Doce de leite', 'Limao', 'Menta', 'Abacaxi')
my_Order.describe_restaurant()
my_Order.sabores()

"""
restaurante = Restaurant("ABC", "DEF", 30)
# restaurante.number_served = 30
restaurante.describe_restaurant()
restaurante.open_restaurant()
restaurante.set_number_served(21)
restaurante.describe_restaurant()
restaurante.imcrement(10)
restaurante.describe_restaurant()


restaurante = Restaurant("sdfvgbh", "sedfgh")
restaurante.describe_restaurant()
restaurante.open_restaurant()

restaurante = Restaurant("zxcvb", "qwery")
restaurante.describe_restaurant()
restaurante.open_restaurant()
"""
