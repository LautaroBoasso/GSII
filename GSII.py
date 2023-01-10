import tkinter

ventana = tkinter.Tk()
ventana.geometry("600x800")
ventana.title ("TP Final")

etiqueta = tkinter.Label(ventana, text = "Este es el TP para Gestión de Software II", bg = "Cyan")
etiqueta.pack(fill = tkinter.X)

etiqueta2 = tkinter.Label(ventana, text = "Hecho por Lautaro Boasso", bg = "Orange")
etiqueta2.pack(side = tkinter.BOTTOM)

boton1 = tkinter.Button(ventana, padx= 4, pady= 5, text = "Ver Base de Datos",command = lambda: print ("Prueba"))
boton1.pack()

boton2 = tkinter.Button(ventana, padx= 3, pady= 4, text = "Agregar un nuevo registro",command = lambda: print ("Prueba"))
boton2.pack()

boton3 = tkinter.Button(ventana, padx= 3, pady= 4, text = "Modificar un Registro",command = lambda: print ("Prueba"))
boton3.pack()

ventana.mainloop()