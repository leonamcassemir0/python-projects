def cars(fabricante, modelo, **caracteristicas):
    car = {}
    car['Fabricante'] = fabricante
    car['modelo'] = modelo
    for key, value in caracteristicas.items():
        car[key] = value
    return car


print(cars('Volkswagen', 'Gol', gasolina='economico', motor='1.0', geracao='g4'))
