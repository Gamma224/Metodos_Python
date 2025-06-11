from app.models.matematicas_model import MatematicasModel  # Importa el modelo matemático para usar su lógica

class MatematicasController:
    """
    Controlador para operaciones matemáticas.

    Esta clase actúa como intermediario entre la vista y el modelo en el patrón MVC.
    Su función principal es recibir solicitudes de la vista, procesarlas si es necesario,
    y delegar la lógica de negocio al modelo correspondiente.
    """

    def __init__(self):
        """
        Inicializa el controlador creando una instancia del modelo MatematicasModel.
        Esto permite que el controlador tenga acceso a los métodos y atributos del modelo.
        """
        self.modelo = MatematicasModel()  # Instancia del modelo matemático

    def obtener_base_menos_uno(self, numero):
        """
        Llama al modelo para obtener 1 o -1 según si el número es par o impar.

        Parámetros:
            numero (int): Número a evaluar.

        Retorna:
            int: 1 si el número es par, -1 si es impar.

        Este método actúa como una capa de abstracción entre la vista y el modelo,
        permitiendo que la vista no interactúe directamente con la lógica de negocio.
        """
        return self.modelo.base_menos_uno(numero)  # Llama al método del modelo y retorna el resultado