from NumerosIdenticosException import NumerosIdenticosException

resultado = None
try:

    a = int(input('Primer nùmero:  '))
    b = input('Segundo nùmero:  ')
    if a == b:
        raise NumerosIdenticosException('números identicos')
    resultado = a/b
except ZeroDivisionError as e:
    print(f'  ZeroDivisionError - Ocurrio un error: {e} , {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {e}, {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {e}, {type(e)}')
else:
    print('No se arrojo ninguna excepcion')
finally:
    print('Ejecucion del bloque finally')

print(f'Resultado: {resultado}')
print('Continuamos...')

