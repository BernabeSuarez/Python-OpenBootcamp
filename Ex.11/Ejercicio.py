# En este ejercicio tendréis que crear una tabla llamada Alumnos
# que constará de tres columnas:
# la columna id de tipo entero, la columna nombre que será de tipo texto y
# la columna apellido que también será de tipo texto.

# Una vez creada la tabla, tenéis que insertarle datos,
# como mínimo tenéis que insertar 8 alumnos a la tabla.

# Por último, tienes que realizar una búsqueda de un alumno por nombre
# y mostrar los datos por consola.

import sqlite3
import random

def main():

    nombre = input ('Nombre del alumno: ') 
    apellido = input ('Apellido del almno: ')
    identifier = random.randrange(10)

    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()
    query = "INSERT INTO alumnos(id,nombre,apellido) VALUES(?, ?, ?)"
    rows = cursor.execute(query, (identifier, nombre, apellido))

    conn.commit()

   

    print(show)

    cursor.close()
    conn.close()





if __name__ == "__main__":
    main()