car = ['subaru', 'audi', 'alfa romeo', 'fiat', 'jaguar',
       'ferrari', 'bugatti', 'chevrolet', 'volkswagen', ]

"""
print("Is car == 'subaru'? I predict True") 
print("\nIs car == 'audi'? I predict False")
"""

# Casos True
print(car[0].title() == 'Subaru')
print(car[1] == 'audi')
print(car[2] == 'alfa romeo')
print(car[3] == 'fiat')
print(car[4] == 'jaguar')

# Casos False
print(car[0] == 'subar')
print(car[1] == 'aud')
print(car[2] == 'alf romeo')
print(car[3] == 'fat')
print(car[4] == 'jguar')
