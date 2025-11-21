# ejem 7  cond
# entrada
x = int(input("Valor x: "))

# entrada_intervalos
a1 = int(input("Intervalo 1 - limite inferior: "))
b1 = int(input("Intervalo 1 - limite superior: "))

a2 = int(input("Intervalo 2 - limite inferior: "))
b2 = int(input("Intervalo 2 - limite superior: "))

a3 = int(input("Intervalo 3 - limite inferior: "))
b3 = int(input("Intervalo 3 - limite superior: "))

# comparacion
dentro1 = (x > a1 and x < b1)
dentro2 = (x > a2 and x < b2)
dentro3 = (x > a3 and x < b3)

# decision
if dentro1 or dentro2 or dentro3:
    # salida
    print("El numero esta DENTRO de al menos uno de los intervalos")
else:
    # salida
    print("El numero esta FUERA de todos los intervalos")