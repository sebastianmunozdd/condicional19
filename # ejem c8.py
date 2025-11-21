# ejem 8 cond
# entrada
tipo = input("Tipo de articulo: ")
precio = float(input("Precio del articulo: "))

# comparacion
if tipo == "Textil":
    descuento = 0
elif tipo == "Electrodomestico":
    descuento = precio * 0.037
elif tipo == "Elementos de cocina":
    descuento = precio * 0.042
elif tipo == "Video juego":
    descuento = precio * 0.078
else:
    # error
    descuento = 0
    print("Tipo no valido")

# salida
print("Descuento:", descuento)