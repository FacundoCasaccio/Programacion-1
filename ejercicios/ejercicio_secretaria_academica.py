from operation_tools.arrays_generales import cargar_notas, calcular_promedios, mostrar_datos_academicos_estudiantes

"""
Programa de Lista paralelas: 

La asistente académica tiene que verificar el promedio de notas de un estudiante. La lista de estudiantes a verificar son 4, estos estudiantes son: Juan, Marta, Andrea, Ana (Precargados en una función.). 

La asistente debe ingresar en el programa, (que nosotros vamos a crear) las notas de cada estudiante, cada estudiante tiene 3 notas y el programa debe calcular el promedio para mostrar los resultados en pantalla. 

Entonces, como programadores debemos: 
Crear una función para ingresar las notas de cada estudiante.
Crear una función que reciba la lista de notas y pueda calcular el promedio de notas de cada estudiante y almacenarlo en una lista de promedio. (El índice de la lista estudiante, corresponde al índice de la lista promedios)
Imprimir la lista de Estudiantes, sus notas y su promedio de notas. Se debe visualizar la lista de notas con respecto a los estudiantes.
"""

estudiantes = ["Juan", "Marta", "Andrea", "Ana"]
notas_estudiantes = cargar_notas(estudiantes, 3, "Ingrese nota del estudiante: ")
promedios = calcular_promedios(notas_estudiantes)

mostrar_datos_academicos_estudiantes(estudiantes, notas_estudiantes, promedios)




