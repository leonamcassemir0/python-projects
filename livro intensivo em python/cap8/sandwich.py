def order(*choices):
    pedido = []
    for m in choices:
        pedido.append(m)
    print(pedido)


order('pao', 'bife', 'presunto', 'mussarela')
order('pao', 'bife', 'presunto', 'mussarela', 'queijo', 'oregano')
order('pao', 'bife', 'presunto', 'mussarela', 'queijo', 'oregano', 'ovo',
      'maionese', 'ketchup')
