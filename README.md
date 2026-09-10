# Sistema Experto Automatico

Proyecto del taller de Sistemas Expertos e Inteligencia Artificial. El programa simula un departamento de marketing que predice si un cliente hara clic en un anuncio usando un arbol de decision.

## Requisitos

- Python 3.10 o superior
- NumPy
- scikit-learn
- Matplotlib
- Tkinter, incluido normalmente en Python para Windows

## Instalacion

Desde la carpeta del proyecto, crea y activa un entorno virtual:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```powershell
python -m pip install numpy scikit-learn matplotlib
```

Si PowerShell bloquea la activacion, ejecuta la aplicacion directamente con el interprete del entorno virtual.

## Ejecucion

### Desde PowerShell

```powershell
.\.venv\Scripts\python.exe main.py
```

### Desde Windows

Haga doble clic en `Ejecutar app.bat`. El lanzador utiliza el entorno virtual `.venv` y abre directamente la ventana grafica del sistema experto.

Al iniciar, el programa:

1. Carga el dataset simulado de marketing.
2. Entrena un `DecisionTreeClassifier`.
3. Genera las reglas con `export_text`.
4. Abre una ventana con las reglas y el grafico del arbol.
5. Permite probar predicciones ingresando edad, horas en linea y compras previas.

## Dataset

El conjunto de datos contiene 10 clientes y tres variables numericas:

- `Edad`
- `Horas_Online`
- `Compras_Previas`

La etiqueta `Y` representa el comportamiento del cliente:

- `1`: hizo clic en el anuncio.
- `0`: ignoro el anuncio.

## Archivos principales

- `datos.py`: crea y devuelve los arreglos `X` e `Y`.
- `modelo.py`: entrena el arbol, extrae las reglas y realiza predicciones.
- `ui.py`: construye la interfaz grafica, muestra las reglas y dibuja el arbol.
- `main.py`: coordina la carga de datos, el entrenamiento y la interfaz.

## Interpretacion

Las reglas generadas por el arbol tienen forma IF-THEN. Por ejemplo, una condicion sobre las horas en linea puede dividir a los clientes en grupos con mayor o menor probabilidad de hacer clic. Estas reglas forman una base de conocimiento interpretable para apoyar decisiones de marketing.

El modelo aprende patrones a partir de los datos simulados. Por eso, sus conclusiones dependen de la calidad y cantidad de ejemplos disponibles y deben validarse con datos reales antes de usarse en una campaña.
