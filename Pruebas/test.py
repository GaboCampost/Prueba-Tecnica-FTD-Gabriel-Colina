import json
import tempfile
import os
import time
from reconciliar import procesar_ventas, procesar_inventario, generar_reporte

tt = 100000

def test_rendimiento_grandes_volumenes():
    
    # Generar datos
    ventas_masivas = []
    for i in range(tt):  
        ventas_masivas.append({
            "items": [
                {"sku": f"SKU_{i % 1000}", "cantidad": str((i % 5) + 1)}
            ]
        })
    
    inventario_masivo = []
    for i in range(50000):  # movimientos
        if i % 5 == 0:  # 20% son SALIDA_POR_VENTA
            inventario_masivo.append({
                "tipo": "SALIDA_POR_VENTA",
                "sku": f"SKU_{i % 1000}",
                "cantidad_ajustada": str((i % 5) + 1)
            })
        else:
            inventario_masivo.append({
                "tipo": "OTRO",
                "sku": f"SKU_{i % 1000}",
                "cantidad_ajustada": "0"
            })
    
    # Medir tiempo
    start_time = time.time()
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f_ventas:
        json.dump(ventas_masivas, f_ventas)
        archivo_ventas = f_ventas.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f_inv:
        json.dump(inventario_masivo, f_inv)
        archivo_inventario = f_inv.name
    
    ventas = procesar_ventas(archivo_ventas)
    inventario = procesar_inventario(archivo_inventario)
    discrepancias = generar_reporte(ventas, inventario)
    
    end_time = time.time()
    
    tiempo_ejecucion = end_time - start_time
    
    # Borrar temps
    os.unlink(archivo_ventas)
    os.unlink(archivo_inventario)
    
    return tiempo_ejecucion, len(discrepancias)

# Prueba
if __name__ == "__main__":
    print("Prueba.")
    tiempo, discrepancias = test_rendimiento_grandes_volumenes()
    
    # Análisis adicional
    print(f"\n Resumen de rendimiento:")
    print(f"- Tiempo total: {tiempo:.2f} segundos")
    print(f"- Discrepancias detectadas: {discrepancias}")
    print(f"- {tt/tiempo:.0f} transacciones/segundo")