#Equipo 2:
#Ernesto Vladimir Chaho Reynoso
#Alan Ponce Castillejos

import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

def process_csv(file_path, chunk_size= 5):
    try:
        df = pd.read_csv(file_path)
        data_list = df.to_dict(orient='records')
        
        with open('output.csv', 'w', newline='') as output_file:
            for i in range(0, len(data_list), chunk_size):
                chunk = data_list[i:i+chunk_size]
                chunk_df = pd.DataFrame(chunk)
                chunk_df.to_csv(output_file, index=False, header=(i == 0))

        messagebox.showinfo("Proceso Completado", "Los datos se han procesado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error al procesar el archivo: {str(e)}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        process_csv(file_path)

# Crear la ventana principal
window = tk.Tk()
window.title("Procesador de Archivos CSV")

# Crear y posicionar widgets
label = tk.Label(window, text="Selecciona un archivo CSV:")
label.pack(pady=10)

browse_button = tk.Button(window, text="Examinar", command=browse_file)
browse_button.pack(pady=10)

# Iniciar el bucle principal
window.mainloop()
