from tkinter import *
from tkinter import messagebox
 #creamos una clase
class App():
   #Metodo es construcutor
    def _init_(self):
        #Creamos el objeto de tipo Tkinter
        ventana = Tk()
        ventana.title("HITO2 COMPLEJIDAD ALGORITMICA")
        ventana.geometry("800x800")
        ventana.configure(bg='silver')
        #widgets
        
        self.label1=Label(ventana,text="SISTEMA DE BÚSQUEDA DE RUTAS EFICIENTES")
        self.label1.place(x=150,y=5)
        
        self.label1=Label(ventana,text="Usuario")
        self.label1.place(x=40,y=40)
        
        self.label1=Label(ventana,text="Clave")
        self.label1.place(x=40,y=75)
        
        self.text1=Entry(ventana,bg='white')
        self.text1.place(x=105,y=40)
        

        self.text2=Entry(ventana,bg='white')
        self.text2.place(x=105,y=75)
        
        
        # Boton
        self.bt1=Button(ventana,text="Ingresar",command=self.mensaje)
        self.bt1.place(x=150,y=105)
        ventana.mainloop()
    def mensaje(self):
        #print("Bievenidos al Hito2 de Trabajo de Complejidad Algoritmica")
        
        messagebox.showinfo(message="Bienvenidos al "+self.text1.get(),title="Ejemplo")
    def imagen(self):
       img= tkinter.PhotoImage(file='logoUpc.png')
       lbl_img=tkinter.Label(ventana,image=img)
       img.place(x=90,y=200)
       lbl_img.pack()
     
     
        
    # Programa principal
Objeto_ventana=App()