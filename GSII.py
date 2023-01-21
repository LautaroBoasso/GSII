from tkinter import *
import mariadb

# Funciones

def abrir_bdd():
    ventana_verbdd = Toplevel()
    ventana_verbdd.title ("Base de Datos")
    ventana_verbdd.geometry ("800x800")
    boton_cerrar = Button(ventana_verbdd, text = "Cerrar", command=ventana_verbdd.destroy)
    boton_cerrar.pack(side = BOTTOM)

# Ventana principal

ventana_principal = Tk()
ventana_principal.geometry("600x800")
ventana_principal.title ("TP Final")


# Base de Datos

try:
    conexion = mariadb.connect(
        user= "root",
        password="",
        host="127.0.0.1",
        port= 3306,
        database = "mundial"
    )
    Label(ventana_principal, text = "Se conecto a la Base de Datos correctamente: " +  conexion.database + ".").pack(side = BOTTOM)

except mariadb.Error as error:
    print (f"Error al conectarse a la Base de Datos  {error}")



# Interfaz gráfica

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

boton4 = Button(ventana_principal, padx= 3, pady= 4, text = "Eliminar un Registro",command = lambda: print ("Prueba"))
boton4.pack()

mainloop()