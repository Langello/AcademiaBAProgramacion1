import tkinter as tk
def permiso():
    if (int(entryEdad.get()) >=18):
        mensaje='Puede pasar      '
    else:
        mensaje='No puede pasar'
    label1=tk.Label(ventana,text=mensaje)
    label1.grid(row=1, column=1)


ventana = tk.Tk()
ventana.title('Admisión')
ventana.geometry("500x100")


labelEdad= tk.Label(ventana, text='Ingrese su edad: ')
labelEdad.config(fg='gray', font=('cambria',12))
labelEdad.grid(row=0, column=0, pady=10, padx=50)

entryEdad=tk.Entry(ventana)
entryEdad.grid(row=0 , column=1, padx=50, pady=10)

boton=tk.Button(ventana, text='Ingresar',command=permiso)
boton.config(bg='skyblue',fg='blue', padx=20, pady=10)
boton.grid(row=1, column=0)

ventana.mainloop()

