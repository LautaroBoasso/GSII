from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3

class Jugadores:
 
 db_nombre = 'jugadores.db'

 def __init__(self,window):

    self.wind = window
    self.wind.title('Aplicación CRUD para GSII')
    self.wind.geometry("1000x400")
    self.wind.resizable(0, 0)

    # ETIQUETAS Y CAJAS DE TEXTO #

    label_Nombre=Label(self.wind, text="Nombre")
    label_Nombre.place(x=15,y=10)
    self.Nombre=Entry(self.wind,width=20)
    self.Nombre.focus()
    self.Nombre.place(x=70,y=10)

    label_Apellidos=Label(self.wind, text="Apellidos")
    label_Apellidos.place(x=215,y=10)
    self.Apellidos=Entry(self.wind, width=30)
    self.Apellidos.place(x=270,y=10)

    label_Edad=Label(self.wind, text="Edad")
    label_Edad.place(x=466,y=10)
    self.Edad=Entry(self.wind, width=5)
    self.Edad.place(x=500,y=10)

    label_Dorsal=Label(self.wind, text="Dorsal")
    label_Dorsal.place(x=165,y=40)
    self.Dorsal=Entry(self.wind, width=5)
    self.Dorsal.place(x=205,y=40)


    label_Edad=Label(self.wind, text="Posición")
    label_Edad.place(x=320,y=40)
    self.combo_posicion=ttk.Combobox(self.wind,values=["Arquero","Defensor","Mediocampista","Delantero"], width=22,state="readonly")
    self.combo_posicion.place(x=370,y=40)

    self.Buscador=Entry(self.wind, width=20)
    self.Buscador.place(x=640,y=90)

    self.ID=Entry(self.wind)

    # BOTONES #

    boton_agregar = Button(self.wind, text="Agregar Registro",bg="lightgreen", command= self.agregar_jugadores)
    boton_agregar.place(x=15, y=90)

    boton_modificar=Button(self.wind, text="Modificar Registro",bg="lightblue")
    boton_modificar.place(x=155, y=90)

    boton_mostrar=Button(self.wind, text="Mostrar Lista",bg="yellow")
    boton_mostrar.place(x=310, y=90)

    boton_eliminar=Button(self.wind, text="Eliminar Registro",bg="red", command = self.eliminar_jugadores)
    boton_eliminar.place(x=435, y=90)

    boton_buscar=Button(self.wind, text="Buscar")
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

    self.obtener_jugadores()

 def LimpiarCampos(self):
    self.Nombre.delete(0, END)
    self.Apellidos.delete(0, END)
    self.Edad.delete(0, END)
    self.Dorsal.delete(0, END)
    self.combo_posicion.set("")
    
 def ejecutar_query(self, query, parameters = ()):
    with sqlite3.connect(self.db_nombre) as conexion:
       cursor = conexion.cursor()
       resultado = cursor.execute(query, parameters)
       conexion.commit()
    return resultado
 
 def obtener_jugadores(self):
     
     
     records = self.tree.get_children()
     for element in records:
        self.tree.delete(element)

     query = 'SELECT * FROM jugadores'
     db_rows = self.ejecutar_query(query)
     for row in db_rows:
        self.tree.insert("",0, text=row[0], values = (row[1],row[2],row[3],row[4],row[5]))
    

 def validar_jugadores(self):
   return len(self.Nombre.get()) != 0 and len(self.Apellidos.get()) !=0 and len(self.Edad.get()) !=0 and len(self.Dorsal.get()) !=0 and len(self.combo_posicion.get()) !=0

 def agregar_jugadores(self):
    if self.validar_jugadores():
       query = 'INSERT INTO jugadores VALUES(NULL, ?, ?, ?, ?, ?)'
       parameters = (self.Nombre.get(), self.Apellidos.get(), self.Edad.get(), self.Dorsal.get(), self.combo_posicion.get())
       self.ejecutar_query(query, parameters)
       messagebox.showinfo('NOTIFICACIÓN','El jugador {}{} fue agregado exitosamente.'.format(self.Nombre.get(),self.Apellidos.get()))
    else:
       messagebox.showerror('ERROR','Uno de los campos está vacío. Verífiquelos e intente nuevamente.')
    self.obtener_jugadores()
    self.LimpiarCampos()

 def eliminar_jugadores(self):
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM jugadores WHERE nombre = ?'
        self.ejecutar_query(query, (name, ))
        self.message['text'] = 'Record {} deleted Successfully'.format(name)
        self.obtener_jugadores()


if __name__ == '__main__':
    window = Tk()
    aplicacion = Jugadores(window)
    window.mainloop()