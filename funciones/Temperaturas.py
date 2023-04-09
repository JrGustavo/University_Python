"""
Ejercicio: Convertidor de Temperatura
REalizar dos funciones para convertir de grados celsius a fharenheit y viceversa.
"""

#Funciones que convierte de celsius a fharenheit
def celsius_fharenheit(celsius):
    return celsius * 9 / 5 + 32


#Funcion que convierte de fharenheit a celsius

def fharenheit_celsius(fharenheit):
    return (fharenheit - 32) * 5 / 9

# Realizamos algunas priebas de conversion
celsius = float(input('Proporcione su valor en celsius:  '))
resultado = celsius_fharenheit(celsius)

#Imprimimos el resultado
print(f'{celsius} C a F: {resultado:.2f}')

#REalizamos la prueba de grados fharenheit a celsius
fharenheit = float(input('Proporcione su valor en fharenheit:   '))
resultado = fharenheit_celsius(fharenheit)

#Imprimimos el resultado
print(f'{fharenheit} F a C: {resultado: 0.2f}')