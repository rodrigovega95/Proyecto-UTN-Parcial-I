from funciones import *
'''● ID
● NombredelProyecto
● Descripción
● FechadeInicio
● FechadeFin
● Presupuesto
● Estado'''

nombre_archivo = 'Proyectos.csv'

# Lista donde descargo la info del archivo .csv
lista_datos = []

# Se abre el archivo .csv
with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
    # Lee todas las líneas del archivo
    lineas = archivo.readlines()    
    # Itera sobre las líneas y divide cada línea en columnas
    for linea in lineas:
        # Elimina los saltos de línea y separa por comas
        fila = linea.strip().split(',')
        # Se agregan fila por fila a la lista los datos
        lista_datos.append(fila)

lista_claves = lista_datos[0]
lista_proyectos = lista_datos

del lista_proyectos[0]

imprimir_menu()
