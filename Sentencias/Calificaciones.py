calificacion = int(input('Proporciona una calificacion entre 0 y 10:   '))
#Si esta entre 9 y 10, imprimir A

if 9 <= calificacion  <= 10:
#if calificacion >= 9 and calificacion <=  10:

    print('A')
elif 8 <= calificacion  < 9:
    print('B')
elif 7 <= calificacion  <= 8:
    print('C')
elif 6  <= calificacion  <= 7:
    print('D')
elif 0 <= calificacion  <= 6:
    print('F')
else:
    print('Valor incorrecto')
