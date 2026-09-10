from datos import cargar_datos
from modelo import entrenar_modelo, extraer_reglas
from ui import mostrar_reglas_gui

def main():
    X, Y = cargar_datos()
    arbol = entrenar_modelo(X, Y)
    nombres = ["Edad", "Horas_Online", "Compras_Previas"]
    reglas = extraer_reglas(arbol, nombres)
    mostrar_reglas_gui(reglas, arbol)

if __name__ == "__main__":
    main()
