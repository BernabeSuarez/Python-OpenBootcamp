# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista
# pasada por parámetro con filter
# y realizará una suma de todos estos elementos obtenidos mediante reduce.
from functools import reduce


numeros = range(100)
lista = list(numeros)

def filtro(a):
    if a % 2 == 1:
     return a


lista_filtrada = filter(filtro, lista)

def suma(a,b):
    return a +b

resultado = reduce(suma, lista_filtrada)

print(resultado)

