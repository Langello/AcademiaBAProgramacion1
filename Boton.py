import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primer ventana")
ventana.geometry("600x400")
ventana.resizable(0,0)
ventana.config(bg="lightblue", bd=10, relief="sunken")


def clickBoton():
    label1= tk.Label(ventana,text='Hola mundo')
    label1.config(fg='red')
    label1.grid(row=1,column=1)


boton=tk.Button(ventana,text='Hola', command=clickBoton)
boton.grid(row=0, column=1)


ventana.mainloop()