# Fase 5 - Evaluación Final POA
# Problema 3: Auditoría de inventario y reabastecimiento
# Grupo: 213022_883
# Programa: Ingeniería de Sistemas
# Código fuente: autoría propia
# -*- coding: utf-8 -*-

def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """Compara el stock actual con el mínimo y retorna cantidad y estado."""
    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
        estado = "Reabastecer"
    else:
        cantidad = 0
        estado = "No requiere pedido"

    return cantidad, estado


def mostrar_informe(inventario):
    """Muestra el informe de reabastecimiento del inventario."""
    print("INFORME DE REABASTECIMIENTO")
    print("-" * 95)
    print("{:<8} {:<18} {:>12} {:>12} {:>15} {:<22}".format(
        "Código", "Artículo", "Actual", "Mínimo", "Pedir", "Estado"
    ))
    print("-" * 95)

    for articulo in inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad_pedir, estado = calcular_cantidad_pedir(
            stock_actual, stock_minimo
        )

        print("{:<8} {:<18} {:>12} {:>12} {:>15} {:<22}".format(
            codigo, nombre, stock_actual, stock_minimo, cantidad_pedir, estado
        ))


inventario = [
    ["ART001", "Teclado", 8, 15],
    ["ART002", "Mouse", 12, 10],
    ["ART003", "Monitor", 4, 9],
    ["ART004", "Memoria USB", 25, 25],
    ["ART005", "Disco duro", 2, 6]
]

mostrar_informe(inventario)
