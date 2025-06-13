from app.models.matematicas_model import MatematicasModel

class MatematicasController:
    """
    Controlador para operaciones matemáticas.

    Esta clase actúa como intermediario entre la vista y el modelo en el patrón MVC.
    """

    def __init__(self):
        """
        Inicializa el controlador con una instancia del modelo.
        """
        self.modelo = MatematicasModel()

    def obtener_base_menos_uno(self, numero):
        """
        Retorna 1 si el número es par, -1 si es impar.
        """
        return self.modelo.base_menos_uno(numero)

    def calcular(self, funcion, x):
        """
        Delegar operaciones a funciones matemáticas del modelo.
        """
        if funcion == "exp":
            return self.modelo.exp(x)
        elif funcion == "sin":
            return self.modelo.sin(x)
        elif funcion == "cos":
            return self.modelo.cos(x)
        elif funcion == "arcsin":
            return self.modelo.arcsin(x)
        elif funcion == "arccos":
            return self.modelo.arccos(x)
        elif funcion == "sinh":
            return self.modelo.sinh(x)
        elif funcion == "cosh":
            return self.modelo.cosh(x)
        else:
            return "Función no válida"
