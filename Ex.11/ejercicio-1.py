import sqlite3
import getpass

def main():
    username = input('Nombre de usuario: ')
    password = getpass.getpass('Contraseña: ')

    if verificar(username, password):
        print('Login Correcto')
    else:
        print('Login Incorrecto')


def verificar(username, password):
    
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    rows = cursor.execute(f"SELECT id FROM usuarios WHERE username='{username}' AND password='{password}'")
    data = rows.fetchone()

    cursor.close()

    conn.close()

    if data == None:
        return False
    return True


if __name__ == '__main__':
    main()


#conn.commit() registra el comic para agregar o borrar datos de la base de datos