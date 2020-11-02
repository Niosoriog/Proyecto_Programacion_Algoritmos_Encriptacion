import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

from vigener import main
from vernan import vernan
from solitario import solit
from cesar import cesar
from personalizado import perso

window = tk.Tk()
window.geometry('900x900')
window.config(bg = "#EA9A1D")

frame1 = tk.Frame(window)
frame1.pack()
frame1.config(bg="#EA9A1D") 
frame1.config(width=900,height=900)

label_titulo = tk.Label(frame1, text="PyCript")
label_titulo.config(fg="#fff", bg="#EA9A1D",font=("Helvetica", 20))
label_titulo.place(relx = 0.45, rely=0.1)

label_nombre = tk.Label(frame1,text="Escoja el método de encriptación")
label_nombre.config(fg="#fff", bg="#EA9A1D",font=("Helvetica", 20))
label_nombre.place(relx = 0.3, rely=0.2)
#-------------------------------------------VENTANA ALGORITMO VIGENER------------------------------------------------------
def vigenerWindow():
    newWindow = tk.Toplevel(window)
    newWindow.title("Vigener")
    frame1 = tk.Frame(newWindow)
    frame1.config(bg="#E01F1C")
    frame1.config(width="900", height="600")
    frame1.grid(row=0, column=0)

    label1 = tk.Label(frame1, text="Ingrese el mensaje: ")
    label1.config(fg="#fff", bg="#E01F1C",font=("Helvetica", 15))
    label1.grid(row=0, column=0)

    entry1 = tk.Entry(frame1, width=20)
    entry1.grid(row=0, column=1)

    label2 = tk.Label(frame1, text="El mensaje es: ")
    label2.config(fg="#fff", bg="#E01F1C",font=("Helvetica", 15))
    label2.grid(row=2, column=0)

    label3 = tk.Label(frame1, text="Ingrese la clave: ")
    label3.config(fg="#fff", bg="#E01F1C",font=("Helvetica", 15))
    label3.grid(row=0, column=2)

    entry2 = tk.Entry(frame1, width=20)
    entry2.grid(row=0,  column=3 )

    boton = tk.Button(frame1, text="Encriptar", command= lambda : vig(entry1.get(), entry2.get()))
    boton.grid(row=1 , column=1)

    def vig(mensaje, clave):
        men = main(mensaje+" ENCRYPT "+clave)
        txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
        txt.grid(column=1,row=2)
        txt.insert('1.0', men)

    label4 = tk.Label(frame1, text="Ingrese el mensaje encriptado: ")
    label4.config(fg="#fff", bg="#E01F1C",font=("Helvetica", 15))
    label4.grid(row=3, column=0)

    label5 = tk.Label(frame1, text="Ingrese la clave: ")
    label5.config(fg="#fff", bg="#E01F1C",font=("Helvetica", 15))
    label5.grid(row=3, column=2)


    label7 = tk.Label(frame1, text="El mensaje es: ")
    label7.config(fg="#fff", bg="#E01F1C",font=("Helvetica", 15))
    label7.grid(row=5, column=0)

    entry3 = tk.Entry(frame1, width=20)
    entry3.grid(row=3, column=1)

    entry4 = tk.Entry(frame1)
    entry4.grid(row=3,column=3)

    boton2 = tk.Button(frame1, text="Desencriptar", command= lambda : dec(entry3.get(), entry4.get()))
    boton2.grid(row=4, column=1)


    def dec(encriptado, clave):
        men = main(encriptado+" DECRYPT "+clave)
        txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
        txt.grid(column=1,row=5)
        txt.insert('1.0', men)
#-------------------------------------------FIN VENTANA ALGORITMO VIGENER------------------------------------------------------

