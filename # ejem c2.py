# ejem c2
nivel = float(input("Nivel de agua (litros): "))

# comparacion
if nivel < 250:
    # accion
    print("Abrir la llave")
elif nivel > 450:
    # accion
    print("Cerrar la llave")
else:
    # accion
    print("Mantener como está (nivel adecuado)")