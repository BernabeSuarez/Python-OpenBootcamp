#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
import pickle

class Vehiculo:
    marca=''
    modelo= 0

    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo

    def getName(self):
        return self.marca

c = Vehiculo('Peugeot', 2008)

b = open('data.bin', 'wb') #crea el archivo a guardar
pickle.dump(c, b) #guarda el archivo en el fichero
b.close() 

f = open('data.bin','rb')  #abre el archivo binario
datos = pickle.load(f)  #pickle.load(file) decodifica el archivo pra poder utilizarlo

print(datos.getName())