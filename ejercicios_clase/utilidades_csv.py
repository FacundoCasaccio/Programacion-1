def leer_imprimir_csv(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        matriz = []
        nombres_columnas = archivo.readline().strip().split(",")

        for linea in archivo:
            linea = linea.rstrip("\n")
            fila = []
            valores = linea.split(",")

            for valor in valores:
                if valor.isdigit():
                    fila.append(int(valor))
                else:
                    fila.append(valor)

            matriz.append(fila)

    print(nombres_columnas)

    for fila in matriz:
        print(fila)
        
def escribir_csv(nombre_archivo, nombres_columnas, matriz_datos):
    with open(nombre_archivo + ".csv", "w") as archivo:
        archivo.write(",".join(nombres_columnas) + "\n")

        for fila in matriz_datos:
            linea = ""
            for i in range(len(fila)):
                linea += str(fila[i])
                if i < (len(fila) - 1):
                    linea += ","
            archivo.write(linea + "\n")
