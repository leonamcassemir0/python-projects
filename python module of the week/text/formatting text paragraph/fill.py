import textwrap
from textwrap_example import texto

print(f'{texto} \n')
print('\n', textwrap.fill(texto, width=50))
'''
A função fill é usada para delimitar a largura de um texto. Ela identa o texto
e mantém fiel à largura determinada.
'''
