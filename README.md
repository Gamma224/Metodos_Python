# Metodos_Python

# Proyecto de Cálculo de Funciones Matemáticas en Python

Repositorio del proyecto desarrollado para el curso [nombre del curso].

## Descripción

Este proyecto implementa una aplicación matemática en Python que calcula funciones trigonométricas e hiperbólicas utilizando exclusivamente estructuras básicas de programación, sin funciones nativas. Los cálculos se realizan mediante series de Taylor y el proyecto está organizado bajo el patrón Modelo-Vista-Controlador (MVC).

Se ofrecen tres interfaces de usuario:
- Terminal (CLI)
- Interfaz gráfica (Tkinter)
- Aplicación web (Flask)

## Funcionalidades

- Cálculo de exponencial \( e^x \)
- Cálculo de seno \( \sin(x) \)
- Cálculo de coseno \( \cos(x) \)
- Cálculo de arcoseno \( \arcsin(x) \)
- Cálculo de arcocoseno \( \arccos(x) \)
- Cálculo de seno hiperbólico \( \sinh(x) \)
- Cálculo de coseno hiperbólico \( \cosh(x) \)

## Estructura del proyecto

Metodos_Python/ 

│ 

├── app/ 

│   ├── controllers/ 

│   │   └── matematicas_controller.py   # Coordina entre vista y modelo 

│   │ 

│   ├── models/ 

│   │   └── matematicas_model.py        # Contiene las funciones matemáticas 

│   │ 

│   ├── views/ 

│   │   ├── matematicas_view.py         # Interfaz en terminal (texto) 

│   │   └── templates/ 

│   │       └── index.html              # Interfaz web HTML 

│   │ 

├── metodos.py                          # Punto de entrada para la app web (Flask) 

├── main.py                             # Punto de entrada para modo consola 

├── requirements.txt                    # Dependencias del proyecto 

└── docs/ 

    └── informe  


## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Gamma224/Metodos_Python.git
cd Metodos_Python

pip install -r requirements.txt

Para ejecutar en terminal:

python main.py

Luego abre http://127.0.0.1:5000 en tu navegador.