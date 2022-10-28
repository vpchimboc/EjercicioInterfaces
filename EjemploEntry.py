from tkinter import*
from tkinter import messagebox

raiz=Tk()
###Ventanas Emergentes
def infoAdicional():
    #messagebox.showinfo("Información","Versión Codigo 1.0.")
    #messagebox.showwarning("Advertencia","Licencia Caducada")
    #messagebox.showerror("Error","Error de conexión")
   # valor=messagebox.askquestion("Atención","Desea eliminar una persona")
    
    valor=messagebox.askokcancel("Atención","Desea Salir de la aplicación")
    print(valor)


minombre=StringVar()
raiz.geometry("300x350")
####Menu
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu,width=300,height=300)
#####
menuBd=Menu(barraMenu,tearoff=0)
menuBorrar=Menu(barraMenu,tearoff=0)
menuCrud=Menu(barraMenu,tearoff=0)
menuAyuda=Menu(barraMenu,tearoff=0)

barraMenu.add_cascade(label="BBDD",menu=menuBd)
barraMenu.add_cascade(label="Borrar",menu=menuBorrar)
barraMenu.add_cascade(label="CRUD",menu=menuCrud)
barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)

#Submenus BBDDD

menuBd.add_command(label="Conectar")
menuBd.add_command(label="Salir")

#Submenus Borrar

menuBorrar.add_command(label="Borrar Campos")

#Submenus CRUD

menuCrud.add_command(label="Crear")
menuCrud.add_command(label="Leer")
menuCrud.add_command(label="Actualizar")
menuCrud.add_command(label="Eliminar")

#Submenus Ayuda

menuAyuda.add_command(label="Licencia",command=infoAdicional)
menuAyuda.add_command(label="Acerca de....")


#####Label titulo
labelTitulo=Label(raiz,text="Sistema de Administración de Personas")
labelTitulo.config(fg="BLUE",bd=2,font=("Comic Sans MS bold",12))
labelTitulo.pack()
            
miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()
#Labels
labelNombre=Label(miFrame,text="Nombre:")
labelNombre.grid(row=0,column=0,pady=5)

labelApellido=Label(miFrame,text="Apellido:")
labelApellido.grid(row=1,column=0,pady=5)

labelDireccion=Label(miFrame,text="Dirección:")
labelDireccion.grid(row=2,column=0,pady=5)

labelPass=Label(miFrame,text="Password:")
labelPass.grid(row=3,column=0,pady=5)

labelComentarios=Label(miFrame,text="Comentarios:")
labelComentarios.grid(row=4,column=0,pady=5)

#Entry campos de texto
nombre=Entry(miFrame,textvariable=minombre)
nombre.grid(row=0,column=1,pady=5)

apellido=Entry(miFrame)
apellido.grid(row=1,column=1,pady=5)

direccion=Entry(miFrame)
direccion.grid(row=2,column=1,pady=5)

parword=Entry(miFrame)
parword.grid(row=3,column=1,pady=5)
parword.config(show="*")

#Area de texto
comentario=Text(miFrame,width=15,height=5)
comentario.grid(row=4,column=1,pady=5)
#Boton
def codigoBoton():
    print(minombre.get())
    minombre.set("Veronica")
   
frame2=Frame()
frame2=Frame(raiz,width=1200,height=600)
frame2.pack()

botonCrear=Button(frame2,text="Crear",command=codigoBoton)
botonCrear.grid(row=0,column=0,padx=5,pady=5)

botonLeer=Button(frame2,text="Leer",command=codigoBoton)
botonLeer.grid(row=0,column=1,padx=5,pady=5)

botonActualizar=Button(frame2,text="Actualizar",command=codigoBoton)
botonActualizar.grid(row=0,column=2,padx=5,pady=5)

botonActualizar=Button(frame2,text="Eliminar",command=codigoBoton)
botonActualizar.grid(row=0,column=3,padx=5,pady=5)

raiz.mainloop()