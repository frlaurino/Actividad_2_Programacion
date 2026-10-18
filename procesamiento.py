SIGNOS = ".,;:!?¡¿\"'()-"


def limpiar_extremos(texto, lado):
    """Quita espacios de un lado del texto: 'izquierda', 'derecha' o 'ambos'."""
    if lado == "izquierda":
        resultado = texto.lstrip()
    elif lado == "derecha":
        resultado = texto.rstrip()
    else:
        resultado = texto.strip()
    return resultado


def normalizar_texto(texto):
    """Quita espacios sobrantes (extremos y dobles del medio) y pasa a minuscula."""
    palabras = texto.strip().split()
    return " ".join(palabras).lower()


def formatear_titulo(texto):
    """Normaliza el texto y deja cada palabra con la primera letra en mayuscula."""
    return normalizar_texto(texto).title()


def buscar_palabra(lista, palabra):
    """Busqueda secuencial con bandera: devuelve la posicion o -1 si no esta."""
    posicion = -1
    encontrado = False
    i = 0
    while i < len(lista) and not encontrado:
        if lista[i] == palabra:
            posicion = i
            encontrado = True
        i += 1
    return posicion


def censurar_texto(texto, palabras_prohibidas):
    """Reemplaza cada palabra prohibida por asteriscos, respetando los signos pegados."""
    resultado = []
    for palabra in texto.split():
        sin_izq = palabra.lstrip(SIGNOS)
        inicio = palabra[:len(palabra) - len(sin_izq)]
        nucleo = sin_izq.rstrip(SIGNOS)
        final = sin_izq[len(nucleo):]

        if nucleo != "" and buscar_palabra(palabras_prohibidas, nucleo.lower()) != -1:
            nucleo = "*" * len(nucleo)
        resultado.append(inicio + nucleo + final)
    return " ".join(resultado)


def reemplazar_termino(texto, buscado, nuevo):
    """Cambia todas las apariciones de 'buscado' por 'nuevo'."""
    return texto.replace(buscado, nuevo)


def invertir_texto(texto):
    """Devuelve el texto al reves usando slicing con paso negativo."""
    return texto[::-1]


def extraer_remate(texto, cantidad):
    """Devuelve los ultimos 'cantidad' caracteres del texto."""
    if cantidad <= 0:
        return ""
    return texto[-cantidad:]


def resumir_texto(texto, largo):
    """Devuelve los primeros 'largo' caracteres y agrega '...' si se corto."""
    if len(texto) <= largo:
        return texto
    return texto[:largo] + "..."


def cifrar_cesar(texto, desplazamiento):
    """Cifra el texto desplazando cada letra (A-Z / a-z); lo demas queda igual."""
    resultado = ""
    for caracter in texto:
        codigo = ord(caracter)
        if codigo >= ord("a") and codigo <= ord("z"):
            base = ord("a")
            resultado += chr((codigo - base + desplazamiento) % 26 + base)
        elif codigo >= ord("A") and codigo <= ord("Z"):
            base = ord("A")
            resultado += chr((codigo - base + desplazamiento) % 26 + base)
        else:
            resultado += caracter
    return resultado


def descifrar_cesar(texto, desplazamiento):
    """Deshace el cifrado: es cifrar con el desplazamiento opuesto."""
    return cifrar_cesar(texto, -desplazamiento)