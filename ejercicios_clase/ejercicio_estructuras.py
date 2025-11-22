"""
Crear una lista llamada estudiantes, donde cada elemento sea un diccionario con las siguientes claves:
"nombre", "edad", "nota"

1 - Cargar manualmemte 5 estudiantes
2 - Mostrar el promedio de notas por estudiante y general
3 - Listar los nombres de los estudiantes cuya nota sea mayor o igual a 6
4 - Listar el o los nombre/s del o los estudiante/s con la nota mas alta


Agregar al diccionario una key llamada division.
Las divisiones seran 312 y 313, las mismas pertenecientes a un set.
Listar los estudiantes de cada division.
Informar el porcentaje de estudiantes por division.
"""
from operation_tools.arrays_generales import *
from menu_tools.menu_utils import *
from input_tools.inputs import *

opciones_menu = ["1 - Cargar manualmemte 5 estudiantes",
                 "2 - Mostrar el promedio de notas por estudiante y general",
                 "3 - Listar los nombres de los estudiantes cuya nota sea mayor o igual a 6",
                 "4 - Listar el o los nombre/s del o los estudiante/s con la nota mas alta",
                 "5 - Listar los estudiantes de cada division",
                 "6 - Salir"
                 ]

estudiantes = []
seleccion_usuario = 0
divisiones = {"312", "313"}

def cargar_estudiante():
    estudiante = {"nombre": "",
                  "edad": -1,
                  "nota": -1}
    
    estudiante["nombre"] = input("Ingrese nombre del estudiante: ") 
    estudiante["edad"] = int(input("Ingrese edad del estudiante: ")) 
    estudiante["nota"] = int(input("Ingrese nota del estudiante: "))
    estudiante["division"] = str(random.randint(312, 313))
    
    return estudiante 

def cargar_estudiantes(estudiantes, cantidad : int = 5):
    for _ in range(cantidad):
        estudiante = cargar_estudiante()
        estudiantes.append(estudiante)
        
def obtener_promedio_estudiantes(estudiantes):
    suma_notas = 0
    promedio = 0
    
    for estudiante in estudiantes:
        suma_notas += estudiante["nota"]
        
    
    promedio = suma_notas / len(estudiantes)
    
    return promedio

def listar_estudiantes_nota_mayor(estudiantes, nota_min: int = 6):
    nombres_estudiantes = []
    for estudiante in estudiantes:
        if estudiante["nota"] > nota_min:
            nombres_estudiantes.append(estudiante["nombre"])
            
    listar_elementos(nombres_estudiantes)
        
def obtener_nota_mas_alta(estudiantes):
    nota_mas_alta = -1
    
    for estudiante in estudiantes:
        if estudiante["nota"] >= nota_mas_alta:
            nota_mas_alta = estudiante["nota"]
    
    return nota_mas_alta

def listar_estudiantes_mejor_nota(estudiantes):
    nota_mas_alta = obtener_nota_mas_alta(estudiantes)
    estudiantes_nota_alta = []
    
    for estudiante in estudiantes:
        if estudiante["nota"] == nota_mas_alta:
            estudiantes_nota_alta.append(estudiante["nombre"])
            
    listar_elementos(estudiantes_nota_alta) 
    
def obtener_porcentaje_estudiantes_division(estudiantes, division):
    contador_estudiantes = 0
    porcentaje_division = 0
    
    for estudiante in estudiantes:
        if estudiante["division"] == division:
            contador_estudiantes += 1
     
    if contador_estudiantes != 0:       
        porcentaje_division = contador_estudiantes * 100 / len(estudiantes)
        
    return porcentaje_division
        
    
def listar_divisiones(estudiantes):
    for division in divisiones:
        porcentaje_division = obtener_porcentaje_estudiantes_division(estudiantes, division)
        
        print(f"Division {division} - {porcentaje_division}% estudiantes:")
        
        for estudiante in estudiantes:
            if division == estudiante["division"]:
                print(estudiante["nombre"])
                
        print()
                

while seleccion_usuario != 6:
    print_menu(opciones_menu)
    seleccion_usuario = get_int(mensaje = f"Ingrese una opcion: ",
                            mensaje_error = "Ingreso incorrect1o, intente nuevamente: ",
                            minimo = 1,
                            maximo = 5,
                            reintentos = 100)

    match seleccion_usuario:
        case 1:
            cargar_estudiantes(estudiantes)
            
        case 2:
            promedio = obtener_promedio_estudiantes(estudiantes)
            print(f"El promedio de la nota de los estudiantes es: {promedio}")
        
        case 3:
            listar_estudiantes_nota_mayor(estudiantes)

        case 4:
            listar_estudiantes_mejor_nota(estudiantes)
            
        case 5:
            listar_divisiones(estudiantes)
        
        
                    
            