from flask import Flask, render_template, request
from app.controllers.matematicas_controller import MatematicasController

"""Flujo principal del aplicativo.

    Este codigo tiene como fin seguir un flujo básico utilizando el Modelo-Vista-Controlador
    con el se puede evidenciar el uso de la función "base_menos_uno", que retorna 1 si un número es par y -1 si es impar ademas de las nuevas
    funciones que se implementaron.

    Flujo del programa:
    1. Al llamar el programa main.py se inicia un servidor web local
    2. Se crea una instancia del controlador `MatematicasController`, que es donde previamente se definieron los modelos matematicos comentados 
    en el proyecto.
    3. Se carga la interfaz html para el usuario y Se crea una vista `MatematicasView`, responsable de mostrar los resultados en el html index.
    4. Impresion del calculo
    """

app = Flask(__name__)
controller = MatematicasController()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    funcion = request.form['funcion']
    x = request.form['x']
    try:
        x = float(x)
        resultado = controller.calcular(funcion, x)
    except ValueError:
        resultado = "Error: Ingresa un número válido"
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)

