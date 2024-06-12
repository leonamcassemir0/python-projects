# turtle permite criar imagens usando [turtle graphics].

import turtle

bob = turtle.Turtle()

"""
bob.pu()
bob.pd()
"""
# pu = caneta para cima
# pd = caneta para baixo

"""
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.bk(200)
"""
# fd = segue reto
# bk = move para trás
# lt = vira à esquerda
# rt = vira à direita
# lt e rt são ângulos

"""
for i in range(4):
    bob.fd(100)
    bob.lt(90)
"""

turtle.mainloop()
# mainloop diz que a janela deve esperar que o usuário faça algo
