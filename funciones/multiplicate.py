

#Definicion de la funcion para multiplicar los valores

def multiplicar_valores(*numeros):
    resultado = 1
    for  numero in numeros:
        #resultado = resultado * numero
        resultado *= numero

    return resultado

# Llamada de la funcion
print(multiplicar_valores(3,5,6))

