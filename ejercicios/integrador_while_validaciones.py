print("Por favor, ingrese sus datos a continuacion")

apellido = input("Ingrese su apellido:\n")

edad = int(input("Ingrese su edad (entre 18 y 90):\n"))
while edad < 18 or edad > 90:
    edad = int(input("Respuesta incorrecta, ingrese nuevamente. \nIngrese su edad (entre 18 y 90):\n"))

estado_civil = input("Ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a, Viudo/a):\n")
while estado_civil != "Soltero" and estado_civil != "Soltera" and estado_civil != "Casado" and estado_civil != "Casada" and estado_civil != "Divorciado" and estado_civil != "Divorciada" and estado_civil != "Viudo" and estado_civil != "Viuda":
    estado_civil = input("Respuesta incorrecta, ingrese nuevamente. \nIngrese su estado civil (Soltero/a, Casado/a, Divorciado/a, Viudo/a):\n")

numero_legajo = int(input("Ingrese su numero de legajo:\n"))
while numero_legajo < 1000:
    numero_legajo = int(input("Respuesta incorrecta, ingrese nuevamente. \nIngrese su numero de legajo:\n"))

print("\n\n################\n\n") # Para visualizar mejor el output

print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estado civil: {estado_civil}")
print(f"Numero de legajo: {numero_legajo}")