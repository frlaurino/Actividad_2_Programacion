def validar_titulo(titulo):
    """Valida que el titulo no este vacio, tenga al menos 2 caracteres y sea alfanumerico."""
    titulo_limpio = titulo.strip()
    sin_espacios = titulo_limpio.replace(" ", "")
    valido = False
    if len(titulo_limpio) >= 2 and sin_espacios.isalnum():
        valido = True
    return valido


def validar_texto_resena(texto):
    """Valida que la reseña no este vacia, supere la longitud minima y contenga letras."""
    texto_limpio = texto.strip()
    tiene_letras = False
    for caracter in texto_limpio:
        if caracter.isalpha():
            tiene_letras = True

    valido = False
    if len(texto_limpio) >= 10 and tiene_letras:
        valido = True
    return valido


def validar_texto_no_vacio(texto):
    """Verifica que una cadena no quede vacia luego de quitar espacios en los extremos."""
    texto_limpio = texto.strip()
    return len(texto_limpio) > 0


def ingresar_titulo(mensaje):
    """Solicita el titulo de la obra hasta que cumpla con la validacion."""
    titulo = input(mensaje).strip()
    while not validar_titulo(titulo):
        print("Error: El titulo debe tener al menos 2 caracteres y contener solo letras o numeros.")
        titulo = input(mensaje).strip()
    return titulo


def ingresar_texto_resena(mensaje):
    """Solicita el texto de la reseña hasta que cumpla con la longitud y contenido."""
    texto = input(mensaje).strip()
    while not validar_texto_resena(texto):
        print("Error: La reseña no puede estar vacia, debe tener al menos 10 caracteres y contener letras.")
        texto = input(mensaje).strip()
    return texto


def ingresar_entero(mensaje):
    """Solicita un numero entero manejando errores de conversion con try-except."""
    valido = False
    while not valido:
        try:
            numero = int(input(mensaje))
            valido = True
        except ValueError as err:
            print("Error:", err)
            print("Debe ingresar un numero entero valido.")
    return numero


def ingresar_flotante(mensaje):
    """Solicita un numero decimal manejando errores de conversion con try-except."""
    valido = False
    while not valido:
        try:
            numero = float(input(mensaje))
            valido = True
        except ValueError as err:
            print("Error:", err)
            print("Debe ingresar un numero valido.")
    return numero


def ingresar_puntuacion(mensaje):
    """Solicita una puntuacion entera entre 1 y 10 usando try-except y raise."""
    valido = False
    while not valido:
        try:
            nota = int(input(mensaje))
            if nota < 1 or nota > 10:
                raise ValueError("La nota debe ser entre 1 y 10")
            valido = True
        except ValueError as err:
            print("Error:", err)
    return nota


def agregar_resena(resenas):
    """Solicita y valida los datos de una nueva reseña y la agrega a la matriz."""
    print("\n--- AGREGAR NUEVA RESEÑA ---")
    if len(resenas) > 0:
        nuevo_id = resenas[len(resenas) - 1][0] + 1
    else:
        nuevo_id = 1

    titulo = ingresar_titulo("Ingrese el titulo de la pelicula o serie: ")
    texto = ingresar_texto_resena("Ingrese el texto de la reseña (minimo 10 caracteres): ")
    puntuacion = ingresar_puntuacion("Ingrese la puntuacion (1 a 10): ")

    nueva_resena = [nuevo_id, titulo, texto, puntuacion]
    resenas.append(nueva_resena)
    print("Reseña cargada con exito. ID asignado:", nuevo_id)
    return nueva_resena
