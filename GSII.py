import tkinter

ventana = tkinter.Tk()
ventana.geometry("600x800")
ventana.title ("TP Final")

etiqueta = tkinter.Label(ventana, text = "Este es el TP para Gestión de Software II", bg = "Cyan")
etiqueta.pack(fill = tkinter.X)

etiqueta2 = tkinter.Label(ventana, text = "Hecho por Lautaro Boasso", bg = "Orange")
etiqueta2.pack(side = tkinter.BOTTOM)

ventana.mainloop()