contador_masculinos_iot_ia_25_50 = 0
contador_ia_negativos_33_40 = 0
edad_mayor_masculino = 0
nombre_mayor_masculino = None
voto_mayor_masculino = None
cantidad_emepleados = 0

while cantidad_emepleados < 10:
    # Input y validacion
    nombre_empleado = input("Ingrese su nombre:\n")

    edad_empleado = int(input("Ingrese su edad:\n"))
    while edad_empleado < 18:
        edad_empleado = int(input("Datos incorrectos. Ingrese su edad nuevamente:\n"))
    
    genero_empleado = input("Ingrese su genero (Masculino/Femenino/Otro):\n")
    while genero_empleado != "Masculino" and genero_empleado != "Femenino" and genero_empleado != "Otro":
        genero_empleado = input("Respuesta incorrecta. Ingrese su genero nuevamente (Masculino/Femenino/Otro):\n")

    voto_tecnologia_empleado = ""
    while voto_tecnologia_empleado != "IA" and voto_tecnologia_empleado != "RV/RA" and voto_tecnologia_empleado != "IOT":
        voto_tecnologia_empleado = input("Elija una de las siguientes tecnologias: \nIA \nRV/RA \nIOT \n")

    # Procesamiento de datos
    if genero_empleado == "Masculino":
        if edad_empleado > edad_mayor_masculino:
            edad_mayor_masculino = edad_empleado
            nombre_mayor_masculino = nombre_empleado
            voto_mayor_masculino = voto_tecnologia_empleado

        if edad_empleado >= 25 and edad_empleado <= 50 and voto_tecnologia_empleado != "RV/RA": 
            contador_masculinos_iot_ia_25_50 += 1
    
    if genero_empleado != "Femenino" and voto_tecnologia_empleado != "IA":
        if edad_empleado > 33 and edad_empleado < 40:
            contador_ia_negativos_33_40 += 1

    
    cantidad_emepleados += 1

porcentaje_no_ia_no_fem_33_40 = contador_ia_negativos_33_40 * 100 / cantidad_emepleados

# Output
print("\n\n###############\n\n")
if edad_mayor_masculino != 0:
    print(f"Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive): {contador_masculinos_iot_ia_25_50}")
    print(f"Empleado masculino de mayor edad: {nombre_mayor_masculino}, y su voto fue {voto_mayor_masculino}")
else:
    print("No hay empleados masculinos en la empresa")
print(f"Porcentaje de empleados no femeninos que NO votaron por IA y su edad está entre los 33 y 40 años: {porcentaje_no_ia_no_fem_33_40}")
