import math
import json
import productos

def promedio_ventas():
    todos_los_productos = productos.leer_archivo_json("./productos.json")
    
    suma_cantidades = 0
    for producto in todos_los_productos:
        suma_cantidades += producto['valor_venta']
        
    promedio = suma_cantidades / len(todos_los_productos)
    print(f"El promedio de los valores de las ventas de los productos es de {int(promedio)}")
    
def media_geometrica():
    todos_los_productos = productos.leer_archivo_json("./productos.json")
    
    suma_cantidades = 0
    for producto in todos_los_productos:
        suma_cantidades += math.log(producto['valor_bruto'])
        
    media = math.exp(suma_cantidades / len(todos_los_productos))
    print(f"La media geomtrica de los valores del valor bruto de los productos es de {int(media)}")
    
def obtener_mas_alto():
    todos_los_productos = productos.leer_archivo_json("./productos.json")
    #ordenar
    productos_ordenados = sorted(todos_los_productos, key=lambda x:x['valor_venta'],reverse=True)
    #print(productos_ordenados)
    for producto in productos_ordenados[:1]:
        print(f"El producto con valor más alto es: {producto['nombre']}")
        print(f"Su valor es de: ${producto['valor_venta']}")
        
def obtener_mas_bajo():
    todos_los_productos = productos.leer_archivo_json("./productos.json")
    #ordenar
    productos_ordenados = sorted(todos_los_productos, key=lambda x:x['valor_venta'],reverse=False)
    #print(productos_ordenados)
    for producto in productos_ordenados[:1]:
        print(f"El producto con valor más bajo es: {producto['nombre']}")
        print(f"Su valor es de: ${producto['valor_venta']}")

obtener_mas_alto()