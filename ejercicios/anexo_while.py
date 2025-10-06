# Ejercicio 9

acumulador_suma = 0
contador_numeros = 0
respuesta_usuario = "s"
while respuesta_usuario == "s":
    num_sumar = int(input("Ingrese numero a sumar: "))
    acumulador_suma += num_sumar

    contador_numeros += 1

    if(contador_numeros >= 5):
        respuesta_usuario = input("Desea seguir sumando numeros? ingrese 's' para continar, 'n' para terminar")
        if (respuesta_usuario == "n") :
                break
        while(respuesta_usuario != "s" and respuesta_usuario != "n"):
            respuesta_usuario = input("Respuesta incorrecta, ingrese nuevamente 's' para continuar, 'n' para terminar")
            if (respuesta_usuario == "n") :
                break


print(f"Total de la suma: {acumulador_suma}")
print(f"Promedio: {acumulador_suma / contador_numeros}")

# Ejercicio 10

acumulador_suma = 0
contador_numeros = 0
respuesta_usuario = "s"
while respuesta_usuario == "s" and contador_numeros < 10:
    num_sumar = int(input("Ingrese numero a sumar: "))
    acumulador_suma += num_sumar

    contador_numeros += 1
    
    if(contador_numeros >= 5):
        respuesta_usuario = input("Desea seguir sumando numeros? ingrese 's' para continar, 'n' para terminar")
        if (respuesta_usuario == "n") :
                break
        while(respuesta_usuario != "s" and respuesta_usuario != "n"):
            respuesta_usuario = input("Respuesta incorrecta, ingrese nuevamente 's' para continuar, 'n' para terminar")
            if (respuesta_usuario == "n") :
                break


print(f"Total de la suma: {acumulador_suma}")
print(f"Promedio: {acumulador_suma / contador_numeros}")