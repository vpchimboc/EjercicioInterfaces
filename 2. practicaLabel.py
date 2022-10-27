from tkinter import *

root=Tk()
miFrame=Frame(root,width=500,height=400)
miFrame.pack()
miLabel=Label(miFrame,text="Hola Alumnos Python")
#miLabel.pack()
miLabel.place(x=100,y=200)
###imagen
miImagen=PhotoImage(file="imagen.png")
milabel2=Label(miFrame,image=miImagen)
milabel2.place(x=100,y=5)
##Cuadrsos de texto
cuadro1=Entry(miFrame)
cuadro1.place(x=100,y=250)
cuadro1.config(fg="red",justify="center")

root.mainloop()