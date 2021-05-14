
import swowpy
import tkinter as tk
from tkinter import *
import time


ventana = tk.Tk()
ventana.geometry("400x400")
ventana.title("Delta-Weather")
ventana.configure(bg="black")
font=("Verdana",15,"bold")



api_key = "d6abc872b027b3817c19cc3276341f01"

def tiempo(): #funcion que recoge la varialbe del entry de tk y reproduce las funciones de swowpy
    ciudad_aux = ciudad.get()
    mycity = swowpy.Swowpy(api_key,ciudad_aux)
    print("Nombre de la ciudad: ",ciudad_aux)
    print("Temperatura: ",mycity.temperature()-273.15)
    print("Tiempo: ",mycity.current_weather('Description'))
    var_ventana.set(f"Cargando....")
    time.sleep(1)
    var_ventana.set(f"Temperatura:  {mycity.temperature()-273.15} ºC" + '\n' f"Tiempo: {mycity.current_weather('Description')} " )



ciudad = tk.StringVar() #variable de tk para poder pasarle a la funcion la ciudad que se meta en tk
var_ventana = tk.StringVar()

#Titulo programa
titulo=tk.Label(ventana,text="DELTA WEATHER APP",bg="black",fg="blue",font=font)
titulo.place(x=10,y=10)

#Texto para indicar donde se introduce la ciudad
ciudad_text=tk.Label(ventana,text="Introduce ciudad ",bg="black",fg="blue",font=font)
ciudad_text.place(x=10,y=50)

#Entrada de texto
e1 = Entry(ventana,textvariable=ciudad).place(x = 200, y = 55)
sbmitbtn = tk.Button(ventana, text = "Buscar",activebackground = "blue", activeforeground = "grey", command=tiempo).place(x = 250, y = 85)

mi_label = tk.Label(ventana, textvariable=var_ventana)
mi_label.place(x = 100, y = 150)
var_ventana.set("TIEMPO" )

















ventana.mainloop()
