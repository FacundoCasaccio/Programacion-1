# Ejercicio 1
i = 1
while i <= 10:
    print(i)
    i += 1  

# Ejercicio 2
i = 10
while i >= 1:
    print(i)
    i -= 1  

# Ejercicio 3
i = 1
acumulador_suma = 0
while i <= 10:
    acumulador_suma += i
    print(acumulador_suma)
    i += 1  

# Ejercicio 4
i = 1
acumulador_suma = 0
while i <= 10:
    if i % 2 == 0:
        acumulador_suma += i
        print(acumulador_suma)
    i += 1  

# Ejercicio 5
acumulador_suma = 0
contador_numeros = 0
while contador_numeros < 5:
    num_sumar = int(input("Ingrese numero a sumar: "))
    acumulador_suma += num_sumar

    contador_numeros += 1


print(f"Total de la suma: {acumulador_suma}")
print(f"Promedio: {acumulador_suma / 5}")

# Ejercicio 6
acumulador_suma = 0
contador_numeros = 0
respuesta_usuario = "s"
while respuesta_usuario == "s":
    num_sumar = int(input("Ingrese numero a sumar: "))
    acumulador_suma += num_sumar

    contador_numeros += 1
    respuesta_usuario = input("Desea seguir sumando numeros? ingrese 's' para continar, 'n' para terminar")
    if (respuesta_usuario == "n") :
            break
    while(respuesta_usuario != "s" and respuesta_usuario != "n"):
        respuesta_usuario = input("Respuesta incorrecta, ingrese nuevamente 's' para continuar, 'n' para terminar")
        if (respuesta_usuario == "n") :
            break


print(f"Total de la suma: {acumulador_suma}")
print(f"Promedio: {acumulador_suma / contador_numeros}")

# Ejercicio 7
acumulador_suma = 0
acumulador_producto = 0
contador_numeros = 0
respuesta_usuario = "s"

while respuesta_usuario == "s":
    numero_ingresado = int(input("Ingrese un numero: "))
    if numero_ingresado >= 0:
        acumulador_suma += numero_ingresado
    else:
        if acumulador_producto == 0:
              acumulador_producto = numero_ingresado
        else:
             acumulador_producto *= numero_ingresado

    contador_numeros += 1
    respuesta_usuario = input("Desea seguir ingresando numeros? ingrese 's' para continar, 'n' para terminar")
    if (respuesta_usuario == "n") :
            break
    while(respuesta_usuario != "s" and respuesta_usuario != "n"):
        respuesta_usuario = input("Respuesta incorrecta, ingrese nuevamente 's' para continuar, 'n' para terminar")
        if (respuesta_usuario == "n") :
            break


print(f"Total de la suma de los numeros positivos: {acumulador_suma}")
print(f"Total del producto de los numeros negativos: {acumulador_producto}")

# Ejercicio 8
contador_numeros = 1
numero_maximo = 0
numero_minimo = 0

while contador_numeros <= 10:
    numero_actual = int(input("Ingrese un numero: "))

    if numero_actual > numero_maximo:
        numero_maximo = numero_actual
    elif numero_actual < numero_minimo:
        numero_minimo = numero_actual

    contador_numeros += 1

print(f"El maximo numero ingresado es {numero_maximo}")
print(f"El minimo numero ingresado es {numero_minimo}")

