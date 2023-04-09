def sumar_valores(*args):
    resultado = 0
    #Iteramos cada elemento
    for valor in args:
        # resultado = resultado + valor

        resultado += valor
    return resultado



#Llamada a la funcion
print(sumar_valores(3, 5, 9))