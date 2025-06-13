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

import tkinter as tk
from tkinter import ttk, messagebox

class MatematicasView(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Calculadora Matemática MVC")

        self.label_funcion = tk.Label(self, text="Función:")
        self.label_funcion.grid(row=0, column=0, padx=5, pady=5)



        self.funcion_var = tk.StringVar(value="exp")
        self.combo_funcion = ttk.Combobox(self, textvariable=self.funcion_var)
        self.combo_funcion['values'] = ("exp",)  # Agrega más funciones si implementas
        self.combo_funcion.grid(row=0, column=1, padx=5, pady=5)

        self.label_x = tk.Label(self, text="Valor de x:")
        self.label_x.grid(row=1, column=0, padx=5, pady=5)

        self.entry_x = tk.Entry(self)
        self.entry_x.grid(row=1, column=1, padx=5, pady=5)

        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.grid(row=2, column=0, columnspan=2, pady=10)

        self.label_resultado = tk.Label(self, text="Resultado:")
        self.label_resultado.grid(row=3, column=0, columnspan=2, pady=5)

    def calcular(self):
        funcion = self.funcion_var.get()
        try:
            x = float(self.entry_x.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un número válido")
            return
        resultado = self.controlador.calcular(funcion, x)
        self.label_resultado.config(text=f"Resultado: {resultado}")


import tkinter as tk
from tkinter import ttk, messagebox

# --- Modelo ---
class MatematicasModel:
    def factorial(self, n):
        resultado = 1
        i = 1
        while i <= n:
            resultado = resultado * i
            i = i + 1
        return resultado

    def potencia(self, x, n):
        resultado = 1
        i = 0
        while i < n:
            resultado = resultado * x
            i = i + 1
        return resultado

    def exp(self, x, terminos=10):
        resultado = 0
        n = 0
        while n < terminos:
            numerador = self.potencia(x, n)
            denominador = self.factorial(n)
            resultado = resultado + (numerador / denominador)
            n = n + 1
        return resultado
