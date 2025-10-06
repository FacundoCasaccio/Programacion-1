"""
Desarrollar algoritmicamente en Python:
Una institución educativa desea procesar los datos de sus estudiantes.
Para ello, se tienen los siguientes datos:
• Una matriz de números enteros de 30 filas por 5 columnas que corresponde a las calificaciones, donde:
• Cada fila representa un estudiante.
• Cada columna representa una materia.
• Cada valor en la intersección es una calificación entera entre 1 y 10.
• Una lista de apellido y nombre de los estudiantes.
• Una lista de géneros de los estudiantes. Cada género debe ser alguno de los siguientes: ['F' | 'M' | 'X*]
: Una lista de legados de los estudioses Ca tho ono core octico de ipe enta de seis cifras.
Cada una de estas listas, se corresponden con las filas de la matriz. Es decir, que se debe trabajar como listas
paralelas entre la matriz y las otras listas.
Se deberá programar un menú de opciones operado por consola, que realice lo siguiente:
1 - Realizar la carga de los datos en la matriz y en cada una de las listas. (Se pueden hardcodear los datos).
Realizar una función para validar cada dato a ser cargado.
2 - Mostrar todos los datos, esto es la matriz completa de calificaciones conjuntamente con las listas de legajo, género y nombre del estudiante, siempre y cuando su estado tenga el valor uno. Realizar una función que recorra
todos y otra que muestre uno.
3 - Calcular el promedio de cada estudiante y guardarlo en una nueva lista de promedios. Realizar una función
cue calcule el promedio.
4 - Ordenar y mostrar los datos de los estudiantes por promedio de manera DESC. Realizar una función que ordene, la cual deberá ordenar de manera ASC o DESC de acuerdo a un parámetro de ordenamiento.
5 - Mostrar la/s materia/s con mayor promedio general. Realizar una función para recorrer todas y otra para mostrar una. Teniendo en cuenta que no hay una lista de materias, sino que cada columna de la matriz representa una materia, entonces cada materia tomará la siguiente nomenclatura para su nombre MATERIA_ indice más uno. Por ejemplo: para la materia del indice cero de la columna, será MATERIA_1.
6 - Buscar y mostrar todos los datos de un estudiante por legajo, incluyendo el promedio calculado en el ítem 3.
Realizar una función de búsqueda. Realizar una función que recorra uno y otra que muestre todos.
7- Buscar y mostrar cuantas veces se repite cada calificación en una asignatura determinada.
Realizar una función que reciba la matriz de calificaciones y el número de materia (indice más uno) como parámetros, y retorne una lista de 10 elementos, donde en el indice 0 estará la cantidad de veces que se repite la nota 1, en el indice 1 estará la cantidad de veces que se repite la nota 2, y así sucesivamente hasta el indice 9 donde estará la cantidad de veces que se repite la nota 10.
8 - Salir del programa.


NOTAS:
Nota 0: Los datos de la matriz y las listas podrán estar hardcodeados a los efectos de realizar las pruebas de
funcionamiento correspondientes.
Nota 1: No se podrá acceder a ningún ítem del menú, sin antes haber cargado los datos. En tal sentido, realizar
la validación correspondiente.
Nota 2: Los puntos deben ser accedidos mediante un menú de opciones.
Nota 3: Cada ítem del menú deberá ser una función.
Nota 4: Se deberá desarrollar biblioteca y funciones propias, las mismas deberán estar correctamente documentadas.
Nota 5: Se deberá desarrollar una función para la validación de cada uno de los datos.
Nota 6: Desarrollar una función que recorra los elementos (mostrar todos) y otra que muestre un elemento
(mostrar uno). La segunda será llamada dentro de la primera.
Nota 7: Para realizar el menú de opciones, se deberá utilizar la estructura de control match.
Nota 8: El menú de opciones deberá estar contenido dentro (anidado) de una estructura de control while
"""
from prog_1_pp.utilidades_listas import *
from prog_1_pp.utilidades_input import *
from prog_1_pp.implementacion_menu import *
from prog_1_pp.estudiantes_hardcodeados import pre_cargar_estudiantes

