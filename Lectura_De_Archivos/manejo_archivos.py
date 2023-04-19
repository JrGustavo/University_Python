
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos informacion al archivo ')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()

