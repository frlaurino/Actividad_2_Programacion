from validaciones import validar_texto_no_vacio
from procesamiento import normalizar_texto
from procesamiento import formatear_titulo
from procesamiento import censurar_texto
from procesamiento import reemplazar_termino
from procesamiento import invertir_texto
from procesamiento import extraer_remate
from procesamiento import resumir_texto
from procesamiento import cifrar_cesar
from procesamiento import descifrar_cesar
from reportes import mostrar_reporte_reseña
from reportes import mostrar_reporte_termino


def mostrar_menu():
    """Muestra en pantalla las opciones del sistema."""
    print()
    print("=" * 40)
    print(f"{'SISTEMA DE RESEÑAS':^40}")
    print("=" * 40)
    print("1. Ver reseñas")
    print("2. Agregar reseña")
    print("3. Analizar texto de una reseña")
    print("4. Normalizar, censurar y transformar")
    print("5. Cifrar reseña (ord / chr)")
    print("6. Reporte estadístico")
    print("7. Salir")
    print("=" * 40)


def ingresar_entero_rango(mensaje, minimo, maximo):
    """Pide un entero entre minimo y maximo; maneja ValueError y usa raise si queda fuera de rango."""
    valido = False
    while not valido:
        try:
            numero = int(input(mensaje))
            if numero < minimo or numero > maximo:
                raise ValueError(f"El valor debe estar entre {minimo} y {maximo}.")
            valido = True
        except ValueError as error:
            print("ERROR:", error)
    return numero


def pedir_opcion(minimo, maximo):
    """Muestra el menú y devuelve una opción válida entre minimo y maximo."""
    mostrar_menu()
    opcion = ingresar_entero_rango("Seleccione una opción: ", minimo, maximo)
    return opcion


def seleccionar_reseña(reseñas):
    """Pide el número de reseña (desde 1) y la devuelve. Usa múltiples except (ValueError e IndexError)."""
    valido = False
    while not valido:
        try:
            numero = int(input(f"Ingrese el número de reseña (1 a {len(reseñas)}): "))
            if numero <= 0:
                raise IndexError("El número de reseña debe ser mayor que cero.")
            reseña = reseñas[numero - 1]
            valido = True
        except ValueError as error:
            print("ERROR. Debe ingresar un número entero.")
            print("Detalle:", error)
        except IndexError as error:
            print("ERROR. No existe una reseña con ese número.")
            print("Detalle:", error)
    return reseña


def ingresar_texto(mensaje):
    """Pide un texto hasta que no quede vacío y lo devuelve sin espacios en los extremos."""
    texto = input(mensaje)
    while not validar_texto_no_vacio(texto):
        print("ERROR. El texto no puede estar vacío.")
        texto = input(mensaje)
    return texto.strip()


def mostrar_reseñas(reseñas):
    """Muestra todas las reseñas en una tabla alineada con f-strings."""
    print()
    print(f"{'ID':<5}{'Título':<26}{'Nota':>5}   {'Reseña'}")
    print("-" * 80)
    for reseña in reseñas:
        titulo_corto = resumir_texto(reseña[1], 22)
        texto_corto = resumir_texto(reseña[2], 40)
        print(f"{reseña[0]:<5}{titulo_corto:<26}{reseña[3]:>5}   {texto_corto}")
    print("-" * 80)
    print(f"Total de reseñas: {len(reseñas)}")


def opcion_analizar(reseñas):
    """Analiza una reseña: datos, longitud, palabras, apariciones y pertenencia de un término."""
    reseña = seleccionar_reseña(reseñas)
    mostrar_reporte_reseña(reseña)
    termino = ingresar_texto("Ingrese una palabra o expresión a buscar: ")
    mostrar_reporte_termino(reseña[2], termino)


def armar_lista_prohibidas(texto):
    """Recibe palabras separadas por coma y devuelve una lista limpia y en minúscula."""
    prohibidas = []
    for palabra in texto.split(","):
        palabra = palabra.strip().lower()
        if palabra != "":
            prohibidas.append(palabra)
    return prohibidas


def opcion_transformar(reseñas):
    """Normaliza, censura, reemplaza, invierte y extrae partes del texto de una reseña."""
    reseña = seleccionar_reseña(reseñas)
    texto = reseña[2]

    print()
    print("Texto original:")
    print(texto)

    print()
    print("Texto normalizado:")
    print(normalizar_texto(texto))
    print("Título formateado:")
    print(formatear_titulo(reseña[1]))

    print()
    palabras = ingresar_texto("Palabras a censurar (separadas por coma): ")
    prohibidas = armar_lista_prohibidas(palabras)
    print("Texto censurado:")
    print(censurar_texto(texto, prohibidas))

    print()
    buscado = ingresar_texto("Término a reemplazar: ")
    nuevo = ingresar_texto("Nuevo término: ")
    if buscado in texto:
        print("Texto con reemplazo:")
        print(reemplazar_termino(texto, buscado, nuevo))
    else:
        print(f'El término "{buscado}" no aparece en la reseña.')

    print()
    print("Texto invertido:")
    print(invertir_texto(texto))

    cantidad = ingresar_entero_rango(f"¿Cuántos caracteres finales desea ver? (1 a {len(texto)}): ", 1, len(texto))
    print("Remate de la reseña:")
    print(extraer_remate(texto, cantidad))


def opcion_cifrar(reseñas):
    """Cifra el texto de una reseña con ord() y chr() y luego lo descifra para comprobarlo."""
    reseña = seleccionar_reseña(reseñas)
    desplazamiento = ingresar_entero_rango("Ingrese el desplazamiento (1 a 25): ", 1, 25)
    cifrado = cifrar_cesar(reseña[2], desplazamiento)
    descifrado = descifrar_cesar(cifrado, desplazamiento)
    print()
    print("Texto original:  ", reseña[2])
    print("Texto cifrado:   ", cifrado)
    print("Texto descifrado:", descifrado)
