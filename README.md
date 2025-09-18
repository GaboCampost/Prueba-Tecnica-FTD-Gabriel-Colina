# Prueba-Tecnica-FTD-Gabriel-Colina

## Descripción del enfoque

Este programa compara las ventas registradas en un archivo JSO con los ajustes de inventario correspondientes para identificar discrepancias.
La solucion se basa en tres pasos principales:

1. Procesamiento de ventas: Donde se lee el archivo de ventas y suma las cantidades vendidas por producto identificado por su SKU.

2. Procesamiento de inventario: lee el archivo de inventario y suma unicamente las salidas por ventas (SALIDA_POR_VENTA) de cada SKU

3. Generacion del reporte: Se realiza la comparacion de las ventas y los movimientos de inventario de tal forma que se identifican los tres tipos de discrepancias:

    - VENTA_SIN_REGISTRO_INV: Ventas sin registro correspondiente en inventario
    - FALTANTE_EN_INVENTARIO: Menos unidades en inventario que las vendidas
    - SOBRANTE_EN_INVENTARIO: Más unidades en inventario que las vendidas
    - **SALIDA_INVENTARIO_SIN_VENTA** : Se da salida del inventario sin registrarse una venta. Este agregado puede servir para facilitar el análisis de los datos, al ser un caso posible en los datos.

## Requisitos
- Python 3.6 o superior

- No se requieren dependencias externas (solo módulos estándar de Python)

## Instrucciones de ejecución

1. Clonar o descargar el repositorio.
2. Navegar al directorio donde se encuentra el archivo reconciliar.py
3. Ejecutar el programa con los siguientes argumentos:

    ```
    python main.py ventas_dia_tienda_X.json movimientos_inventario_dia_tienda_X.json
    ```
    Donde tus archivos de entrada:  
        <ventas_dia_tienda_X.json> Sera tu archivo de ventas.
        <movimientos_inventario_dia_tienda_X.json> Sera tu archivo de movimientos en el inventario.
    Estos archivos deben estar en formato .JSON siguiendo el formato siguiente: 

    Ventas
    ```archivo_ventas.json
    [
        {
            "id_transaccion": "TXN001",
            "items": [
            {
                "sku": "SKU001",
                "cantidad": 1
            }
            ]
        }
    ]
    ```
    Inventario
    ```archivo_ventas.json
    [
        {
            "sku": "SKU002",
            "tipo": "SALIDA_POR_VENTA",
            "cantidad_ajustada": 7
        }
    ]
    ```

 ### Notas

 - El programa solo considera movimientos de inventario de tipo "SALIDA_POR_VENTA"
 - Las cantidades se procesan como valores enteros
 - En caso de no encontrar discrepancias, se mostrará un mensaje informativo