#-------------------------------------------VENTANA ALGORITMO VERMAN-----------------------------------------------------------
def vermanWindow():
    newWindow = tk.Toplevel(window)
    newWindow.title("Vernan")
    newWindow.config(bg = "#EA9A1D")

    frame1 = tk.Frame(newWindow)
    frame1.config(bg="#1E96A2")
    frame1.config(width="800", height="600")
    frame1.grid(row=0, column=0)

    entry_mensaje = tk.Entry(frame1, width=16)
    entry_mensaje.grid(row=0, column=1)

    entry_clave = tk.Entry(frame1, width=16)
    entry_clave.grid(row=0, column=3)

    label_mensaje = tk.Label(frame1, text="Ingrese el mensaje a encriptar:",bd=1)
    label_mensaje.config(fg="#fff", bg="#1E96A2",font=("Helvetica", 10))
    label_mensaje.grid(row=0, column=0)

    label_clave = tk.Label(frame1, text="Ingrese la clave:",bd=1)
    label_clave.config(fg="#fff", bg="#1E96A2",font=("Helvetica", 10))
    label_clave.grid(row=0, column=2)

    label_mensaje_2 = tk.Label(frame1, text="Ingrese el mensaje para desencriptar: ")
    label_mensaje_2.config(fg="#fff", bg="#1E96A2",font=("Helvetica", 10))
    label_mensaje_2.grid(row=2, column=0)

    label_clave_2 = tk.Label(frame1, text="Ingrese la clave:",bd=1)
    label_clave_2.config(fg="#fff", bg="#1E96A2",font=("Helvetica", 10))
    label_clave_2.grid(row=2, column=2)

    mensaje_encriptado = tk.Entry(frame1, width=16)
    mensaje_encriptado.grid(row=2, column=1)

    entry_clave_2 = tk.Entry(frame1, width=16)
    entry_clave_2.grid(row=2, column=3)


    boton_encriptar = tk.Button(frame1, text="Encriptar", command= lambda: encript(entry_mensaje.get(), entry_clave.get()))
    boton_encriptar.grid(row=1,column=1)

    boton_desencriptar = tk.Button(frame1, text="Desencriptar", command= lambda:desencriptar(mensaje_encriptado.get(), entry_clave_2.get()))
    boton_desencriptar.grid(row=3, column=1)

    def encript(mensaje, clave):
        encriptado = vernan(mensaje, clave, "enc")
        txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
        txt.grid(column=2,row=1)
        txt.insert('1.0', encriptado)

    def desencriptar(mensaje,clave):
        desencriptado = vernan(mensaje, clave, "dec")
        txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
        txt.grid(column=2,row=3)
        txt.insert('1.0', desencriptado)



    window.mainloop() 


#-------------------------------------------FIN VENTANA ALGORITMO VERNAN---------------------------------------------------------------

#-------------------------------------------VENTANA ALGORITMO SOLITARIO-----------------------------------------------------------

