def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE='Integreated Development Enviroment', PK='Primary Key')
listarTerminos(DBMS = 'Database Management System ')

