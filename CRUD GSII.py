from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mariadb

# Ventana principal e Interfaz Gráfica

root=Tk()
root.title("Aplicación CRUD para GSII")
root.geometry("600x350")

miID= StringVar()
miNombre= StringVar()
miApellidos= StringVar()
miEdad= StringVar()
miDorsal= StringVar()
miPosicion= StringVar()

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
    print (f"Error al conectarse a la Base de Datos  {error}")


def SalirAplicacion():
    valor=messagebox.askquestion("Salir","¿Cerrar aplicación?")
    if valor=="yes":
       root.destroy()


def LimpiarCampos():
    miID.set("")
    miNombre.set("")
    miApellidos.set("")
    miEdad.set("")
    miDorsal.set("")
    miPosicion.set("")

def Mensaje():
    acerca= """
    Aplicación CRUD
    Hecha por Lautaro Boasso para Gestión de Software II
    Con Python Tkinter
    """

# Desarrollo CRUD #

def Crear():
    cursor=conexion.cursor()

    try:
        datos=miNombre.get(),miApellidos.get(),miEdad.get(),miDorsal.get(),miPosicion.get()
        cursor.execute("INSERT INTO jugadores VALUES (NULL,?,?,?,?,?)", (datos))
        conexion.commit()

    except mariadb.Error as error_registro:
        print (f"Error al registrar los datos {error_registro}")
        pass
    limpiarCampos()
    mostrar()

def mostrar():
    cursor=conexion.cursor()
    registros=tree.get_children()
    for elemento in registros:
        tree.delete(elemento)

    try:
        cursor.execute("SELECT * FROM jugadores")
        for row in cursor:
            tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4]))
    except:
        pass
    
    
    # TABLA # 

tree=ttk.Treeview(height=10, columns=('#0', '#1', '#2', '#3', '#4'))
tree.place(x= 0, y= 130)


root.mainloop()