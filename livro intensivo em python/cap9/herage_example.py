class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fill_gas = 58

    def fill_gas_tank(self):
        print("This car has " + str(self.fill_gas) + ' in the gas tank!')

    def get_descritive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can-t roll back an odometer!')

    def incremente_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class EletricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    """
    def battery_saver(self):
        print('This car has ' + str(self.battery_save) + '-kWt hour.')
    """

    def fill_gas_tank(self):
        print("This car doesn´t need a gas tank!")      


my_tesla = EletricCar('tesla', 'model s', 2016)
print(my_tesla.get_descritive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
