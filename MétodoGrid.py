import tkinter as tk
root = tk.Tk()
root.title("Método Grid")
root.geometry("300x300")

LabelNombre= tk.Label(root, text="Nombre :")
LabelNombre.grid(row=0,column=0, padx=30, pady=5)
EntryNombre=tk.Entry(root)
EntryNombre.grid(row=0, column=1, padx=30,pady=5)

root.mainloop()