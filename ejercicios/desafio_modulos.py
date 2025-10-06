from input_tools import inputs

print("Bienvenido, elija una opcion a continuacion\n")
opcion_elegida = int(input("1- Validar entero \n2- Validar decimal \n3- Validar string\n"))

while opcion_elegida != 1 and opcion_elegida != 2 and opcion_elegida != 3:
    print("Opcion incorrecta, elija nuevamente...\n")
    opcion_elegida = int(input("1- Validar entero\n2- Validar decimal\n 3- Validar string\n"))

input_usuario = None

if opcion_elegida == 1:
    input_usuario = inputs.get_int(
                mensaje = "A continuacion, se validara un numero entero",
                mensaje_error = "Ingreso incorrecto",
                minimo = 5,
                maximo = 10,
                reintentos = 2
                  )
    print(input_usuario)
    
elif opcion_elegida == 2:
    input_usuario = inputs.get_float(
                mensage = "A continuacion, se validara un numero flotante",
                mensaje_error = "Ingreso incorrecto",
                minimo = 5,
                maximo = 10,
                reintentos = 2
                  )
    print(input_usuario)

elif opcion_elegida == 3:
    input_usuario = inputs.get_string_with_length(
                mensage = "A continuacion, se validara un numero flotante",
                mensaje_error = "Ingreso incorrecto",
                reintentos = 2,
                longitud = 5
                  )
    print(input_usuario)
    
