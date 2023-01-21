from tkinter import *

ventana_principal = Tk()
ventana_principal.geometry("600x800")
ventana_principal.title ("TP Final")

def abrir_bdd():
    ventana_verbdd = Toplevel()
    ventana_verbdd.title ("Base de Datos")
    ventana_verbdd.geometry ("800x800")
    boton_cerrar = Button(ventana_verbdd, text = "Cerrar", command=ventana_verbdd.destroy)
    boton_cerrar.pack(side = BOTTOM)

etiqueta = Label(ventana_principal, text = "Este es el TP para Gestión de Software II", bg = "Cyan")
etiqueta.pack(fill = X)

etiqueta2 = Label(ventana_principal, text = "Hecho por Lautaro Boasso", bg = "Orange")
etiqueta2.pack(side = BOTTOM)

boton1 = Button(ventana_principal, padx= 4, pady= 5, text = "Ver Base de Datos", command= abrir_bdd)
boton1.pack()



boton2 = Button(ventana_principal, padx= 3, pady= 4, text = "Agregar un nuevo registro",command = lambda: print ("Prueba"))
boton2.pack()

boton3 = Button(ventana_principal, padx= 3, pady= 4, text = "Modificar un Registro",command = lambda: print ("Prueba"))
boton3.pack()


mainloop()