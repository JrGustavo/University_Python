archivo = open('prueba.txt', 'r', encoding='utf8')
#print(archivo.read())

#Leer algunos caracteres
#print(archivo.read(5))
#print(archivo.read(3))

#Leer lineas completas
##print(archivo.readline())
#p#rint(archivo.readline())

#Iterar el archivo
# for linea in archivo:
# print(linea

# Leer lineas
#print(archivo.readline()[2])

#Abrimos un nuevo archivo
# a - anexar información
archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo.close()
#print('Se ha terminado el proceso de leer y copiar')