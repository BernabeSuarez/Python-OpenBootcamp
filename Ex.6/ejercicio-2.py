class Alumno:
 #inicializar los atributos
    def Init(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

# funcion para imprimir
    def imprimir(self):
        print('Nombre: ', self.nombre)
        print('Nota: ', self.nota)

#funcion para ver los resultados
    def resultado(self):
        if self.nota < 4:
            print('El Alumno no ha aprobado')
        else:
            print ('El alumno aprobo')

#crear los Objetos

alumnoA = Alumno()
alumnoB = Alumno()

#inicializar los objetos

alumnoA.Init('Juan', 8)
alumnoB.Init('Maria', 3.9)

#imprimir datos y resultados

alumnoA.imprimir()
alumnoA.resultado()
alumnoB.imprimir()
alumnoB.resultado()