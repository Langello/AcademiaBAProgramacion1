import tkinter as tk

root = tk.Tk()
root.title("Whatsapp")
root.iconbitmap("AcademiaBAProgramacion1/extras/Whatsapp.ico")
root.geometry("400x400")
root.resizable(0,0)
root.config(bg="#50b354", relief="groove", bd=5)
Label1 = tk.Label(root, text="Escribe tu mensaje")
Label1.config(bg="#50b354",fg="#ffffff",font=("Arial", 25, "bold"),padx=20,pady=20)
Label1.pack()
Entry1=tk.Entry(root)
Entry1.config(fg="Green", font=("Arial",15),insertbackground="green",justify="center")
Entry1.pack()
root.mainloop()