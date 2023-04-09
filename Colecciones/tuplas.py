frutas = ('Naranja', 'Platano', 'Guayaba')
print(frutas)

print(len(frutas))

print(frutas[0])

for fruta in frutas:
    print(fruta, end=' ')

frutas[0] = 'Pera'
print(frutas, end= ''  )


frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)

print('\n',frutas)