nombres = ['Juan', 'Karla', 'Ricardo', 'Mario']

print(nombres)
#Acceder a los elementos de forma individual

print(nombres[0])
print(nombres[-1])
#Imprimir un rango
print(nombres[0:2])

nombres[3] = 'Ivone'
print(nombres)

for nombre in nombres:
    print(nombres)
else:
    print('No existen mas nombres en la lista')
nombres.pop()
print(nombres)

del nombres [0]
