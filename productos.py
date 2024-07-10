import random
import os
import json
import csv
def asignar_aleatorios():
    productos = ["Café Americano",
                 "Té Chai",
                 "Croissant",
                 "Jugo Naranja",
                 "Panini de Pavo y Queso",
                 "Pastel de Zanahoria",
                 "Espresso Doble",
                 "Batido de Frutas",
                 "Muffin", "Ensalada",
                 "Chocolate Caliente",
                 "Tarta de Frambuesa",
                 "Sándwich de Huevo",
                 "Galletas de Avena", 
                 "Frappé de Caramelo"]
    
    todos_los_productos = []
    
    for nombre_producto in productos:
        nombre = nombre_producto
        valor_bruto = random.randint(30,80)*100
        utilidad = int(valor_bruto * 0.4)
        iva = int(valor_bruto * 0.19)
        valor_venta = valor_bruto + utilidad + iva
        
        nuevo_producto = {
            'nombre':nombre,
            'valor_bruto':valor_bruto,
            'utilidad':utilidad,
            'iva':iva,
            'valor_venta':valor_venta
        }
        todos_los_productos.append(nuevo_producto)
    #aqui guardaremos nuestro registro en un json.
    guardar_archivo_json('productos.json',todos_los_productos)
    print("Valores De Los Productos Generados. . . ")
    
def guardar_archivo_json(ruta_archivo, datos):
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4)
        
def guardar_archivo_csv(dir,data,fieldnames):
    try:
        with open(dir,mode="w",newline='',encoding='utf-8') as archivo:
            data_csv = csv.DictWriter(archivo, fieldnames=fieldnames)
            data_csv.writeheader()
            data_csv.writerows(data)
    except:
        return []
def seleccionar_opcion(max_value):
    opcion = 0
    while True:
        try:
            opcion = int(input("Ingrese una opción >> "))
        except:
            pass
        if opcion < 1 or opcion > max_value:
            input("Opción inválida, intente nuevamente >> ")
        else:
            return opcion
    
def leer_archivo_json(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
       return json.load(archivo)

def clasificacion_productos():
    todos_los_productos = leer_archivo_json("./productos.json")
   
    categorias = {
        'menores a $5.000':[],
        'entre $5.001 a 7.000':[],
        'superior a $7.001':[]
    }
    for producto in todos_los_productos:
        if producto['valor_venta'] <= 5000:
            categorias["menores a $5.000"].append(producto)
        elif producto["valor_venta"] >= 5001 and producto["valor_venta"] <=7000:
            categorias["entre $5.001 a 7.000"].append(producto)
        elif producto["valor_venta"]> 7001:
            categorias["superior a $7.001"].append(producto)
            
    for clave, categoria,  in categorias.items():
        print("Productos",clave)
        print("Producto  Precio Venta")
        print("Cantidad",len(categoria))
        print("_______________________")
        print("\n")
        for producto in categoria:
            print(f"{producto['nombre']} -- {producto['valor_venta']}")
            print(" ")
        
    input("Presione Enter Para Continuar")
    os.system("cls")
        
#imprimir por pantalla reporte solicitado        
def reporte_productos():
    todos_los_productos = leer_archivo_json("./productos.json")
    
    print("Nombre Producto |  Valor Bruto  |  Utilidad  |  IVA   |   Precio Venta")
    print("----------------------------------------------------------------------")
    
    for producto in todos_los_productos:
        print(f"{producto['nombre']} \t\t${producto['valor_bruto']} \t{producto['utilidad']} \t{producto['iva']} \t{producto['valor_venta']}")

    fieldnames = ['nombre','valor_bruto','utilidad','iva','valor_venta']
    guardar_archivo_csv('reporte_producto.csv',todos_los_productos,fieldnames)
###############################################################################################################

