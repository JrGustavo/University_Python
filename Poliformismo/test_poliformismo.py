from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalle(objeto):
    print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado('Juan', 5000)
imprimir_detalle(empleado)


Gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalle(Gerente)
