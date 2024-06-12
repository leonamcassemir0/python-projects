import string

"""
safe_substitute method is available in the string.Template class. 
It allows you to replace placeholders in a template string with values from a dictionary.


Use substitute quando você tem certeza de que todos os marcadores têm valores correspondentes. 

Use safe_substitute quando você quer manter os marcadores intactos caso algum valor esteja faltando.
"""


class MyTemplate(string.Template):
    delimiter = '@'
    idpattern = '[a-z]+_[a-z]+'


text = '''
Delimiter: @@
Replaced: @with_underscore
Ignored: @notunderscored
'''

d = {
    'with_underscore': 'replaced',
    'notunderscored': 'not replaced'
}

t = MyTemplate(text)
print('Modified ID pattern:')
print(t.safe_substitute(d))
