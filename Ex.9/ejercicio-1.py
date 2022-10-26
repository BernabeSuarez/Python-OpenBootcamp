
items = input('Ingresa paises separados por coma: \n')

paises = [pais for pais in items.split(',')]


print(','.join(sorted(list(set(paises)))))

"""
    .join() agrega la separacion con coma
    sorted() ordena alfabeticamente
    list() retorna una lista
    set() quita los paises repetidos

"""