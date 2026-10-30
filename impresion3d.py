import pandas as pd
import plotly.express as px

def analizar_centro_impresion():
    print("=" * 65)
    print("   ANALIZADOR DE CONSUMO Y PRODUCCIÓN - CENTRO DE IMPRESIÓN 3D   ")
    print("=" * 65)
    
    # 1. Definición de la Matriz de Consumo (A) y el Vector de Recursos (B)
    A = [
        [3.0, 2.0, 1.0],
        [1.0, 2.0, 3.0],
        [2.0, 1.0, 2.0]
    ]
    
    B = [100.0, 80.0, 75.0]
    
    print("\n--- 3. ANÁLISIS DE COMPATIBILIDAD E INVERTIBILIDAD ---")
    det_A = 8.0  # Valor analítico precalculado
    print(f"Determinante de A: {det_A:.2f}")
    print("Resultado: [✔] Compatible (Matriz invertible)")
    
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
        suma = sum(A_inv[i][j] * B[j] for j in range(3))
        X.append(suma)
    
    nombres_piezas = ["Piezas Básicas", "Piezas Técnicas", "Piezas Avanzadas"]
    
    print("\nVector de Producción Óptimo (X):")
    for i in range(3):
        print(f"  - {nombres_piezas[i]}: {X[i]:.0f} unidades")
    
    # Comprobación de la solución (AX = B)
    B_comprobacion = [sum(A[i][j] * X[j] for j in range(3)) for i in range(3)]
    print(f"\nComprobación (AX = B): {[round(val, 2) for val in B_comprobacion]} (100% Exacto)")

    # 3. Análisis de Ingresos Económicos
    print("\n--- 6. ANÁLISIS DE INGRESOS ECONÓMICOS ---")
    precios = [50.0, 80.0, 120.0]  # Básica, Técnica, Avanzada
    
    # Cálculo de ingresos por tipo de pieza (Precio * Cantidad)
    ingresos_por_tipo = [precios[i] * X[i] for i in range(3)]
    
    print("\nIngresos por categoría:")
    for i in range(3):
        print(f"  - {nombres_piezas[i]}: Q{ingresos_por_tipo[i]:,.2f}")
    
    # Ingreso total
    ingreso_total = sum(ingresos_por_tipo)
    print("=" * 65)
    print(f"INGRESO TOTAL GENERADO: Q{ingreso_total:,.2f}")
    print("=" * 65)

    # 4. Generación del Dashboard Interactivo (Guarda un archivo HTML seguro)
    print("\n[INFO] Generando el dashboard interactivo...")
    try:
        data_df = {
            'tipo_pieza': nombres_piezas,
            'cantidad_producida': [round(val, 0) for val in X],
            'precio_unitario': precios,
            'ingreso_generado': ingresos_por_tipo
        }
        df = pd.DataFrame(data_df)
        
        # Crear gráfico interactivo de barras con Plotly
        fig = px.bar(
            df,
            x='tipo_pieza',
            y='cantidad_producida',
            color='tipo_pieza',
            text='cantidad_producida',
            hover_data=['precio_unitario', 'ingreso_generado'],
            title='Dashboard Interactivo: Producción y Rendimiento - Centro de Impresión 3D',
            labels={
                'tipo_pieza': 'Categoría de Pieza', 
                'cantidad_producida': 'Unidades Producidas'
            }
        )
        
        fig.update_traces(texttemplate='%{text} unidades', textposition='outside')
        fig.update_layout(
            xaxis_title="Tipo de Pieza",
            yaxis_title="Cantidad Óptima (Unidades)"
        )
        
        # Guardar en HTML para evitar bloqueos del sistema operativo
        archivo_html = "dashboard_impresion.html"
        fig.write_html(archivo_html)
        print(f"[ÉXITO] Dashboard guardado como '{archivo_html}' en tu carpeta.")
        print("        (Puedes abrirlo con doble clic en cualquier navegador web).")
        
        # Intenta lanzarlo automáticamente
        fig.show()
        
    except Exception as e:
        print(f"[AVISO] No se pudo desplegar automáticamente el gráfico: {e}")

if __name__ == "__main__":
    analizar_centro_impresion()
