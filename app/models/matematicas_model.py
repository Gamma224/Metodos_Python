class MatematicasModel:
    """
    Modelo para operaciones matemáticas básicas.
    """

    def __init__(self, valor_inicial=0):
        """
        Inicializa el modelo con un valor inicial.
        :param valor_inicial: int o float, valor inicial para las operaciones.
        """
        self.valor = valor_inicial


    def base_menos_uno(self, numero):
        """
        Retorna 1 si el número es par, -1 si es impar, usando la base -1.
        :param numero: int, número a evaluar.
        :return: int, 1 para par, -1 para impar.
        """
        return 1 if numero % 2 == 0 else -1