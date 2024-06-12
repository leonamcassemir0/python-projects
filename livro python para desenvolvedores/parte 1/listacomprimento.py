def flatten(it):

    # Se for uma lista
    if isinstance(it, list):
        ls = []
        # Para cada item da lista
        for item in it:
            # Evoca flatten() recursivamente
            ls = ls + flatten(item)
            return ls
    else:
        return [it]


# Teste
l = ["1, 2, 3, 4, 5, 6, 7"]
print(flatten(l))
# imprime: [1, 2, 3, 4, 5, 6, 7]
