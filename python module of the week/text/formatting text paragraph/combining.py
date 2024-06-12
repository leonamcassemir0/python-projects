import textwrap
from textwrap_example import texto

dedent_text = textwrap.dedent(texto)
for width in [45, 60]:
    print('{} Columns: \n'.format(width))
    print(textwrap.fill(dedent_text, width=width))
    print()
