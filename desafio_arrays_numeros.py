from input_tools.inputs import get_int, get_fixed_int_list
from menu_tools.menu_utils import print_menu
from operation_tools import arrays_generales

opciones_menu = [
    "1- Ingresar datos (10 numero enteros entre -1000 y 1000)",
    "2- Cantidad de positivos y negativos",
    "3- Suma de numeros pares",
    "4- Mayor numero impar",
    "5- Listar numeros ingresados",
    "6- Listar los numeros pares",
    "7- Listar los numeros en posiciones impares",
    "8- Salir del programa\n"
]

numeros_ingresados = []
opcion_seleccionada = 0

while opcion_seleccionada != 8:
    print_menu(opciones_menu)
    
    opcion_seleccionada = get_int(mensaje = "Seleccione una opcion: ", 
                                  mensaje_error = "Opcion incorrecta, intente nuevamente",
                                  minimo = -1000,
                                  maximo = 1000,
                                  reintentos = 5)
    
    match opcion_seleccionada:
        case 1:
            numeros_ingresados = get_fixed_int_list(lenght = 10,
                                            mensaje = "Ingrese un numero entre -1000 y 1000: ", 
                                            mensaje_error = "Opcion incorrecta, intente nuevamente",
                                            minimo = -1000,
                                            maximo = 1000,
                                            reintentos = 5)
            
        case 2 if len(numeros_ingresados) != 0:
            cantidad_positivos = arrays_generales.contar_positivos(numeros_ingresados)
            cantidad_negativos = arrays_generales.contar_negativos(numeros_ingresados)
            print(f"Positivos: {cantidad_positivos}, Negativos: {cantidad_negativos}")
            
        case 3 if len(numeros_ingresados) != 0:
            print(f"La suma de los pares ingresados es: {arrays_generales.sumar_pares(numeros_ingresados)}")
            
        case 4 if len(numeros_ingresados) != 0:
            print(f"El mayor impar es: {arrays_generales.determinar_mayor_impar(numeros_ingresados)}")
            
        case 5 if len(numeros_ingresados) != 0:
            arrays_generales.listar_elementos(numeros_ingresados)
            
        case 6 if len(numeros_ingresados) != 0:
            arrays_generales.listar_pares(numeros_ingresados)
        
        case 7 if len(numeros_ingresados) != 0:
            arrays_generales.listar_posiciones_impares(numeros_ingresados)
        
        case 8 if len(numeros_ingresados) != 0:
            print("Gracias por utilizar el programa, hasta la proxima!")
            
    
    if len(numeros_ingresados) == 0 and opcion_seleccionada != 1 and opcion_seleccionada != 8:
        print("Debe ingresar numeros primero para realizar alguna operacion.\n")
        
    print("\n\n\n") # Para separar las iteraciones yt se lea mejor
             
        
            
