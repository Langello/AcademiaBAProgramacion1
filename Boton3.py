import tkinter as tk


def funcionCalcular():
    if (int(entrySueldo.get()) >= 300000):
        neto = int(entrySueldo.get())-int(entrySueldo.get())*0.10
        texto = tk.Label(ventana, text=entryNombre.get() +' Tu sueldo neto es' + str(neto))
        texto.grid(row=0, column=3)
    else:
        texto = tk.Label(ventana, text=entryNombre.get() +' Tu sueldo es libre de impuestos')
        texto.grid(row=0, column=3)


ventana = tk.Tk()
ventana.title('Calculo de ganancias')
ventana.geometry("500x200")


labelNombre = tk.Label(ventana, text='Ingrese nombre')
labelNombre.grid(row=0, column=0, padx=10, pady=10)
entryNombre = tk.Entry(ventana)
entryNombre.grid(row=0, column=1, padx=10, pady=10)

labelSueldo = tk.Label(ventana, text='Ingrese su sueldo')
labelSueldo.grid(row=1, column=0, padx=10, pady=10)
entrySueldo = tk.Entry(ventana)
entrySueldo.grid(row=1, column=1, padx=10, pady=10)

boton = tk.Button(ventana, text='Calcular', command=funcionCalcular)
boton.grid(row=2, column=0, padx=10, pady=10)


ventana.mainloop()
