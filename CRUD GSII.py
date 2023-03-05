from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mariadb

# Ventana principal e Interfaz Gráfica

root=Tk()
root.title("Aplicación CRUD para GSII")
root.geometry("700x450")

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