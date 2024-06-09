def imprimir_menu():
    print("\n Seleccione una opción: \n")
    print("1. Ingresar proyecto")
    print("2. Modificar proyecto")
    print("3.Cancelar proyecto")
    print("4. Comprobar proyectos")
    print("5. Mostrar todos")
    print("6. Calcular presupuesto promedio")
    print("7. Buscar proyecto por nombre")
    print("8. Ordenar proyectos")
    print("9. Retomar proyecto")
    print("10. Proyectos que superen 'x' presupuesto")
    print("11. Informe de un proyecto")
    print("12. Salir")

'''● ID
● NombredelProyecto
● Descripción
● FechadeInicio
● FechadeFin
● Presupuesto
● Estado'''

def ingresar_proyecto():
    lista_proyecto = []

    contador_id = 11
    lista_proyecto.append(contador_id)
    contador_id +=1 

    nombre_proyecto = input("Por favor, coloque el nombre del proyecto.")
    lista_proyecto.append(nombre_proyecto)

    descripcion_proyecto = input("Por favor, coloque una descripción de este proyecto.")
    lista_proyecto.append(descripcion_proyecto)

    fecha_inicio = input("Coloque a continuación la fecha de inicio del proyecto.") 
    lista_proyecto.app
    fecha_fin = input("Coloque por favor la fecha de finalización del proyecto.")
    presupuesto_proyecto = int(input("Díganos el presupuesto que posee el proyecto por favor."))
    estado = "Activo"



    pass

def modificar_proyecto():
    pass

def cancelar_proyecto():
    pass

def comprobar_proyecto():
    pass

def mostrar_todos():
    pass

def calcular_presupuesto_promedio():
    pass

def buscar_por_nombre():
    pass

def ordenar_proyectos():
    pass

def retomar_proyecto():
    pass

def proyecto_que_supere_presupuesto():
    pass

def informe_proyecto():
    pass


'''Validaciones:
● NombredelProyecto: Debe contener solo caracteres alfabéticos y no exceder los 30
caracteres. No pueden contener números ni caracteres especiales.
● Descripción: Debe ser un texto alfanumérico de no más de 200 caracteres.
● Presupuesto: Debe ser un valor numérico entero no menor a $500000.
● FechadeInicio y Fecha de Fin: Deben ser fechas válidas en el formato "DD/MM/AAAA".
● LaFechadeFinnopuedeseranterior a la Fecha de Inicio.
● Elestado debe deiniciar como ‘Activo’, pudiendo ser también ‘Cancelado’ o ‘Finalizado’'''

def validar_nombre():
    pass

def validar_descripcion():
    pass

def validar_presupuesto():
    pass

def validar_fecha():
    pass

def vildar_estado():
    pass

