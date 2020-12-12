import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, PhotoImage, filedialog, Canvas
from tkinter.filedialog import askopenfilename
import tkinter.font as font
from PIL import ImageTk, Image
import cv2 
from cv2 import cv2
import numpy as np

from vigener import main
from vernan import vernan
from solitario import solit
from cesar import cesar
from personalizado import perso
from image_hide import hide_image 
from image_show import show_image
from rsa import rsa
from scrapping import scrapp


def initWindow(usuario):
    window = tk.Tk()
    window.geometry('900x900')

    fondo = Canvas(window, height=900, width=900)
    img_fondo = ImageTk.PhotoImage(Image.open('recursor/fondo_menu.jpg'))
    fondo.create_image(450,450,image=img_fondo)
    fondo.pack()

    label_titulo = tk.Label(window, text="PyCript")
    label_titulo.config(font=('Helvetica',44), fg='red', bg='black')
    label_titulo.place(relx = 0.40, rely=0.05)

    label_nombre = tk.Label(window,text="Escoja el método de encriptación")
    label_nombre.config(font=('Helvetica',22), fg='red', bg='black')
    label_nombre.place(relx = 0.27, rely=0.15)
    myFont = font.Font(family='Helvetica', size=20, weight='bold')
    myFont2 = font.Font(family='Helvetica', size=10, weight='bold')
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
            men = main(mensaje+" ENCRYPT "+clave,usuario)
            txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
            txt.grid(column=1,row=2)
            txt.insert('1.0', men[0])

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
            men = main(encriptado+" DECRYPT "+clave, usuario)
            txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
            txt.grid(column=1,row=5)
            txt.insert('1.0', men[0])
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
            encriptado = vernan(mensaje, clave, "enc",usuario)
            txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
            txt.grid(column=2,row=1)
            txt.insert('1.0', encriptado)

        def desencriptar(mensaje,clave):
            desencriptado = vernan(mensaje, clave, "dec", usuario)
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
            men = solit(mensaje, clave, "enc", usuario)
            txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
            txt.grid(column=2,row=1)
            txt.insert('1.0', men)


        def desencriptar(mensaje, clave):
            men = solit(mensaje, clave, "dec", usuario)
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
            men = cesar(mensaje, posiciones, "enc",usuario)
            txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
            txt.grid(column=2,row=1)
            txt.insert('1.0', men)
        def desencriptar(mensaje, posiciones):
            men = cesar(mensaje, posiciones, "dec",usuario)
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
            txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
            txt.grid(column=2,row=1)
            txt.insert('1.0', men)

        def desencriptar(mensaje, clave):
            men = perso(mensaje, clave, "dec")
            txt = scrolledtext.ScrolledText(frame1,width=15,height=0,font=("Helvetica", 15))
            txt.grid(column=2,row=3)
            txt.insert('1.0', men)
    #-------------------------------------------FIN VENTANA ALGORITMO PERSONALIZADO---------------------------------------------------------------
    
    #-------------------------------------------VENTANA ALGORITMO IMAGENES-----------------------------------------------------------
    def images_window():
        root = tk.Toplevel(window)    
        def showImage():
            filename = askopenfilename(filetypes=(("png file", "*.png"), ("jpg file", "*.jpg"), ("All files", "*.*"),))
            entry.insert(0, filename)
            im = Image.open(filename)
            image_tk1 = ImageTk.PhotoImage(im)
            lbl1 = tk.Label(c, image=image_tk1)
            lbl1.grid(column=0, row=1)
            lbl1.image=image_tk1

        def showImage2():
            filename2 = askopenfilename(filetypes=(("png file", "*.png"), ("jpg file", "*.jpg"), ("All files", "*.*"),))
            entry_2.insert(0, filename2)
            im2 = Image.open(filename2)
            image_tk2 = ImageTk.PhotoImage(im2)
            label2 = tk.Label(c, image=image_tk2)
            label2.grid(column=1, row=1)
            label2.image=image_tk2
                    
        def encriptar(a,b):
            e = str(a)
            d = str(b)
            rgb_values = hide_image(e,d)
            red = rgb_values[0]
            blue = rgb_values[1]
            green = rgb_values[2] 
            img = cv2.imread(e)
            for x in range(300):
                    for y in range(300):
                            img[x,y] = (red[x][y], green[x][y], blue[x][y])
            edge = Image.fromarray(img)
            tk_edge = ImageTk.PhotoImage(edge)
            label = tk.Label(c, image=tk_edge)
            label.grid(column=0, row=4)
            label.image=tk_edge
            filename = filedialog.asksaveasfile(mode='wb', defaultextension=".png")
            if not filename:
                    return
            edge.save(filename)
        def desencriptar():
            filename = askopenfilename(filetypes=(("png file", "*.png"), ("jpg file", "*.jpg"), ("All files", "*.*"),))
            rgb_values = show_image(filename)
            red = rgb_values[0]
            blue = rgb_values[1]
            green = rgb_values[2]
            img = cv2.imread(filename)
            for x in range(300):
                    for y in range(300):
                            img[x,y] = (red[x][y], green[x][y],blue[x][y] )
            edge = Image.fromarray(img)
            tk_edge = ImageTk.PhotoImage(edge)
            label1 = tk.Label(c, image=tk_edge)
            label1.grid(column=1, row=4)
            label1.image=tk_edge
            filename = filedialog.asksaveasfile(mode='wb', defaultextension=".png")
            if not filename:
                    return
            edge.save(filename)
        root.geometry('500x500')
        root.config(bg='#43EFEF')
        c = tk.Frame(root)
        c.config(bg='#43EFEF')
        c.grid(column=0, row=0)

        boton_subir_1 = tk.Button(c, text="Cargar imagen para mostrar", command=showImage)
        boton_subir_1.grid(column=0, row=0)

        boton_subir_2 = tk.Button(c, text="Cargar imagen para esconder", command=showImage2)
        boton_subir_2.grid(column=1, row=0)

        entry = tk.Entry(c)
        entry.grid(column=0, row=2)

        entry_2 = tk.Entry(c)
        entry_2.grid(column=1, row=2)

        boton_encriptar = tk.Button(c, text="Encriptar y Guardar", command=lambda : encriptar(entry.get(), entry_2.get()))
        boton_encriptar.grid(column=0, row=3)

        boton_desencriptar = tk.Button(c,text= "Desencriptar", command=lambda : desencriptar())
        boton_desencriptar.grid(column=0, row=300)
        root.mainloop()
    #-------------------------------------------FIN VENTANA ALGORITMO IMAGENES---------------------------------------------------------------

    def rsa_window():
        new = tk.Toplevel()
        new.geometry('500x500')
        new.config(bg='#224FF4')
      
        label_mensaje = tk.Label(new,text='Ingrese el mensaje ')
        label_mensaje.config(bg='#224FF4')
        label_mensaje['font'] = myFont2
        label_mensaje.place(relx=0.6, rely=0.15)

        label_clave = tk.Label(new,text='Ingrese la clave ')
        label_clave.config(bg='#224FF4')
        label_clave['font'] = myFont2
        label_clave.place(relx=0.6, rely=0.25)
        
        entry_mensaje = tk.Entry(new)
        entry_mensaje.place(relx=0.6, rely=0.2)

        entry_clave = tk.Entry(new)
        entry_clave.place(relx=0.6, rely=0.3)

        def generar_claves():
            res = rsa(None, None, 1, None,usuario)
            txt2 = scrolledtext.ScrolledText(new,width=20,height=0,font=("Helvetica", 15))
            txt2.place(relx=0.05, rely=0.2)
            txt2.insert('1.0','Clave Pública: '+res[0]+'\n'+'Clave Privada: '+res[1])
        
        def encriptar(men,cla):
            res = rsa(men, cla, 0, 'enc',usuario)
            txt.insert('1.0',res)
        def desencriptar(men, cla):
            res = rsa(men, cla, 0, 'des',usuario)
            txt.delete('1.0', tk.END)
            txt.insert('1.0',res)

        txt = scrolledtext.ScrolledText(new,width=20,height=20,font=("Helvetica", 12))
        txt.place(relx=0.45, rely=0.5)

        boton_enc = tk.Button(new, text='Encriptar', command= lambda:encriptar(entry_mensaje.get(), entry_clave.get()))
        boton_enc.place(relx=0.55, rely=0.4)

        boton_des = tk.Button(new, text='Desencriptar', command= lambda:desencriptar(entry_mensaje.get(), entry_clave.get()))
        boton_des.place(relx=0.7, rely=0.4)

        boton_claves = tk.Button(new, text='Generar Claves', command= lambda: generar_claves())
        boton_claves.place(relx=0.1, rely=0.1)

    def scrapp_window():
        new = tk.Toplevel(window)
        new.geometry('600x600')
        new.config(bg='dodger blue')

        label_ejemplo = tk.Label(new,text='Informacion de los algoritmos')
        label_ejemplo.config(bg='dodger blue')
        label_ejemplo['font'] = myFont
        label_ejemplo.place(relx=0.20, rely=0.05)
        def encriptar(metodo):
            res = scrapp()
            if metodo=='vig':
                messaage.delete('1.0', tk.END)
                messaage.insert('1.0',res[0])
            elif metodo=='ver':
                messaage.delete('1.0', tk.END)
                messaage.insert('1.0',res[1]) 
            elif metodo=='ces':
                messaage.delete('1.0', tk.END)
                messaage.insert('1.0',res[2]) 
            else:
                messaage.delete('1.0', tk.END)
                messaage.insert('1.0',res[3])           
        boton_vig = tk.Button(new, text='Metodo Vigener', 
                            height=1, width=15, 
                            borderwidth=0, bg='white',fg='dodger blue',
                            command=lambda : encriptar('vig'))
        boton_vig.place(relx = 0.05, rely=0.13)
        boton_vig['font'] = font.Font(family='Helvetica', size=10, weight='bold')

        boton_ver = tk.Button(new, text='Metodo Vernam', 
                            height=1, width=15, 
                            borderwidth=0, bg='white',fg='dodger blue',
                            command=lambda : encriptar('ver'))
        boton_ver.place(relx = 0.3, rely=0.13)
        boton_ver['font'] = font.Font(family='Helvetica', size=10, weight='bold')

        boton_ces = tk.Button(new, text='Metodo Cesar', 
                            height=1, width=15, 
                            borderwidth=0, bg='white',fg='dodger blue',
                            command=lambda : encriptar('ces'))
        boton_ces.place(relx = 0.55, rely=0.13)
        boton_ces['font'] = font.Font(family='Helvetica', size=10, weight='bold')

        boton_sol = tk.Button(new, text='Metodo Solitario', 
                            height=1, width=15, 
                            borderwidth=0, bg='white',fg='dodger blue',
                            command=lambda : encriptar('sol'))
        boton_sol.place(relx = 0.78, rely=0.13)
        boton_sol['font'] = font.Font(family='Helvetica', size=10, weight='bold')
        
        messaage = scrolledtext.ScrolledText(new,width=48,height=20,font=("Helvetica", 15))
        messaage.place(relx = 0.05, rely=0.2)
    def historial():
        new = tk.Toplevel(window)
        new.geometry('600x600')
        new.config(bg='dodger blue')

        label_titulo = tk.Label(new,text='Historial de mensajes')
        label_titulo.config(bg='dodger blue')
        label_titulo['font'] = myFont
        label_titulo.place(relx=0.25, rely=0.05)       

        def mostrar():
            ruta ="archivos/historial/{}.txt".format(usuario)
            u=open(ruta,"r")
            url=u.read()
            messaage.delete('1.0', tk.END)
            messaage.insert('1.0',url)
            u.close
        def mensajes():
            ruta ="archivos/Texto/{}.txt".format(usuario)
            u=open(ruta,"r")
            url=u.read()
            messaage.delete('1.0', tk.END)
            messaage.insert('1.0',url)
            u.close

        boton_his = tk.Button(new, text='Ver mensajes',height=1, width=15, 
                        borderwidth=0, bg='white',fg='dodger blue',
                        command=lambda : mensajes())
        boton_his.place(relx = 0.28, rely=0.15)
        boton_his['font'] = font.Font(family='Helvetica', size=10, weight='bold')
        
        boton_his = tk.Button(new, text='Mostrar Historial',height=1, width=15, 
                        borderwidth=0, bg='white',fg='dodger blue',
                        command=lambda : mostrar())
        boton_his.place(relx = 0.52, rely=0.15)
        boton_his['font'] = font.Font(family='Helvetica', size=10, weight='bold')

        messaage = scrolledtext.ScrolledText(new,width=48,height=20,font=("Helvetica", 15))
        messaage.place(relx = 0.05, rely=0.2)
     

    boton_vigener = tk.Button(window, 
                text="Metodo Vigener", height=2, width=20, 
                borderwidth=0, bg='red3',fg='white',
                command=vigenerWindow)
    boton_vigener['font'] = myFont
    boton_vigener.place(relx = 0.32, rely=0.5)

    boton_vernan = tk.Button(window, height=2, width=20, 
                borderwidth=0, bg='red3',fg='white',
                text="Metodo Vernan",
                command=vermanWindow)
    boton_vernan['font'] = myFont
    boton_vernan.place(relx = 0.32, rely=0.6)

    boton_solitario = tk.Button(window,  height=2, width=20, 
                borderwidth=0, bg='red3',fg='white',
                text="Metodo Solitario",
                command=solitarioWindow)
    boton_solitario['font'] = myFont
    boton_solitario.place(relx = 0.32, rely=0.3)


    boton_cesar = tk.Button(window,  height=2, width=20,
                borderwidth=0, bg='red3',fg='white',
                text="Metodo Cesar",
                command=cesarWindow)
    boton_cesar['font'] = myFont
    boton_cesar.place(relx = 0.32, rely=0.2)

    boton_personalizado= tk.Button(window,  height=2, width=20,
                borderwidth=0, bg='red3',fg='white',
                text="Metodo P-I",
                command=personalizadoWindow)
    boton_personalizado['font'] = myFont
    boton_personalizado.place(relx = 0.32, rely=0.4)

    boton_imagenes = tk.Button(window, height=2, width=20,
                borderwidth=0, bg='red3',fg='white',
                text="Encriptar imagenes",
                command=images_window)
    boton_imagenes['font'] = myFont
    boton_imagenes.place(relx = 0.32, rely=0.7)

    boton_rsa = tk.Button(window, height=2, width=20,
                borderwidth=0, bg='red3',fg='white',
                text="Metodo RSA",
                command=rsa_window)
    boton_rsa['font'] = myFont
    boton_rsa.place(relx = 0.32, rely=0.8)


    boton_ayuda = tk.Button(window, height=2, width=5,
                borderwidth=0, bg='dodger blue',fg='white',
                text="Info",
                command=scrapp_window)
    boton_ayuda['font'] = font.Font(family='Helvetica', size=15, weight='bold')
    boton_ayuda.place(relx = 0.12, rely=0.82)

    boton_historial = tk.Button(window, height=2, width=7,
                borderwidth=0, bg='dodger blue',fg='white',
                text="Historial",
                command=historial)
    boton_historial['font'] = font.Font(family='Helvetica', size=15, weight='bold')
    boton_historial.place(relx = 0.83, rely=0.82)

    window.mainloop()





