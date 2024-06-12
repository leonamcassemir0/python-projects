import string

values = {'var': 'foo'}

t = string.Template("""
Variable: $var
Escape: $$
Variable in text: ${var}iable
""")
print('TEMPLATE', t.substitute(values))


"""
A interpolação em Python é uma técnica poderosa que permite criar strings dinâmicas, substituindo partes específicas por valores ou expressões.
"""
s = """
Variable: %(var)s
Escape: %%
Variable in text: %(var)siable
"""
print("INTERPOLATION", s % values)


"""
The format() method formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets:{}
"""
h = """
Variable: {var}
Escape: {{}}
Variable in text: {var}iable
""" 
print("FORMAT:", h.format(**values))