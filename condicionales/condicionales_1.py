# Ejercicio 1

altura = float(input("Ingrese altura del jugador en centimetros: "))
posicion = None

if (altura < 160):
    posicion = "Base"
elif (altura < 180):
    posicion = "Escolta"
elif (altura < 200):
    posicion = "Alero"
else:
    posicion = "Pivot"

print(f"El jugador tiene la posicion de {posicion}")