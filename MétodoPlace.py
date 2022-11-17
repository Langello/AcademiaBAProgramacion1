import tkinter as tk

root=tk.Tk()
root.title("Método Place")
root.geometry("300x300")

LabelNombre=tk.Label(root, text="Ingrese nombre:")
LabelNombre.place(x=20, y=10)
EntryNombre = tk.Entry(root)
EntryNombre.place(x=120, y=10)
EntryNombre.config(font=("Arial",15),width=15,fg="black")
LabelApellido=tk.Label(root,text="Ingrese apellido:")
LabelApellido.place(x=20, y=45)
EntryApellido = tk.Entry(root)
EntryApellido.place(x=120, y=45)
EntryApellido.config(font=("Arial",15),width=15,fg="black")
root.mainloop()