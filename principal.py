from datos import reseñas
from validaciones import agregar_reseña
from reportes import mostrar_reporte_general
from menu import pedir_opcion
from menu import mostrar_reseñas
from menu import opcion_analizar
from menu import opcion_transformar
from menu import opcion_cifrar


def main():
    """Inicia el sistema y coordina las opciones del menú hasta que el usuario elige salir."""
    opcion = 0
    while opcion != 7:
        opcion = pedir_opcion(1, 7)
        if opcion == 1:
            mostrar_reseñas(reseñas)
        elif opcion == 2:
            agregar_reseña(reseñas)
        elif opcion == 3:
            opcion_analizar(reseñas)
        elif opcion == 4:
            opcion_transformar(reseñas)
        elif opcion == 5:
            opcion_cifrar(reseñas)
        elif opcion == 6:
            mostrar_reporte_general(reseñas)
    print("Gracias por utilizar el sistema. ¡Hasta luego!")


# Programa principal
main()
