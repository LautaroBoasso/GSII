from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mariadb

class Jugadores:
    #db_name='database_proyecto.db'
    
     def __init__(self, ventana_principal):
        self.window=ventana_principal 
        self.window.title("Aplicación CRUD para GSII")
        self.window.geometry("1000x400")
        self.window.resizable(0,0)
        
        # ETIQUETAS Y CAJAS DE TEXTO #

        label_Nombre=Label(ventana_principal, text="Nombre")
        label_Nombre.place(x=15,y=10)
        self.Nombre=Entry(root,width=20)
        self.Nombre.place(x=70,y=10)

        label_Apellidos=Label(ventana_principal, text="Apellidos")
        label_Apellidos.place(x=215,y=10)
        self.Apellidos=Entry(ventana_principal, width=30)
        self.Apellidos.place(x=270,y=10)

        label_Edad=Label(ventana_principal, text="Edad")
        label_Edad.place(x=466,y=10)
        self.Edad=Entry(ventana_principal, width=5)
        self.Edad.place(x=500,y=10)

        label_Dorsal=Label(ventana_principal, text="Dorsal")
        label_Dorsal.place(x=165,y=40)
        self.Dorsal=Entry(ventana_principal, width=5)
        self.Dorsal.place(x=205,y=40)

        label_Posicion=Label(ventana_principal, text="Posición")
        label_Posicion.place(x=325,y=40)
        self.Posicion=Entry(ventana_principal, width=25)
        self.Posicion.place(x=380,y=40)

        self.Buscador=Entry(ventana_principal, width=20)
        self.Buscador.place(x=640,y=90)

        self.ID=Entry(ventana_principal)
    
        # CRUD #
        
        def LimpiarCampos():
         self.Nombre.delete(0, END)
         self.Apellidos.delete(0, END)
         self.Edad.delete(0, END)
         self.Dorsal.delete(0, END)
         self.Posicion.delete(0, END)




        def Crear():
         cursor=conexion.cursor()

         try:
            datos=self.Nombre.get(),self.Apellidos.get(),self.Edad.get(),self.Dorsal.get(),self.Posicion.get()
            cursor.execute("INSERT INTO jugadores VALUES (NULL,?,?,?,?,?)", (datos))
            conexion.commit()

         except mariadb.Error as error_registro:
            print (f"Error al registrar los datos {error_registro}")
         pass
        LimpiarCampos()


        # BOTONES #

        boton_agregar=Button(ventana_principal, text="Agregar Registro",bg="lightgreen", command=Crear)
        boton_agregar.place(x=15, y=90)

        boton_modificar=Button(ventana_principal, text="Modificar Registro",bg="lightblue")
        boton_modificar.place(x=155, y=90)

        boton_mostrar=Button(ventana_principal, text="Mostrar Lista",bg="yellow")
        boton_mostrar.place(x=310, y=90)

        boton_eliminar=Button(ventana_principal, text="Eliminar Registro",bg="red")
        boton_eliminar.place(x=435, y=90)

        boton_buscar=Button(ventana_principal, text="Buscar")
        boton_buscar.place(x=770, y=87)

        # TABLA #

        self.tree=ttk.Treeview(height=10, columns=('#0', '#1', '#2', '#3', '#4'))
        self.tree.place(x= 15, y= 130)
        self.tree.column('#0', width=50)
        self.tree.heading('#0', text="ID", anchor=CENTER)
        self.tree.heading('#1', text="Nombre", anchor=CENTER)
        self.tree.heading('#2', text="Apellidos", anchor=CENTER)
        self.tree.heading('#3', text="Edad", anchor=CENTER)
        self.tree.column('#3', width=50)
        self.tree.heading('#4', text="Dorsal", anchor=CENTER)
        self.tree.column('#4', width=50)
        self.tree.heading('#5', text="Posición", anchor=CENTER)



if __name__ == '__main__':
    root=Tk()
    aplicacion=Jugadores(root)

# Base de Datos

try:
    conexion = mariadb.connect(
    user= "root",
    password="",
    host="127.0.0.1",
    port= 3307,
    database = "mundial"
    )
    Label(root, text = "Se conecto a la Base de Datos correctamente: " +  conexion.database + ".").pack(side = BOTTOM)

except mariadb.Error as error:
    print (f"Error al conectarse a la Base de Datos:  {error}")



root.mainloop()