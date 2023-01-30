import tkinter
import RPi.GPIO as GPIO
import time 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

rojo1,verde1,azul1=2,3,4
rojo2,verde2,azul2=17,27,22
rojo3,verde3,azul3=10,9,11

def controlRojo():
    time.sleep(0.1) 
    GPIO.output(rojo1, True)
    GPIO.output(verde1, False)
    GPIO.output(azul1, False)
    
def controlAzul():
    time.sleep(0.1) 
    GPIO.output(rojo1, False)
    GPIO.output(verde1, True)
    GPIO.output(azul1, False)
    
def controlVerde():
    time.sleep(0.1) 
    GPIO.output(rojo1, False)
    GPIO.output(verde1, False)
    GPIO.output(azul1, True)
    
def controlAmarillo():
    time.sleep(0.1) 
    GPIO.output(rojo1, True)
    GPIO.output(verde1, False)
    GPIO.output(azul1, True)
    
def controlRosa():
    time.sleep(0.1) 
    GPIO.output(rojo1, True)
    GPIO.output(verde1, True)
    GPIO.output(azul1, False)
    
def controlTurquesa():
    time.sleep(0.1) 
    GPIO.output(rojo1, False)
    GPIO.output(verde1, True)
    GPIO.output(azul1, True)
    
def controlBlanco():
    time.sleep(0.1) 
    GPIO.output(rojo1, True)
    GPIO.output(verde1, True)
    GPIO.output(azul1, True)
    
def apagado():
    time.sleep(0.1) 
    GPIO.output(rojo1, False)
    GPIO.output(verde1, False)
    GPIO.output(azul1, False)
    
def NuevaVentana(): 
    ventana = tkinter.Tk()
    ventana.title("PROYECTO FINAL")
    ventana.geometry("200x200")
    ventana.configure(bg="pink")
    etiqueta = tkinter.Label(ventana, text="Menu Principal", bg = "yellow")
    etiqueta.pack(fill = tkinter.X)
    Botton = tkinter.Button(ventana, bg = "green", text = "Controlar Luces", command = MenuCuartos)
    Botton.place(x=40, y=30)
    Botton1 = tkinter.Button(ventana, bg = "green", text = "Sensores de Temperatura", command = NuevaVentana2)
    Botton1.place(x=0, y=70)
    Botton2 = tkinter.Button(ventana, command = ventana.destroy, bg="red", text="Cerrar")
    Botton2.place(x=70, y=120)
    ventana.mainloop()
    
def MenuCuartos(): 
    ventana1 = tkinter.Tk()
    ventana1.title("PROYECTO FINAL")
    ventana1.geometry("200x200")
    ventana1.configure(bg="pink")
    etiqueta = tkinter.Label(ventana1, text="Menu Principal", bg = "yellow")
    etiqueta.pack(fill = tkinter.X)
    
    boton1 = Button(ventana1, bg = "green", text = 'Cuarto 1', width = 10, command = colores())
    boton1.grid(row = 0, column = 2)
    
    boton2 = Button(ventana1, bg = "green", text = 'Baño', width = 10, command = colores())
    boton2.grid(row = 1, column = 2)
    
    boton3 = Button(ventana1, bg = "green", text = 'Cuarto 2', width = 10, command = colores())
    boton3.grid(row = 2, column = 2)
    
    boton4 = Button(ventana1, bg = "green", text = 'Baño 2', width = 10, command = colores())
    boton4.grid(row = 1, column = 2)
    
    boton5 = Button(ventana1, bg = "green", text = 'Comedor', width = 10, command = colores())
    boton5.grid(row = 3, column = 2)
    
    boton6 = Button(ventana1, bg = "green", text = 'Luces de Fuera', width = 10, command = colores())
    boton6.grid(row = 4, column = 2)
    
    boton7 = Button(ventana1, command = ventana1.destroy, bg="red", text="Cerrar")
    boton7.grid(row = 4, column = 2)
    ventana.mainloop()
    
    
def colores():
    
    ventana2 = tkinter.Tk()
    ventana2.title("PROYECTO FINAL")
    ventana2.geometry("200x200")
    ventana2.configure(bg="pink")
    etiqueta = tkinter.Label(ventana2, text="Colores", bg = "yellow")
    etiqueta.pack(fill = tkinter.X)
    
    etiqueta = tkinter.Label(ventana1, text="cocina: ", bg = "green")
    etiqueta.pack()
    
    RB = tkinter.Radiobutton(ventana2, text="Rojo", value=1,bg="blue", command = controlRojo())
    RB.pack()
    
    RB = tkinter.Radiobutton(ventana2, text="Verde", value=2,bg="blue", command = controlVerde())
    RB.pack()
    
    RB = tkinter.Radiobutton(ventana2, text="Azul", value=3,bg="blue", command = controlAzul())
    RB.pack()
    
    RB = tkinter.Radiobutton(ventana2, text="Amarillo", value=4,bg="blue",  command = controlVerde())
    RB.pack()
    
    RB = tkinter.Radiobutton(ventana2, text="Rosa", value=5,bg="blue", command = controlRosa())
    RB.pack()
    
    RB = tkinter.Radiobutton(ventana2, text="Turquesa", value=6,bg="blue", command = controlTurquesa())
    RB.pack()
    
    RB = tkinter.Radiobutton(ventana2, text="Blanco", value=7,bg="blue", command = controlBlanco())
    RB.pack()
    
    Botton2 = tkinter.Button(ventana2, command = ventana2.destroy, bg="red", text="Cerrar")
    Botton2.place(x=80, y=50)
    ventana1.mainloop()
    
    
    
root = tkinter.Tk()
root.title("PROYECTO")
root.geometry("200x200")
root.configure(bg = "pink")
etiqueta = tkinter.Label(root, text="Interfaces de Computadoras", bg = "yellow")
etiqueta.pack(fill = tkinter.X)