a = open('first-file.txt', 'w')
a.write('Creacion del primer archivo \n')
a.close()

a = open('first-file.txt', 'r+')  #indicar que se va a leer el archivo
a.readline() 
a.write('Segunda vez que escribo en el archivo')
a.close()

