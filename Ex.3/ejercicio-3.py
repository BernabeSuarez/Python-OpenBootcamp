peso = input("Ingresa tu peso (Kg): ")
altura = input("Ingresa tu altura (mts): ")
pot = 2

calc = float(altura)**pot


imc = float(peso) / calc

masa = round(imc, 2)

print(f'Tu indice de masa corporal es de: {masa}')