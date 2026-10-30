def analizar_centro_impresion():
    print("=" * 60)
    print("ANALIZADOR DE CONSUMO Y PRODUCCIÓN - CENTRO DE IMPRESIÓN 3D")
    print("=" * 60)
    
    # 1. Definición de la Matriz de Consumo (A) y el Vector de Recursos (B)
    A = [
        [3, 2, 1],
        [1, 2, 3],
        [2, 1, 2]
    ]
    
    B = [100, 80, 75]
    
    print("\n--- 3. ANÁLISIS DE COMPATIBILIDAD E INVERTIBILIDAD ---")
    det_A = 8.0  # Valor analítico precalculado
    print(f"Determinante de A: {det_A:.2f}")
    print("Resultado: [X] Compatible (Matriz invertible)")
    
    # 2. Matriz Inversa (A^-1) obtenida mediante Gauss-Jordan
    A_inv = [
        [1/8, -3/8, 1/2],
        [1/2, 1/2, -1],
        [-3/8, 1/8, 1/2]
    ]
    
    print("\n--- 4. DESARROLLO DE LA SOLUCIÓN ---")
    print("Matriz Inversa (A^-1):")
    for fila in A_inv:
        print([round(val, 4) for val in fila])
    
    # Multiplicación de la matriz inversa por el vector B (X = A^-1 * B)
    X = []
    for i in range(3):
        suma = 0
        for j in range(3):
            suma += A_inv[i][j] * B[j]
        X.append(suma)
    
    print("\nVector de Producción (X):")
    print(f"  - Piezas Básicas (x1): {X[0]:.0f}")
    print(f"  - Piezas Técnicas (x2): {X[1]:.0f}")
    print(f"  - Piezas Avanzadas (x3): {X[2]:.0f}")
    
    # Comprobación de la solución (AX = B)
    B_comprobacion = []
    for i in range(3):
        suma = 0
        for j in range(3):
            suma += A[i][j] * X[j]
        B_comprobacion.append(suma)
        
    print(f"\nComprobación (AX = B): {[round(val, 2) for val in B_comprobacion]} (Coincide exactamente con los recursos)")

    # 3. Análisis de Ingresos Económicos
    print("\n--- 6. ANÁLISIS DE INGRESOS ECONÓMICOS ---")
    precios = [50, 80, 120]  # Básica, Técnica, Avanzada
    
    # Cálculo de ingresos por tipo de pieza (Precio * Cantidad)
    ingresos_por_tipo = [precios[i] * X[i] for i in range(3)]
    
    print("\nIngresos por categoría:")
    print(f"  - Ingresos por piezas Básicas: Q{ingresos_por_tipo[0]:.2f}")
    print(f"  - Ingresos por piezas Técnicas: Q{ingresos_por_tipo[1]:.2f}")
    print(f"  - Ingresos por piezas Avanzadas: Q{ingresos_por_tipo[2]:.2f}")
    
    # Ingreso total
    ingreso_total = sum(ingresos_por_tipo)
    print("=" * 60)
    print(f"INGRESO TOTAL GENERADO: Q{ingreso_total:.2f}")
    print("=" * 60)

    # 4. Exportación nativa a Excel (Formato CSV compatible)
    archivo_salida = "reporte_centro_impresion.csv"
    try:
        with open(archivo_salida, mode="w", encoding="utf-8-sig") as f:
            f.write("Tipo de Pieza,Cantidad Producida,Precio Unitario (Q),Ingreso Generado (Q)\n")
            nombres_piezas = ["Piezas Básicas", "Piezas Técnicas", "Piezas Avanzadas"]
            for i in range(3):
                f.write(f"{nombres_piezas[i]},{round(X[i], 0)},{precios[i]},{ingresos_por_tipo[i]:.2f}\n")
            f.write(f"TOTAL GENERAL,,, {ingreso_total:.2f}\n")
            
        print(f"\n[ÉXITO] Reporte exportado a '{archivo_salida}' (Ábralo directamente con Excel).")
    except Exception as e:
        print(f"\n[AVISO] No se pudo guardar el archivo: {e}")

if __name__ == "__main__":
    analizar_centro_impresion()
