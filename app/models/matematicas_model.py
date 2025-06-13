"""constante pi"""
PI = 3.14

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
    
    def factorial(self, n):
        """Calcula el factorial de n de forma iterativa."""
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def power(self, x, n):
        """Calcula x elevado a la n (x^n), sin usar funciones nativas."""
        result = 1
        for _ in range(n):
            result *= x
        return result

    def exp(self, x, terms=20):
        """Calcula e^x mediante la serie de Taylor."""
        result = 0
        for n in range(terms):
            result += self.power(x, n) / self.factorial(n)
        return result

    def sin(self, x, terms=20):
        """Calcula sin(x) mediante la serie de Taylor."""
        result = 0
        for n in range(terms):
            sign = 1 if n % 2 == 0 else -1
            result += sign * self.power(x, 2 * n + 1) / self.factorial(2 * n + 1)
        return result

    def cos(self, x, terms=20):
        """Calcula cos(x) mediante la serie de Taylor."""
        result = 0
        for n in range(terms):
            sign = 1 if n % 2 == 0 else -1
            result += sign * self.power(x, 2 * n) / self.factorial(2 * n)
        return result

    def arcsin(self, x, terms=20):
        """Calcula arcsin(x) usando la serie de Taylor."""
        result = 0
        for n in range(terms):
            num = self.factorial(2 * n)
            den = self.power(4, n) * (self.factorial(n) ** 2) * (2 * n + 1)
            result += (num / den) * self.power(x, 2 * n + 1)
        return result

    def arccos(self, x, terms=20):
        """
        Calcula arccos(x) como:
        arccos(x) = pi/2 - arcsin(x)
        """
        return (PI / 2) - self.arcsin(x, terms)

    def sinh(self, x, terms=20):
        """Calcula sinh(x) mediante la serie de Taylor."""
        result = 0
        for n in range(terms):
            result += self.power(x, 2 * n + 1) / self.factorial(2 * n + 1)
        return result

    def cosh(self, x, terms=20):
        """Calcula cosh(x) mediante la serie de Taylor."""
        result = 0
        for n in range(terms):
            result += self.power(x, 2 * n) / self.factorial(2 * n)
        return result