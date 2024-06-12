import textwrap
from textwrap_example import texto

dedent_text = textwrap.dedent(texto)
hanging = textwrap.fill(dedent_text, initial_indent='',
                        subsequent_indent=' '*4,
                        width=50)
print(hanging)
'''
Conseguimos estilizar as identações das linhas iniciais e subsequentes. Com initial_indent e subsequent_indent dentro da função fill.
'''