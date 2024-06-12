import textwrap
from textwrap_example import texto

dedent_text = textwrap.dedent(texto)
wrapped = textwrap.fill(dedent_text, width=50)
final = textwrap.indent(wrapped, '- ')
print(final)
'''
A função indent coloca identação em seus textos.
'''


def should_indent(line):
    print('Indent {}'. format(line))
    return len(line.strip()) % 2 == 0


dedented_text = textwrap.dedent(texto)
wrapped = textwrap.fill(dedented_text, width=50)
final = textwrap.indent(wrapped, 'EVEN', predicate=should_indent)

print('\nQuoted block:\n')
print(final)
