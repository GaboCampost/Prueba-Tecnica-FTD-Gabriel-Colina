import json
import os

def crear_archivos_ejemplo():
    #Crear json con pruebas
    
    # Datos de ventas
    ventas_data = [
        {
            "id_transaccion": "TXN001",
            "items": [
                { "sku": "SKU001", "cantidad": 2 },
                { "sku": "SKU002", "cantidad": 1 },
                { "sku": "SKU003", "cantidad": 3 }
            ]
        },
        {
            "id_transaccion": "TXN002",
            "items": [
                { "sku": "SKU001", "cantidad": 1 },
                { "sku": "SKU004", "cantidad": 2 }
            ]
        },
        {
            "id_transaccion": "TXN003",
            "items": [
                { "sku": "SKU002", "cantidad": 2 },
                { "sku": "SKU005", "cantidad": 1 },
                { "sku": "SKU006", "cantidad": 4 }
            ]
        },
        {
            "id_transaccion": "TXN004",
            "items": [
                { "sku": "SKU001", "cantidad": 1 },
                { "sku": "SKU007", "cantidad": 2 }
            ]
        },
        {
            "id_transaccion": "TXN005", 
            "items": [
                { "sku": "SKU003", "cantidad": 1 },
                { "sku": "SKU008", "cantidad": 3 }
            ]
        },
        {
            "id_transaccion": "TXN006",
            "items": [
                { "sku": "SKU002", "cantidad": 6 },
                { "sku": "SKU003", "cantidad": 4 }
            ]
        }
    ]
    
    # Datos de inventario
    inventario_data = [
        { "sku": "SKU001", "tipo": "SALIDA_POR_VENTA", "cantidad_ajustada": 3 },
        { "sku": "SKU002", "tipo": "SALIDA_POR_VENTA", "cantidad_ajustada": 5 },
        { "sku": "SKU003", "tipo": "ENTRADA_MERCANCIA", "cantidad_ajustada": 50 },
        { "sku": "SKU004", "tipo": "SALIDA_POR_VENTA", "cantidad_ajustada": 2 },
        { "sku": "SKU005", "tipo": "SALIDA_POR_VENTA", "cantidad_ajustada": 2 },
        { "sku": "SKU006", "tipo": "SALIDA_POR_DONACION", "cantidad_ajustada": 1 },
        { "sku": "SKU007", "tipo": "SALIDA_POR_VENTA", "cantidad_ajustada": 1 },
        { "sku": "SKU009", "tipo": "SALIDA_POR_VENTA", "cantidad_ajustada": 5 },
        { "sku": "SKU010", "tipo": "SALIDA_POR_VENTA", "cantidad_ajustada": 3 }
    ]
    
    # Guardar archivos
    with open('ventas_dia_tienda_101.json', 'w', encoding='utf-8') as f:
        json.dump(ventas_data, f, indent=2, ensure_ascii=False)
    
    with open('movimientos_inventario_dia_tienda_101.json', 'w', encoding='utf-8') as f:
        json.dump(inventario_data, f, indent=2, ensure_ascii=False)
    

if __name__ == "__main__":
    crear_archivos_ejemplo()