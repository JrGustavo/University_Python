print('Proporcione los siguientes datos del libro')
nombre = input('Proporcione el nombre del libro: ')
id = int(input('Proporciona el ID del libro: '))
precio = float(input('Proporciona el valor del libro:  '))
envioGratuito =  input('Indica si es envio gratuito (True/False):  ')

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'Valor incorrecto, debe escribir True/False'

    print(f'''
    
    Nombre: {nombre}, 
    Id: {id}
    Precio: {precio}
    Envio gratuito?: {envioGratuito}
    
    ''')