import csv

# Abre el archivo CSV en modo lectura
with open('./TablaDatos.csv', 'r', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    
    # Itera sobre las filas del archivo CSV
    for fila in lector_csv:
        # fila contiene los datos de una fila del archivo CSV
        print(fila)