def solitarioWindow():
    newWindow = tk.Toplevel(window)
    frame1 = tk.Frame(newWindow)
    frame1.config(bg="#0578EB")
    frame1.config(width="900", height="600")
    frame1.grid(row=0, column=0)

    label_mensaje = tk.Label(frame1, text="Ingrese el mensaje: ")
    label_mensaje.config(fg="#fff", bg="#0578EB",font=("Helvetica", 15))
    label_mensaje.grid(row=0, column=0)

    label_clave = tk.Label(frame1, text="Ingrese la clave: ")
    label_clave.config(fg="#fff", bg="#0578EB",font=("Helvetica", 15))
    label_clave.grid(row=0, column=2)


    entry_mensaje = tk.Entry(frame1)
    entry_mensaje.grid(row=0, column=1)

    entry_clave = tk.Entry(frame1)
    entry_clave.grid(row=0, column=3)

    label_mensaje_2 = tk.Label(frame1, text="Ingrese el mensaje para desencriptar: ")
    label_mensaje_2.config(fg="#fff", bg="#0578EB",font=("Helvetica", 15))
    label_mensaje_2.grid(row=2, column=0)

    lable_clave_2 = tk.Label(frame1, text="Ingrese la clave: ")
    lable_clave_2.config(fg="#fff", bg="#0578EB",font=("Helvetica", 15))
    lable_clave_2.grid(row=2, column=2)


    entry_mensaje_2 = tk.Entry(frame1)
    entry_mensaje_2.grid(row=2, column=1)

    entry_clave_2 = tk.Entry(frame1)
    entry_clave_2.grid(row=2, column=3)

    boton_enc = tk.Button(frame1, text="Encriptar", command= lambda : encriptar(entry_mensaje.get(), entry_clave.get()))
    boton_enc.grid(row=1, column=1)

    boton_dec = tk.Button(frame1, text="Desencriptar", command= lambda : desencriptar(entry_mensaje_2.get(), entry_clave_2.get()))
    boton_dec.grid(row=3, column=1)


    def encriptar(mensaje, clave):
        men = solit(mensaje, clave, "enc")
        txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
        txt.grid(column=2,row=1)
        txt.insert('1.0', men)


    def desencriptar(mensaje, clave):
        men = solit(mensaje, clave, "dec")
        txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
        txt.grid(column=2,row=3)
        txt.insert('1.0', men)

#-------------------------------------------FIN VENTANA ALGORITMO SOLITARIO---------------------------------------------------------------

#-------------------------------------------VENTANA ALGORITMO CESAR-----------------------------------------------------------
def cesarWindow():
    messagebox.showinfo('Ayuda metodo cesar', 'Ingrese unicamente caracteres contenidos en el abecedario')
    newWindow = tk.Toplevel(window)
    frame1 = tk.Frame(newWindow)
    frame1.config(bg="#135B0B")
    frame1.config(width="900", height="600")
    frame1.grid(row=0, column=0)

    label_mensaje = tk.Label(frame1,text="Ingrese el mensaje: ")
    label_mensaje.config(fg="#fff", bg="#135B0B",font=("Helvetica", 15))
    label_mensaje.grid(row=0, column=0)

    entry_mensaje = tk.Entry(frame1)
    entry_mensaje.grid(row=0, column=1)

    label_posicion = tk.Label(frame1,text="Digite cuantas posiciones lo desea rotar: ")
    label_posicion.config(fg="#fff", bg="#135B0B",font=("Helvetica", 15))
    label_posicion.grid(row=0, column=2)

    entry_posicion= tk.Entry(frame1)
    entry_posicion.grid(row=0, column=3)
    
    label_mensaje_2 = tk.Label(frame1,text="Digite el texto a desencriptar: ")
    label_mensaje_2.config(fg="#fff", bg="#135B0B",font=("Helvetica", 15))
    label_mensaje_2.grid(row=2, column=0)

    entry_mensaje_2 = tk.Entry(frame1)
    entry_mensaje_2.grid(row=2, column=1)

    label_posicion_2 = tk.Label(frame1,text="Digite cuantas posiciones lo desea rotar: ")
    label_posicion_2.config(fg="#fff", bg="#135B0B",font=("Helvetica", 15))
    label_posicion_2.grid(row=2, column=2)

    entry_posicion_2 = tk.Entry(frame1)
    entry_posicion_2.grid(row=2, column=3)   

    boton_enc = tk.Button(frame1, text="Encriptar", command = lambda : encriptar(entry_mensaje.get(), entry_posicion.get()))
    boton_enc.grid(row=1, column=1)

    boton_dec = tk.Button(frame1, text="Desencriptar",command = lambda : desencriptar(entry_mensaje_2.get(), entry_posicion_2.get()))
    boton_dec.grid(row=3, column=1)


    def encriptar(mensaje, posiciones):
        men = cesar(mensaje, posiciones, "enc")
        txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
        txt.grid(column=2,row=1)
        txt.insert('1.0', men)
    def desencriptar(mensaje, posiciones):
        men = cesar(mensaje, posiciones, "dec")
        txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
        txt.grid(column=2,row=3)
        txt.insert('1.0', men)
