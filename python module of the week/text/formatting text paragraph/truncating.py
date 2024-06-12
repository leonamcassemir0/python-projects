import textwrap
from textwrap_example import texto

dedent_text = textwrap.dedent(texto)
original = textwrap.fill(dedent_text, width=50)
print('original: \n')
print(original)

shortened = textwrap.shorten(original, 250)
shortened_wrapped = textwrap.fill(shortened, width=50)
print('\n shortened: \n')
print(shortened_wrapped)
'''
A função shorten adiciona um sumário ao texto.
'''
