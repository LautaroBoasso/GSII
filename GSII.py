from tkinter import *
import mariadb

# Ventana principal

ventana_principal = Tk()
ventana_principal.geometry("600x800")
ventana_principal.title ("TP Final") 

id = StringVar()
a_nombre = StringVar()
a_apellidos = StringVar()
a_edad = StringVar()
a_dorsal = StringVar()
a_posicion = StringVar()

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

# Funciones


def abrir_bdd():
    ventana_verbdd = Toplevel()
    ventana_verbdd.title ("Base de Datos")
    ventana_verbdd.geometry ("800x800")
    boton_cerrar = Button(ventana_verbdd, text = "Cerrar", command=ventana_verbdd.destroy)
    boton_cerrar.pack(side = BOTTOM)


def agregar_registro():
    ventana_registro = Toplevel()
    ventana_registro.title ("Agregar Registro")
    ventana_registro.geometry ("400x600")

    texto_inicial_agregar_registro = Label(ventana_registro,
     text="Registro para nuevos jugadores",
     font="arial 16",
     fg="red")
    texto_inicial_agregar_registro.grid(row=0, columnspan=2)


    agregar_registro_nombre = Label(ventana_registro, text= "Nombre")
    agregar_registro_nombre.grid(row = 1, column = 0, pady=5)
    v_nombre = Entry(ventana_registro, textvariable=a_nombre)
    v_nombre.grid(row = 1, column = 1)

    agregar_registro_apellidos = Label(ventana_registro, text= "Apellido")
    agregar_registro_apellidos.grid(row = 2, column = 0, pady=5)
    v_apellidos = Entry(ventana_registro, textvariable=a_apellidos)
    v_apellidos.grid(row = 2, column = 1)

    agregar_registro_dorsal = Label(ventana_registro, text= "Dorsal")
    agregar_registro_dorsal.grid(row = 3, column = 0, pady=5)
    v_dorsal = Entry(ventana_registro, textvariable=a_dorsal)
    v_dorsal.grid(row = 3, column= 1)

    agregar_registro_edad = Label(ventana_registro, text = "Edad")
    agregar_registro_edad.grid(row = 4, column = 0, pady=5)
    v_edad = Entry(ventana_registro, textvariable=a_edad)
    v_edad.grid(row = 4, column = 1)

    agregar_registro_posicion = Label(ventana_registro, text= "Posición")
    agregar_registro_posicion.grid(row = 5, column = 0, pady=5)
    v_posicion = Entry(ventana_registro, textvariable=a_posicion)
    v_posicion.grid(row = 5, column= 1)

    boton_registrar = Button(ventana_registro, text = "Registrar", command=registro_jugador)
    boton_registrar.grid(row = 6, column = 0, pady=5)

    #boton_cerrar_registro = Button(ventana_registro, text = "Cerrar", command=ventana_registro.destroy)
    #boton_cerrar_registro.grid(row = 6, column= 1)

def registro_jugador():
    cursor=conexion.cursor()
    try:
        datos = a_nombre.get(), a_apellidos.get(), a_dorsal.get(), a_edad.get(), a_posicion.get()
        cursor.execute("INSERT INTO jugadores VALUES (NULL,?,?,?,?,?)", (datos))
        conexion.commit()

    except mariadb.Error as error_registro:
        print (f"Error al registrar los datos {error_registro}")


# Interfaz gráfica

etiqueta = Label(ventana_principal, text = "Este es el TP para Gestión de Software II", bg = "Cyan")
etiqueta.pack(fill = X)

etiqueta2 = Label(ventana_principal, text = "Hecho por Lautaro Boasso", bg = "Orange")
etiqueta2.pack(side = BOTTOM)

boton1 = Button(ventana_principal, padx= 4, pady= 5, text = "Ver Base de Datos", command= abrir_bdd)
boton1.pack()

boton2 = Button(ventana_principal, padx= 3, pady= 4, text = "Agregar un nuevo registro",command= agregar_registro)
boton2.pack()


boton3 = Button(ventana_principal, padx= 3, pady= 4, text = "Modificar un Registro",command = lambda: print ("Prueba"))
boton3.pack()

boton4 = Button(ventana_principal, padx= 3, pady= 4, text = "Eliminar un Registro",command = lambda: print ("Prueba"))
boton4.pack()

mainloop()