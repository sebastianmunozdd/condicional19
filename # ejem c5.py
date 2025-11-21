# jem5 c
# entrada
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# operacion
discriminante = (b * b) - (4 * a * c)

# comparacion
if discriminante < 0:
    # salida
    print("La ecuacion NO tiene solucion real")
else:
    # salida
    print("La ecuacion Si tiene solucion real")