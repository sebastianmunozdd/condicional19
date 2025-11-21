# jem4 c
# entrada
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
n5 = float(input("Nota 5: "))

# promedio
definitiva = (n1 + n2 + n3 + n4 + n5) / 5

# comparacion
if definitiva > 3.5:
    # salida
    print("Gano el curso")
else:
    # salida
    print("Perdio el curso")

# mostrar_nota
print("Nota final:", definitiva)