class MatematicasView:
    """
    Vista para operaciones matemáticas.

    Esta clase representa la capa de presentación en el patrón MVC (Modelo-Vista-Controlador).
    Su responsabilidad principal es mostrar información al usuario, en este caso, los resultados
    de las operaciones matemáticas realizadas por el modelo a través del controlador.

    Características:
    - No contiene lógica de negocio ni manipula datos directamente.
    - Solo se encarga de la presentación de los resultados.
    - Utiliza métodos estáticos ya que no requiere mantener estado interno.
    """

    @staticmethod
    def mostrar_resultado(numero, resultado):
        """
        Muestra en consola el resultado de la operación matemática para un número dado.

        Parámetros:
            numero (int): El número evaluado.
            resultado (int): El resultado de la operación (1 si es par, -1 si es impar).

        Este método imprime un mensaje formateado en la consola para que el usuario
        pueda ver claramente el resultado de la operación.
        """
        print(f"El resultado para el número {numero} es: {resultado}")