from app.controllers.matematicas_controller import MatematicasController
from app.views.matematicas_view import MatematicasView

def main():
    """
    Flujo principal del aplicativo.

    Este codigo tiene como fin seguir un flujo básico utilizando el Modelo-Vista-Controlador
    con el se puede evidenciar el uso de la función "base_menos_uno", que retorna 1 si un número es par y -1 si es impar.

    Flujo del programa:
    1. Se crea una instancia del controlador `MatematicasController`, que es donde previamente se definieron los modelos matematicos.
    2. Se crea una vista `MatematicasView`, responsable de mostrar los resultados en el html index.
    3. Se define una lista de números de ejemplo para probar la función.
    4. Para cada número en la lista: El controlador llama al modelo para calcular si el número es par o impar usando la base 
      La vista muestra el resultado en consola de forma legible para el usuario.

    """
    controller = MatematicasController()
    view = MatematicasView()

    numeros = [2, 3, 0, -4, -5]  # Lista de números a evaluar
    for numero in numeros:
        resultado = controller.obtener_base_menos_uno(numero)
        view.mostrar_resultado(numero, resultado)

if __name__ == "__main__":
    main()