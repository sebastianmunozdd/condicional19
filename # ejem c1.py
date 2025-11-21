# ejem c1
costo = float(input("Costo: "))

# comparacion
if costo > 150000:
    # multiplicacion
    descuento = costo * 0.05
else:
    # asignacion
    descuento = 0

# salida
print("Descuento:", descuento)