#-------------------------------------------FIN VENTANA ALGORITMO CESAR---------------------------------------------------------------

#-------------------------------------------VENTANA ALGORITMO PERSONALIZADO-----------------------------------------------------------

def personalizadoWindow():
    newWindow = tk.Toplevel(window)
    frame1 = tk.Frame(newWindow)
    frame1.config(bg="#627360")
    frame1.config(width="900", height="600")
    frame1.grid(row=0, column=0)

    label_mensaje = tk.Label(frame1,text="Ingrese el mensaje: ")
    label_mensaje.config(fg="#fff", bg="#627360",font=("Helvetica", 15))
    label_mensaje.grid(row=0, column=0)

    entry_mensaje = tk.Entry(frame1)
    entry_mensaje.grid(row=0, column=1)

    label_clave = tk.Label(frame1,text="Ingrese la clave: ")
    label_clave.config(fg="#fff", bg="#627360",font=("Helvetica", 15))
    label_clave.grid(row=0, column=2)

    entry_clave = tk.Entry(frame1)
    entry_clave.grid(row=0, column=3)

    label_mensaje_2 = tk.Label(frame1,text="Digite el texto a desencriptar: ")
    label_mensaje_2.config(fg="#fff", bg="#627360",font=("Helvetica", 15))
    label_mensaje_2.grid(row=2, column=0)

    entry_mensaje_2 = tk.Entry(frame1)
    entry_mensaje_2.grid(row=2, column=1)

    lable_clave_2 = tk.Label(frame1,text="Ingrese la clave: ")
    lable_clave_2.config(fg="#fff", bg="#627360",font=("Helvetica", 15))
    lable_clave_2.grid(row=2, column=2)

    entry_clave_2 = tk.Entry(frame1)
    entry_clave_2.grid(row=2, column=3)

    boton_enc = tk.Button(frame1, text="Encriptar", command = lambda : encriptar(entry_mensaje.get(), entry_clave.get()))
    boton_enc.grid(row=1, column=1)

    boton_dec = tk.Button(frame1, text="Desencriptar",command = lambda : desencriptar(entry_mensaje_2.get(), entry_clave_2.get()))
    boton_dec.grid(row=3, column=1)

    def encriptar(mensaje, clave):
        men = perso(mensaje, clave, "enc")
        #label_salida_enc.configure(text=''+men)
        txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
        txt.grid(column=2,row=1)
        txt.insert('1.0', men)

    def desencriptar(mensaje, clave):
        men = perso(mensaje, clave, "dec")
        txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
        txt.grid(column=2,row=3)
        txt.insert('1.0', men)
#-------------------------------------------FIN VENTANA ALGORITMO PERSONALIZADO---------------------------------------------------------------
boton_vigener = tk.Button(frame1, 
              text="Metodo Vigener", height=5, width=50, 
              command=vigenerWindow)
boton_vigener.place(relx = 0.32, rely=0.7)

boton_vernan = tk.Button(frame1, height=5, width=50, 
              text="Metodo Vernan",
              command=vermanWindow)
boton_vernan.place(relx = 0.32, rely=0.8)

boton_solitario = tk.Button(frame1,  height=5, width=50,
              text="Metodo Solitario",
              command=solitarioWindow)
boton_solitario.place(relx = 0.32, rely=0.5)


boton_cesar = tk.Button(frame1,  height=5, width=50,
              text="Metodo Cesar",
              command=cesarWindow)
boton_cesar.place(relx = 0.32, rely=0.4)

boton_personalizado= tk.Button(frame1,  height=5, width=50,
              text="Metodo P-I",
              command=personalizadoWindow)
boton_personalizado.place(relx = 0.32, rely=0.6)







window.mainloop()