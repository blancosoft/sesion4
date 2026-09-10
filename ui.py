import tkinter as tk
from tkinter import scrolledtext, messagebox
from modelo import predecir
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def mostrar_reglas_gui(reglas, arbol):
    ventana = tk.Tk()
    ventana.title("Sistema Experto Automático")

    etiqueta = tk.Label(ventana, text="📌 Base de Reglas generada automáticamente:", font=("Arial", 12, "bold"))
    etiqueta.pack(pady=10)

    # --- Reglas en texto ---
    cuadro = scrolledtext.ScrolledText(ventana, width=70, height=15, font=("Courier", 11))
    cuadro.pack(padx=10, pady=10)
    cuadro.insert(tk.END, reglas)
    cuadro.config(state="disabled")

    # --- Gráfico del árbol (más grande y legible) ---
    fig, ax = plt.subplots(figsize=(10,6))  # tamaño más grande
    plot_tree(
        arbol,
        feature_names=["Edad", "Horas_Online", "Compras_Previas"],
        class_names=["Ignora", "Clic"],
        filled=True,
        fontsize=10,   # fuente más grande
        ax=ax
    )
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

    # --- Sección de predicción ---
    frame_pred = tk.Frame(ventana)
    frame_pred.pack(pady=10)

    tk.Label(frame_pred, text="Edad:").grid(row=0, column=0, padx=5, pady=5)
    edad_entry = tk.Entry(frame_pred)
    edad_entry.grid(row=0, column=1)

    tk.Label(frame_pred, text="Horas Online:").grid(row=1, column=0, padx=5, pady=5)
    horas_entry = tk.Entry(frame_pred)
    horas_entry.grid(row=1, column=1)

    tk.Label(frame_pred, text="Compras Previas:").grid(row=2, column=0, padx=5, pady=5)
    compras_entry = tk.Entry(frame_pred)
    compras_entry.grid(row=2, column=1)

    def ejecutar_prediccion():
        try:
            edad = int(edad_entry.get())
            horas = int(horas_entry.get())
            compras = int(compras_entry.get())
            resultado = predecir(arbol, edad, horas, compras)
            if resultado == 1:
                mensaje = "✅ El cliente HARÍA clic en el anuncio."
            else:
                mensaje = "❌ El cliente IGNORARÍA el anuncio."
            messagebox.showinfo("Resultado de Predicción", mensaje)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

    boton_pred = tk.Button(ventana, text="Probar Predicción", command=ejecutar_prediccion)
    boton_pred.pack(pady=10)

    boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
    boton_cerrar.pack(pady=10)

    ventana.mainloop()
