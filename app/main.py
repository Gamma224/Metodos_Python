from controllers.matematicas_controller import MatematicasController
from views.matematicas_view import MatematicasView

def main():
    """
    Función principal del programa.

    Este script implementa un flujo básico utilizando el patrón de arquitectura MVC (Modelo-Vista-Controlador)
    para demostrar el uso de la función `base_menos_uno`, que retorna 1 si un número es par y -1 si es impar.

    Flujo del programa:
    1. Se crea una instancia del controlador `MatematicasController`, que se encarga de la lógica de negocio y 
       la comunicación con el modelo de matemáticas.
    2. Se crea una instancia de la vista `MatematicasView`, responsable de mostrar los resultados al usuario.
    3. Se define una lista de números de ejemplo para probar la función.
    4. Para cada número en la lista:
        a. El controlador llama al modelo para calcular si el número es par o impar usando la base -1.
        b. La vista muestra el resultado en consola de forma legible para el usuario.

    Este ejemplo ilustra cómo separar la lógica de negocio (controlador/modelo) de la presentación (vista)
    siguiendo buenas prácticas de diseño de software.
    """
    controller = MatematicasController()
    view = MatematicasView()

    numeros = [2, 3, 0, -4, -5]  # Lista de números a evaluar
    for numero in numeros:
        resultado = controller.obtener_base_menos_uno(numero)
        view.mostrar_resultado(numero, resultado)

if __name__ == "__main__":
    main()