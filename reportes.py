
from analisis import calcular_promedio
from analisis import calcular_porcentajes
from analisis import analizar_longitud
from analisis import contar_palabras
from analisis import contar_apariciones
from analisis import contiene_termino


def mostrar_reporte_reseña(reseña):
    """Muestra los datos y las estadísticas de una reseña."""

    print("\n========== REPORTE DE RESEÑA ==========")
    print(f"ID:          {reseña[0]}")
    print(f"Título:      {reseña[1]}")
    print(f"Puntuación:  {reseña[3]}/10")
    print(f"Caracteres:  {analizar_longitud(reseña[2])}")
    print(f"Palabras:    {contar_palabras(reseña[2])}")
    print(f"Texto:       {reseña[2]}")
    print("========================================")


def mostrar_reporte_general(reseñas):
    """Muestra el promedio y los porcentajes de las reseñas."""

    print("\n========== REPORTE GENERAL ==========")

    try:
        promedio = calcular_promedio(reseñas)
        print(f"Promedio de puntuaciones: {promedio:.2f}")
    except ZeroDivisionError as error:
        print(f"No se pudo calcular el promedio: {error}")

    try:
        porcentaje_positivas, porcentaje_negativas = calcular_porcentajes(reseñas)

        print(f"Reseñas positivas: {porcentaje_positivas:6.2f}%")
        print(f"Reseñas negativas: {porcentaje_negativas:6.2f}%")
    except ZeroDivisionError as error:
        print(f"No se pudieron calcular los porcentajes: {error}")

    print("=====================================")


def mostrar_reporte_termino(texto, termino):
    """Muestra las apariciones y la presencia de un término."""

    cantidad = contar_apariciones(texto, termino)
    encontrado = contiene_termino(texto, termino)

    print("\n========== REPORTE DE TÉRMINO ==========")
    print(f"Término buscado:  {termino}")
    print(f"Apariciones:      {cantidad}")
    print(f"¿Está presente?:  {encontrado}")
    print("========================================")
