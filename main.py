
import time
import os
import productos
import estadisticas

def menu_estadisticas():
    while True:
        os.system("cls")
        print("=== Menu Estadisticas ===")
        print("1. Producto Valor Más Alto")
        print("2. Producto Iva Más Bajo")
        print("3. Promedio Valor De Productos")
        print("4. Obtener Media Geometrica Del Valor De Los Productos")
        print("5. Retornar Al Menu Principal")
        
        opcion = productos.seleccionar_opcion(5)
        
        if opcion == 1:
            estadisticas.obtener_mas_alto()
        elif opcion == 2:
            estadisticas.obtener_mas_bajo()
        elif opcion == 3:
            estadisticas.promedio_ventas()
        elif opcion == 4:
            estadisticas.media_geometrica()
        elif opcion == 5:
            print("Saliendo Menu Estadisticas")
            return


def menu_general():
    while True:
        print("=== Menu ===")
        print("1. Asignar valores aleatorios ")
        print("2. Clasificar productos ")
        print("3. Ver estadísticas. ")
        print("4. Reporte de productos ")
        print("5. Salir del programa ")
        
        opcion = productos.seleccionar_opcion(5)
        if opcion == 1:
            print("--- Asignacion Ventas ---")
            productos.asignar_aleatorios()
        elif opcion == 2:
            print("Clasificar Productos")
            productos.clasificacion_productos()
        elif opcion == 3:
            print("Ver Estadisticas")
            menu_estadisticas()
        elif opcion == 4:
            print("Reporte De Productos")
            productos.reporte_productos()
        elif opcion == 5:
            print("Cerrando Programa.")
            time.sleep(2)
            print("Fin de la ejecución")
            print("Desarrollado Por Mati Droid")
            return
#inicialzacion del programa
menu_general()