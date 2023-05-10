from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Ventana principal e Interfaz Gráfica

class Jugadores:
    db_nombre = 'jugadores.db'

    def __init__(self):
     self.root=Tk()
     self.root.title("Aplicación CRUD para GSII")
     self.root.geometry("1000x400")

     self.miID= StringVar()
     self.miNombre= StringVar()
     self.miApellidos= StringVar()
     self.miEdad= StringVar()
     self.miDorsal= StringVar()
     self.miPosicion= StringVar()
     
     # ETIQUETAS Y CAJAS DE TEXTO #

     e1=Entry(self.root, textvariable=self.miID)

     l2=Label(self.root, text="Nombre")
     l2.place(x=15,y=10)
     self.Nombre=Entry(self.root, textvariable=self.miNombre, width=20)
     self.Nombre.place(x=70,y=10)

     l3=Label(self.root, text="Apellidos")
     l3.place(x=215,y=10)
     self.Apellidos=Entry(self.root, textvariable=self.miApellidos, width=30)
     self.Apellidos.place(x=270,y=10)

     l4=Label(self.root, text="Edad")
     l4.place(x=466,y=10)
     self.Edad=Entry(self.root, textvariable=self.miEdad, width=5)
     self.Edad.place(x=500,y=10)

     l5=Label(self.root, text="Dorsal")
     l5.place(x=165,y=40)
     self.Dorsal=Entry(self.root, textvariable=self.miDorsal, width=5)
     self.Dorsal.place(x=205,y=40)

     l6=Label(self.root, text="Posición")
     l6.place(x=325,y=40)
     self.Posicion=Entry(self.root, textvariable=self.miPosicion, width=25)
     self.Posicion.place(x=380,y=40)

     self.e7=Entry(self.root, width=20)
     self.e7.place(x=640,y=90)

     # BOTONES #

     boton_agregar=Button(self.root, text="Agregar Registro",bg="lightgreen", command=Crear)
     boton_agregar.place(x=15, y=90)

     boton_modificar=Button(self.root, text="Modificar Registro",bg="lightblue", command=actualizar)
     boton_modificar.place(x=155, y=90)

     boton_mostrar=Button(self.root, text="Mostrar Lista",bg="yellow", command=mostrar)
     boton_mostrar.place(x=310, y=90)

     boton_eliminar=Button(self.root, text="Eliminar Registro",bg="red", command=eliminar)
     boton_eliminar.place(x=435, y=90)

     boton_buscar=Button(self.root, text="Buscar", command=Buscar_jugadores)
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



    # FUNCIONES # 

 def SalirAplicacion(self):
     valor=messagebox.askquestion("Salir","¿Cerrar aplicación?")
     if valor=="yes":
            self.root.destroy()


 def LimpiarCampos(self):
     self.miID.set("")
     self.miNombre.set("")
     self.miApellidos.set("")
     self.miEdad.set("")
     self.miDorsal.set("")
     self.miPosicion.set("")


 # Desarrollo CRUD #

 def actualizar(self):

 try:
     datos=self.miNombre.get(),self.miApellidos.get(),self.miEdad.get(),self.miDorsal.get(),self.miPosicion.get()
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
            conexion.commit()
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


def SeleccionarUsandoClick(event):
    item=tree.identify('item',event.x,event.y)
    miID.set(tree.item(item,"text"))
    miNombre.set(tree.item(item,"values")[0])
    miApellidos.set(tree.item(item,"values")[1])
    miEdad.set(tree.item(item,"values")[2])
    miDorsal.set(tree.item(item,"values")[3])
    miPosicion.set(tree.item(item,"values")[4])

tree.bind("<Double-1>", SeleccionarUsandoClick)

def Buscar_jugadores():
        #Obtener todos los elementos con get_children(), que retorna una tupla de ID.
        records=tree.get_children()
        for element in records:
            tree.delete(element)
        
        if (combo_buscar.get()=='Nombre'):
            query=("SELECT * FROM jugadores WHERE Nombre LIKE ? ") 
            parameters=("%"+e7.get()+"%")
            db_rows=Ejecutar_consulta(query,(parameters,))
            for row in db_rows:
                tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5]))
            if(list(tree.get_children())==[]):
               messagebox.showerror("ERROR","Jugador no encontrado")
        else:
            query=("SELECT * FROM jugadores WHERE Apellidos LIKE ? ")
            parameters=("%"+e7.get()+"%")
            db_rows=Ejecutar_consulta(query,(parameters,))
            for row in db_rows:
                tree.insert("",0, text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))
            if(list(tree.get_children())==[]):
               messagebox.showerror("ERROR","Producto no encontrado")

def Ejecutar_consulta(query, parameters=()):
        
        cursor=conexion.cursor()
        result=cursor.execute(query,parameters)
        conexion.commit()
        return result
        
 

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

label_buscar=Label(root,text="Buscar Por: ",font=("Comic Sans", 10,"bold"))
label_buscar.place(x=637, y=35)
combo_buscar=ttk.Combobox(root,values=["Nombre","Apellido","Edad","Dorsal","Posición"], width=22,state="readonly")
combo_buscar.current(0)
combo_buscar.place(x=640, y=60)






if __name__ == '__main__':
    root = Tk()
    aplicacion = Jugadores(root)
    root.mainloop()