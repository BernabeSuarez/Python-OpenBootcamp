class Vehiculo:
    color = 'Azul'
    ruedas = 4
    puertas = 3

class Coche(Vehiculo):
   velocidad = 180
   cilindrada = 1600

c = Coche()

print(c.color)
print(c.cilindrada)