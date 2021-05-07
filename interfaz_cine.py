from tkinter import *
from tkinter import ttk
import cine_database 

ventana = Tk()
frame_app = Marco(ventana, ancho=400, alto=600, bg="rojo")
frame_app. paquete()

cartelera=StringVar()
pelicula=StringVar()
hora=StringVar()
precio=StringVar()

def crear_sala():
    cartelera=entry_cartelera. obtener()
    pelicula=entry_pelicula. obtener()
    hora=entry_hora. obtener()
    fecha=entry_fecha. obtener()
    idioma=entry_idioma. obtener()

    cine_db=cine_database. MyDatabase()
    cine_db. insert_db(cartelera, pelicula, hora, fecha, idioma)

# Widgets dentro de la aplicación contendiente
frame_navbar = Marco(frame_app, ancho=400, altura=100)
frame_navbar. cuadrícula(fila=0, columna=0)
frame_title = Marco(frame_app, ancho=400, altura=120)
frame_title. cuadrícula(fila=1, columna=0)
frame_options = Marco(frame_app, ancho=400, altura=500)
frame_options. cuadrícula(fila=2, columna=0)

# Widgets dentro del contendiente NAVBAR
título = Etiqueta(frame_navbar, 
              texto="CINE LOVE",
              fuente=("Century Gothic", "14"))
título. lugar(x=250, y=40)

# Widgets dentro del título del contendiente
title1 = Etiqueta(frame_title, 
              texto="SALAS DE CINE", 
              fuente=("Century Gothic", "22", "bold"),
              justificar=IZQUIERDA)
título1. lugar(x=25, y=10)
title2 = Etiqueta(frame_title, 
              texto="Todos los campos son obligartorios.", 
              fuente=("Century Gothic", "14"),
              justificar=IZQUIERDA)
título2. lugar(x=25, y=50)

# Widgets dentro de las OPCIONES de contendiente
frame_form = Marco(frame_options, ancho=350, altura=450, bg="#d48df0")
frame_form. lugar(x=25, y=5)
label_cartelera = Etiqueta(frame_form, 
              texto="CARTELERA:",
              fuente=("Century Gothic", "20", "bold"),
              fg="blanco",
              bg="#d48df0")
label_cartelera. lugar(x=30, y=30)
entry_cartelera = Entrada(frame_form, justificar=IZQUIERDA, anchura=25, 
             fuente=("Century Gothic", "14"))
entry_cartelera. lugar(x=30, y=70)

label_pelicula = Etiqueta(frame_form, 
              texto="PELICULA:",
              fuente=("Century Gothic", "20", "bold"),
              fg="blanco",
              bg="#d48df0")
label_pelicula. lugar(x=30, y=100)
entry_pelicula = Entrada(frame_form, justificar=IZQUIERDA, anchura=25, 
                fuente=("Century Gothic", "14"))
entry_pelicula. lugar(x=30, y=140)

label_hora = Etiqueta(frame_form, 
              texto="HORA:",
              fuente=("Century Gothic", "20", "bold"),
              fg="blanco",
              bg="#d48df0")
label_hora. lugar(x=30, y=170)
entry_hora = Entrada(frame_form, justificar=IZQUIERDA, anchura=25, 
                fuente=("Century Gothic", "14"))
entry_hora. lugar(x=30, y=210)

label_fecha = Etiqueta(frame_form, 
              texto="FECHA:",
              fuente=("Century Gothic", "20", "bold"),
              fg="blanco",
              bg="#d48df0")
label_fecha. lugar(x=30, y=240)
entry_fecha = Entrada(frame_form, justificar=IZQUIERDA, anchura=25,
               fuente=("Century Gothic", "14"))
entry_fecha. lugar(x=30, y=280)

label_idioma = Etiqueta(frame_form, 
              texto="IDIOMA:",
              fuente=("Century Gothic", "20", "bold"),
              fg="blanco",
              bg="#d48df0")
label_idioma. lugar(x=30, y=310)
entry_idioma = Entrada(frame_form, justificar=IZQUIERDA, anchura=25,
               fuente=("Century Gothic", "14"))
entry_idioma. lugar(x=30, y=350)


button_agregar = Botón(frame_form, texto="Crear sala", 
                        fuente=("Century Gothic", "14", "bold"),
                        comando=crear_sala)
button_agregar. lugar(x=110, y=400)

ventana. mainloop()