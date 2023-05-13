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
     self.root.resizable(0,0)

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

     boton_agregar=Button(self.root, text="Agregar Registro",bg="lightgreen", command=self.Crear)
     boton_agregar.place(x=15, y=90)

     boton_modificar=Button(self.root, text="Modificar Registro",bg="lightblue", command=self.actualizar)
     boton_modificar.place(x=155, y=90)

     boton_mostrar=Button(self.root, text="Mostrar Lista",bg="yellow", command=self.mostrar)
     boton_mostrar.place(x=310, y=90)

     boton_eliminar=Button(self.root, text="Eliminar Registro",bg="red", command=self.eliminar)
     boton_eliminar.place(x=435, y=90)

     boton_buscar=Button(self.root, text="Buscar", command=self.Buscar_jugadores)
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

       # WIDGETS #
       # MENUS #
     menubar=Menu(self.root)
     menubasedat=Menu(menubar,tearoff=0)
     menubasedat.add_command(label="Salir", command=self.SalirAplicacion)
     menubar.add_cascade(label="Inicio", menu=menubasedat)

     ayudamenu=Menu(menubar,tearoff=0)
     ayudamenu.add_command(label="Resetear Campos", command=self.LimpiarCampos)
     ayudamenu.add_command(label="Acerca", command=self.Mensaje)
     ayudamenu.add_command(label="Sobre la Base de Datos", command=self.MensajeBDD)
     menubar.add_cascade(label="Ayuda",menu=ayudamenu)

     label_buscar=Label(self.root,text="Buscar Por: ",font=("Comic Sans", 10,"bold"))
     label_buscar.place(x=637, y=35)
     combo_buscar=ttk.Combobox(root,values=["Nombre","Apellido","Edad","Dorsal","Posición"], width=22,state="readonly")
     combo_buscar.current(0)
     combo_buscar.place(x=640, y=60)



    # FUNCIONES # 

 def SalirAplicacion(self):
     valor=messagebox.askquestion("Salir","¿Cerrar aplicación?")
     if valor=="yes":
            self.root.destroy()

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


 def LimpiarCampos(self):
     self.miID.set("")
     self.miNombre.set("")
     self.miApellidos.set("")
     self.miEdad.set("")
     self.miDorsal.set("")
     self.miPosicion.set("")

 def ejecutar_query(self, query, parameters = ()):
    with sqlite3.connect(self.db_nombre) as conexion:
       cursor = conexion.cursor()
       resultado = cursor.execute(query, parameters)
       conexion.commit()
    return resultado


 # Desarrollo CRUD #

 def mostrar(self):
    cursor=conexion.cursor()
    registros=self.tree.get_children()
    for elemento in registros:
        self.tree.delete(elemento)

 def actualizar(self):

         try:
             datos=self.miNombre.get(),self.miApellidos.get(),self.miEdad.get(),self.miDorsal.get(),self.miPosicion.get()
             cursor.execute("UPDATE jugadores SET nombre=?, apellidos=?, edad=?, dorsal=?, posicion=? WHERE id="+miID.get(), (datos))
             conexion.commit()

         except mariadb.Error as error_registro:
            print (f"Error al registrar los datos {error_registro}")
            pass
         self.LimpiarCampos()
         self.mostrar()

 def eliminar(self):
     cursor=conexion.cursor()

     try:
        if messagebox.askyesno(message="¿Desea eliminar este registro?", title="ADVERTENCIA"):
            cursor.execute("DELETE FROM jugadores WHERE id="+self.miID.get())
            conexion.commit()
     except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de borrar el registro")
        pass
     self.LimpiarCampos()
     self.mostrar()


 def Crear(self):
    cursor=conexion.cursor()

    try:
        datos=self.miNombre.get(),self.miApellidos.get(),self.miEdad.get(),self.miDorsal.get(),self.miPosicion.get()
        cursor.execute("INSERT INTO jugadores VALUES (NULL,?,?,?,?,?)", (datos))
        conexion.commit()

    except mariadb.Error as error_registro:
        print (f"Error al registrar los datos {error_registro}")
        pass
    self.LimpiarCampos()
    self.mostrar()

 def mostrar(self):
    cursor=conexion.cursor()
    registros=self.tree.get_children()
    for elemento in registros:
        self.tree.delete(elemento)

    try:
        cursor.execute("SELECT * FROM jugadores")
        for row in cursor:
            self.tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5]))
    except:
        pass


 def SeleccionarUsandoClick(self, event):
    item=self.tree.identify('item',event.x,event.y)
    self.miID.set(self.tree.item(item,"text"))
    self.miNombre.set(self.tree.item(item,"values")[0])
    self.miApellidos.set(self.tree.item(item,"values")[1])
    self.miEdad.set(self.tree.item(item,"values")[2])
    self.miDorsal.set(self.tree.item(item,"values")[3])
    self.miPosicion.set(self.tree.item(item,"values")[4])

    self.tree.bind("<Double-1>", self.SeleccionarUsandoClick)

 def Buscar_jugadores(self):
        #Obtener todos los elementos con get_children(), que retorna una tupla de ID.
        records=self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        
        if (self.combo_buscar.get()=='Nombre'):
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




if __name__ == '__main__':
    root = Tk()
    aplicacion = Jugadores(root)
    root.mainloop()