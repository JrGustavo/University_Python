#Diccionarios (Key, value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

print(diccionario)

#LArgo
print(len(diccionario))
#Acceder a un elemento (key)
print(diccionario['IDE'])

#Otra forma de recuperar un elemento
print(diccionario.get('OOP'))

#Modificando elementos en un diccionario
diccionario['IDE'] = 'integrated development environment'

#Recorrer los elementos

for termino, valor in diccionario.items():
    print(termino, valor)

for valor in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

