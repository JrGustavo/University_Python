valor = int(input('Escribe el valor: '))

valorMaximo = 5
valorMinimo = 0

dentroRango = (valor >= valorMinimo ) and (valor <= valorMaximo)

if dentroRango:
    print(f' El valor {valor} esta dentro de rango')
else:
    print(f'  El valor {valor} esta fuera de rango')







