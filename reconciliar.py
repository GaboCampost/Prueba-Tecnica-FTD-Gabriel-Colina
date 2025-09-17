import json
from collections import defaultdict
import sys
import os

def procesar_ventas(archivo_ventas):
    #Tomar ventas del archivo .json y crear un diccionario por sku
    ventas_por_sku = defaultdict(int) #Iniciar diccionario

    #Tomar archivo json e ingresar al diccionario
    try:
        
        with open(archivo_ventas, 'r', encoding='utf-8') as file:
            datos_ventas = json.load(file)       
        for trasaccion in datos_ventas:
            for item in trasaccion["items"]:
                cantidad= int(item['cantidad'])
                sku = item['sku']
                ventas_por_sku[sku] += cantidad
        print(f"Procesadas {len(datos_ventas)} transacciones de ventas")
        return dict(ventas_por_sku)
    except FileNotFoundError:
        print(f"Error, el archivo de ventas no ha sido encontrado: {archivo_ventas}")
    except Exception as e:
        print(f"Error 1: {e}")

def procesar_inventario(archivo_inventario):
    #Tomar el inventario segun la SALIDA_POR_VENTA
    inventario_por_sku= defaultdict(int)

    try:
        with open(archivo_inventario, 'r', encoding='utf-8') as file:
            datos_inventario = json.load(file)
        
        for movimiento in datos_inventario:
            mov =  "SALIDA_POR_VENTA"
            if movimiento['tipo'] == mov:
                sku = movimiento['sku']
                cantidad = int(movimiento['cantidad_ajustada'])
                inventario_por_sku[sku] += cantidad
        return inventario_por_sku
    except FileExistsError:
        print(f"Error, el archivo de ventas no ha sido encontrado: {archivo_inventario}")
    except Exception as e:
        print(f"Error 2: {e}")


def generar_reporte(ventas_por_sku,inventario_por_sku):

    #Aqui se guardan los errores
    discrepancias = []

    #Posibles errores
    ERR_REGISTRO = "VENTA_SIN_REGISTRO_INV"
    ERR_FALTANTE = "FALTANTE_EN_INVENTARIO"
    ERR_SOBRANTE = "SOBRANTE_EN_INVENTARIO"

    if not isinstance(ventas_por_sku,dict) or not isinstance(inventario_por_sku,dict):
        print(f"Los parametros deben ser diccionarios.")
    
    for sku in ventas_por_sku:
        #Verificar que la venta tenga registro en el inventario
        if sku not in inventario_por_sku:
            discrepancias.append({
                "sku": sku,
                "tipo_discrepancia": ERR_REGISTRO,
                "cantidad_vendida": ventas_por_sku[sku],
                "cantidad_inventario": 0
            })
        else:
            #Verificar que la venta 
            cantidad_ventas = ventas_por_sku[sku]
            cantidad_inventario = inventario_por_sku[sku]

            #Verificar validez
            if cantidad_inventario != cantidad_ventas:
                #Verificar tipo de fallo
                if cantidad_ventas < cantidad_inventario:
                    ERR_REGRISTRADO = ERR_SOBRANTE
                if cantidad_ventas > cantidad_inventario:
                    ERR_REGRISTRADO = ERR_FALTANTE
                #Agregar fallo
                discrepancias.append({
                        "sku": sku,
                        "tipo_discrepancia": ERR_REGRISTRADO,
                        "cantidad_vendida": ventas_por_sku[sku],
                        "cantidad_inventario": inventario_por_sku[sku]
                })

    #Crear el reporte_discrepancias.json
    if not discrepancias:
        print(f"No han ocurrido discrepancias")
    else:
        #Crearjson
        archivo_salida = "reporte_discrepancias.json"
        try:
            with open(archivo_salida, 'w', encoding='utf-8') as file: json.dump(discrepancias, file, indent=2, ensure_ascii=False, sort_keys=False)

            print(f"Reporte creado {archivo_salida}.")
            print(f"Numero de discrepancias {len(discrepancias)}.")

        except Exception as e:
            print(f"Error al crear el reporte {e}.")




def main(archivo_ventas,archivo_inventario):
    #Main definiendo flujo de funcion del programa
    try:
        ventas_por_sku = procesar_ventas(archivo_ventas)
        inventario_por_sku = procesar_inventario(archivo_inventario)
        generar_reporte(ventas_por_sku,inventario_por_sku)
    except Exception as e:
        print(f"Error en el proceso principal: {e}")
    return []

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error: Número incorrecto de argumentos")
        sys.exit(1)
    archivo_ventas = sys.argv[1]
    archivo_inventario = sys.argv[2]
    main(archivo_ventas,archivo_inventario)