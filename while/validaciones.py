# # Ejercicio 1
# clave_correcta = "123"
# clave = input("Ingrese su clave: ")

# while clave != clave_correcta:
#     clave = input("Clave incorrecta, ingrese nuevamente: ")

# print("Ingreso exitoso!")

# Ejercicio 2
# clave_correcta = "123"
# clave = input("Ingrese su clave: ")
# intentos = 1

# while clave != clave_correcta and intentos < 3:
#     clave = input(f"Clave incorrecta, le quedan {3 - intentos} intento, ingrese nuevamente: ")
#     intentos += 1

# if intentos >= 3:
#     print("Su cuenta ha sido bloqueada")
# else:
#     print("Ingreso exitoso!")

# Ejercicio 3
# nota = 0

# while nota < 1 or nota > 10:
#     nota = int(input("Ingrese su nota: "))

# Ejercicio 4
color = ""

while color != "Rojo" and color != "Verde" and color != "Azul":
    color = input("Ingrese un color: ")