CANTIDAD_ESTUDIANTES = 30
CANTIDAD_MATERIAS = 5

opciones_menu = [
    "1 - Cargar datos de estudiantes",
    "2 - Mostrar datos de estudiantes",
    "3 - Calcular promedios de estudiantes",
    "4 - Mostrar promedios en orden descendente",
    "5 - Mostrar materias con mayor promedio",
    "6 - Mostrar datos de estudiante por legajo",
    "7 - Mostrar cantidad de notas repetidas en asignatura",
    "8 - Salir\n\n",
]
        
def ejecutar_programa(debug = False):
    
    if debug:
        calificaciones_estudiantes, nombres_estudiantes, generos_estudiantes, legajos_estudiantes, estados_estudiantes = pre_cargar_estudiantes()
        estudiantes_cargados = True
    else:
        calificaciones_estudiantes = generar_matriz_de_elemento(filas = CANTIDAD_ESTUDIANTES, columnas = CANTIDAD_MATERIAS, elemento = 0)
        nombres_estudiantes = generar_array_de_elemento(longitud = CANTIDAD_ESTUDIANTES, elemento = None)
        generos_estudiantes = generar_array_de_elemento(longitud = CANTIDAD_ESTUDIANTES, elemento = None)
        legajos_estudiantes = generar_array_de_elemento(longitud = CANTIDAD_ESTUDIANTES, elemento = None)
        estados_estudiantes = generar_array_de_elemento(longitud = CANTIDAD_ESTUDIANTES, elemento = 0)
        estudiantes_cargados = False
        
    promedios_estudiantes = generar_array_de_elemento(longitud = CANTIDAD_ESTUDIANTES, elemento = None)
    seleccion_usuario = 0
    promedios_calculados = False
    
    while seleccion_usuario != 8:
        imprimir_menu(opciones_menu)
        seleccion_usuario = obtener_entero(mensaje = f"Ingrese una opcion: ",
                                mensaje_error = "Ingreso incorrecto, intente nuevamente: ",
                                minimo = 1,
                                maximo = 8,
                                reintentos = 100)
    
        match seleccion_usuario:
            case 1:
                pedir_y_cargar_datos_estudiante(calificaciones_estudiantes, 
                                                nombres_estudiantes,
                                                generos_estudiantes,
                                                legajos_estudiantes,
                                                estados_estudiantes
                                                )
                
                estudiantes_cargados = True
                promedios_calculados = False
            case 2 if estudiantes_cargados:
                mostrar_datos_estudiantes(calificaciones_estudiantes, 
                                            nombres_estudiantes,
                                            generos_estudiantes,
                                            legajos_estudiantes,
                                            estados_estudiantes,
                                            promedios_estudiantes
                                            )

            case 3 if estudiantes_cargados:
                promedios_estudiantes = calcular_promedios_estudiantes(calificaciones_estudiantes, estados_estudiantes)
                promedios_calculados = True
                
            case 4 if estudiantes_cargados and promedios_calculados:
                mostrar_datos_por_promedio(calificaciones_estudiantes, 
                                                nombres_estudiantes,
                                                generos_estudiantes,
                                                legajos_estudiantes,
                                                estados_estudiantes,
                                                promedios_estudiantes,
                                                ascendente = False
                                                )
                
            case 5 if estudiantes_cargados:
                mostrar_materias_mas_promedio(calificaciones_estudiantes, estados_estudiantes)
                
            case 6 if estudiantes_cargados:
                mostrar_datos_por_legajo(calificaciones_estudiantes, 
                                        nombres_estudiantes,
                                        generos_estudiantes,
                                        legajos_estudiantes,
                                        estados_estudiantes,
                                        promedios_estudiantes
                                        )
                
            case 7 if estudiantes_cargados: 
                mostrar_notas_repetidas_materias(calificaciones_estudiantes, estados_estudiantes)
                
            case 8:
                print("Finalizando programa, hasta luego!")
                
            case _:
                mostrar_mensajes_error(seleccion_usuario, estudiantes_cargados, promedios_calculados)
                
        print() # para separar de la posterior impresion del menu

ejecutar_programa(debug = False)