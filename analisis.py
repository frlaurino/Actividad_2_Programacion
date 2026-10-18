
def analizar_longitud(texto):
    """Devuelve la cantidad de caracteres de una reseña."""
    return len(texto)


def contar_palabras(texto):
    """Devuelve la cantidad de palabras de una reseña."""
    palabras = texto.split()
    return len(palabras)


def contar_apariciones(texto, termino):
    """Cuenta las apariciones de un término sin distinguir mayúsculas."""
    texto = texto.lower()
    termino = termino.lower()
    return texto.count(termino)


def contiene_termino(texto, termino):
    """Indica si un término está presente sin distinguir mayúsculas."""
    texto = texto.lower()
    termino = termino.lower()
    return termino in texto


def calcular_promedio(reseñas):
    """Calcula el promedio de las puntuaciones de las reseñas."""
    if len(reseñas) == 0:
        raise ZeroDivisionError("No hay reseñas para calcular el promedio.")

    suma = 0

    for reseña in reseñas:
        suma += reseña[3]

    promedio = suma / len(reseñas)
    return promedio


def contar_por_clasificacion(reseñas):
    """Cuenta las reseñas positivas y negativas."""
    positivas = 0
    negativas = 0

    for reseña in reseñas:
        puntuacion = reseña[3]

        if puntuacion >= 6:
            positivas += 1
        else:
            negativas += 1

    return positivas, negativas


def calcular_porcentajes(reseñas):
    """Calcula los porcentajes de reseñas positivas y negativas."""
    if len(reseñas) == 0:
        raise ZeroDivisionError("No hay reseñas para calcular porcentajes.")

    positivas, negativas = contar_por_clasificacion(reseñas)

    porcentaje_positivas = positivas * 100 / len(reseñas)
    porcentaje_negativas = negativas * 100 / len(reseñas)

    return porcentaje_positivas, porcentaje_negativas


def obtener_reseña(reseñas, indice):
    """Devuelve una reseña por su índice, comenzando desde cero."""
    try:
        if indice < 0:
            raise IndexError("El indice no puede ser negativo.")

        return reseñas[indice]

    except IndexError as error:
        print(f"Error: no se pudo seleccionar la reseña. {error}")
        return None
