import tkinter  # librería que te permite crear ventanas y hacer una interfaz similar a la que se usa windows

ventana = tkinter.Tk()
ventana.title("Mi primer ventana")
ventana.iconbitmap("extras/danza.ico")
ventana.geometry("600x400")
ventana.resizable(0,0)
ventana.config(bg="lightblue", bd=10, relief="sunken")

ventana.mainloop()
