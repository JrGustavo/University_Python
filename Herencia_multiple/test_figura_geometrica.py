from Clases.Rectangulo import Rectangulo
from Cuadrado import Cuadrado

print('Creacion objeto cuadrado'.center(50, '_'))
cuadrado1 = Cuadrado(lado=-5, color='rojo')
cuadrado1.alto = -10
print(f'Calculo area cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)


print('Creacion objeto cuadrado'.center(50, '_'))
rectangulo1 = Rectangulo(ancho=13, alto=8, color='verde')
rectangulo1.ancho = 15
print(f'Calculo area rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

