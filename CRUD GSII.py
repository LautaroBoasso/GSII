from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mariadb

# Ventana principal e Interfaz Gráfica

root=Tk()
root.title("Aplicación CRUD para GSII")
root.geometry("780x400")

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

# FUNCIONES # 

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
    acerca= """Aplicación CRUD
    Hecha por Lautaro Boasso para Gestión de Software II
    Con Python Tkinter
    """
    messagebox.showinfo(title="INFORMACION", message=acerca)

def MensajeBDD():
    acerca= """La Base de Datos fue creada con la siguiente sintaxis: 

CREATE TABLE jugadores 
(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(32) NOT NULL, 
apellidos VARCHAR(64) NOT NULL, 
edad VARCHAR(2),
dorsal VARCHAR(3),  
posicion VARCHAR (25) NOT NULL)
    """
    messagebox.showinfo(title="INFORMACION", message=acerca)


# Desarrollo CRUD #

def actualizar():
    cursor=conexion.cursor()

    try:
        datos=miNombre.get(),miApellidos.get(),miEdad.get(),miDorsal.get(),miPosicion.get()
        cursor.execute("UPDATE jugadores SET nombre=?, apellidos=?, edad=?, dorsal=?, posicion=? WHERE id="+miID.get(), (datos))
        conexion.commit()

    except mariadb.Error as error_registro:
        print (f"Error al registrar los datos {error_registro}")
        pass
    LimpiarCampos()
    mostrar()

def eliminar():
    cursor=conexion.cursor()

    try:
        if messagebox.askyesno(message="¿Desea eliminar este registro?", title="ADVERTENCIA"):
            cursor.execute("DELETE FROM jugadores WHERE id="+miID.get())
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de borrar el registro")
        pass
    LimpiarCampos()
    mostrar()


def Crear():
    cursor=conexion.cursor()

    try:
        datos=miNombre.get(),miApellidos.get(),miEdad.get(),miDorsal.get(),miPosicion.get()
        cursor.execute("INSERT INTO jugadores VALUES (NULL,?,?,?,?,?)", (datos))
        conexion.commit()

    except mariadb.Error as error_registro:
        print (f"Error al registrar los datos {error_registro}")
        pass
    LimpiarCampos()
    mostrar()

def mostrar():
    cursor=conexion.cursor()
    registros=tree.get_children()
    for elemento in registros:
        tree.delete(elemento)

    try:
        cursor.execute("SELECT * FROM jugadores")
        for row in cursor:
            tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5]))
    except:
        pass
    
    
    # TABLA # 

tree=ttk.Treeview(height=10, columns=('#0', '#1', '#2', '#3', '#4'))
tree.place(x= 15, y= 130)
tree.column('#0', width=50)
tree.heading('#0', text="ID", anchor=CENTER)
tree.heading('#1', text="Nombre", anchor=CENTER)
tree.heading('#2', text="Apellidos", anchor=CENTER)
tree.heading('#3', text="Edad", anchor=CENTER)
tree.column('#3', width=50)
tree.heading('#4', text="Dorsal", anchor=CENTER)
tree.column('#4', width=50)
tree.heading('#5', text="Posición", anchor=CENTER)

def SeleccionarUsandoClick(event):
    item=tree.identify('item',event.x,event.y)
    miID.set(tree.item(item,"text"))
    miNombre.set(tree.item(item,"values")[0])
    miApellidos.set(tree.item(item,"values")[1])
    miEdad.set(tree.item(item,"values")[2])
    miDorsal.set(tree.item(item,"values")[3])
    miPosicion.set(tree.item(item,"values")[4])

tree.bind("<Double-1>", SeleccionarUsandoClick)

# WIDGETS #
# MENUS #
menubar=Menu(root)
menubasedat=Menu(menubar,tearoff=0)
menubasedat.add_command(label="Salir", command=SalirAplicacion)
menubar.add_cascade(label="Inicio", menu=menubasedat)

ayudamenu=Menu(menubar,tearoff=0)
ayudamenu.add_command(label="Resetear Campos", command=LimpiarCampos)
ayudamenu.add_command(label="Acerca", command=Mensaje)
ayudamenu.add_command(label="Sobre la Base de Datos", command=MensajeBDD)
menubar.add_cascade(label="Ayuda",menu=ayudamenu)

# ETIQUETAS Y CAJAS DE TEXTO #

e1=Entry(root, textvariable=miID)

l2=Label(root, text="Nombre")
l2.place(x=80,y=10)
e2=Entry(root, textvariable=miNombre, width=20)
e2.place(x=135,y=10)

l3=Label(root, text="Apellidos")
l3.place(x=280,y=10)
e3=Entry(root, textvariable=miApellidos, width=30)
e3.place(x=335,y=10)

l4=Label(root, text="Edad")
l4.place(x=540,y=10)
e4=Entry(root, textvariable=miEdad, width=5)
e4.place(x=575,y=10)

l5=Label(root, text="Dorsal")
l5.place(x=230,y=40)
e5=Entry(root, textvariable=miDorsal, width=5)
e5.place(x=270,y=40)

l6=Label(root, text="Posición")
l6.place(x=400,y=40)
e6=Entry(root, textvariable=miPosicion, width=25)
e6.place(x=455,y=40)

# BOTONES #

b1=Button(root, text="Agregar Registro",bg="lightgreen", command=Crear)
b1.place(x=20, y=90)

b2=Button(root, text="Modificar Registro",bg="lightblue", command=actualizar)
b2.place(x=180, y=90)

b3=Button(root, text="Mostrar Lista",bg="yellow", command=mostrar)
b3.place(x=320, y=90)

b4=Button(root, text="Eliminar Registro",bg="red", command=eliminar)
b4.place(x=450, y=90)

root.config(menu=menubar)

root.mainloop()