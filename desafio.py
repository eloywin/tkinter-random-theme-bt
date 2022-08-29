from tkinter import *
import random


mi_id = 0
colores = [
    "blue",
    "cyan",
    "black",
    "purple",
    "yellow",
    "orange",
    "grey",
    "pink",
    "green",
    "white",
]


master = Tk()

var_nombre = StringVar()
var_apellido = StringVar()
var_descripcion = StringVar()


encabezado = Label(master, text="Ingrese sus datos", bg="purple")
encabezado.grid(row=0, column=1)

titulo = Label(master, text="Titulo")
titulo.grid(row=1, column=0, sticky=W)
ruta = Label(master, text="Ruta")
ruta.grid(row=2, column=0, sticky=W)
descripcion = Label(master, text="Descripción")
descripcion.grid(row=3, column=0, sticky=W)

entry_nombre = Entry(master, textvariable=var_nombre, width=25)
entry_nombre.grid(row=1, column=1)
entry_apellido = Entry(master, textvariable=var_apellido, width=25)
entry_apellido.grid(row=2, column=1)
entry_descripcion = Entry(master, textvariable=var_descripcion, width=25)
entry_descripcion.grid(row=3, column=1)


def funcion_send():
    global mi_id
    mi_id += 1
    print(
        "Nueva alta de datos :\n",
        var_nombre.get(),
        var_apellido.get(),
        var_descripcion.get(),
    )


def funcion_sorpresa():
    master.configure(bg=colores[random.randrange(0, 10)])


boton_send = Button(master, text="Guardar", command=funcion_send)
boton_send.grid(row=4, column=1)

boton_sorpresa = Button(master, text="Sorpresa", command=funcion_sorpresa)
boton_sorpresa.grid(row=4, column=3)

master.mainloop()
