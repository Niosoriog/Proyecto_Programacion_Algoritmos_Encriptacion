import tkinter as tk
from tkinter import ttk, PhotoImage, Canvas, Toplevel, messagebox
from PIL import ImageTk, Image
import tkinter.font as font
import sqlite3

from menu import initWindow

main = tk.Tk()

fondo = Canvas(main, height=600, width=800)
img_fondo = ImageTk.PhotoImage(Image.open('recursor/fondo.jpg'))
fondo.create_image(400,300,image=img_fondo)
fondo.pack()

label_titulo = tk.Label(fondo, text='PyCrypt')
label_titulo.config(font=('Helvetica',44), fg='red', bg='black')
label_titulo.place(relx=0.36, rely=0.1)

myFont = font.Font(family='Helvetica', size=20, weight='bold') 
myFont2 = font.Font(family='Helvetica', size=10, weight='bold')
def entrar():
    new = Toplevel(main)
    canvas = Canvas(new, height= 500, width=700)
    canvas.pack()
    img_bg = ImageTk.PhotoImage(Image.open('recursor/regis.png'))
    canvas.create_image(350, 250, image=img_bg)
    canvas.image = img_bg
    entry_usuario = tk.Entry(new)
    entry_usuario.place(relx=0.43, rely=0.38)
    entry_clave = tk.Entry(new, show='*')
    entry_clave.place(relx=0.43, rely=0.48)
    def log(a,b):
        conn = sqlite3.connect('archivos/base/database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM registro WHERE usuario="+"'"+a+"'"+" AND clave="+"'"+b+"'")
        data = c.fetchall()
        if len(data) == 0:
            messagebox.showinfo('Error', 'Usuario o contraseña incorrectos')
        else:
            main.destroy()
            initWindow(a)
        c.close()
        conn.close()
    label_usuario = tk.Label(new, text='Ingrese el usuario')
    label_usuario.config(bg='turquoise', fg='black')
    label_usuario['font'] = myFont2
    label_usuario.place(relx=0.43, rely=0.33)

    label_clave = tk.Label(new, text='Ingrese la clave')
    label_clave.config(bg='turquoise', fg='black')
    label_clave['font'] = myFont2
    label_clave.place(relx=0.44, rely=0.43)

    boton_log = tk.Button(new, text='Ingresar', 
                borderwidth=0, bg='turquoise',fg='white',
                height = 1, width = 11, 
                activebackground='white', activeforeground='turquoise',
                command=lambda :log(entry_usuario.get(), entry_clave.get()))
    boton_log['font'] = myFont
    boton_log.place(relx=0.38, rely=0.58)
    

def registrarse():
    new = Toplevel(main)
    canvas = Canvas(new, height= 500, width=700)
    canvas.pack()
    img_bg = ImageTk.PhotoImage(Image.open('recursor/regis.png'))
    canvas.create_image(350, 250, image=img_bg)
    canvas.image = img_bg
    entry_usuario = tk.Entry(new)
    entry_usuario.place(relx=0.43, rely=0.38)
    entry_clave = tk.Entry(new, show='*')
    entry_clave.place(relx=0.43, rely=0.48)
    def reg(a,b):
        conn = sqlite3.connect('archivos/base/database.db')
        c = conn.cursor()
        c.execute("INSERT INTO registro (usuario, clave) VALUES(?,?)",
        (a,b))
        conn.commit()
        c.close()
        conn.close()
    label_usuario = tk.Label(new, text='Ingrese el usuario')
    label_usuario.config(bg='turquoise', fg='black')
    label_usuario['font'] = myFont2
    label_usuario.place(relx=0.43, rely=0.33)

    label_clave = tk.Label(new, text='Ingrese la clave')
    label_clave.config(bg='turquoise', fg='black')
    label_clave['font'] = myFont2
    label_clave.place(relx=0.44, rely=0.43)
    boton_regis = tk.Button(new, text='Registrarse', 
                    borderwidth=0, bg='turquoise',fg='white',
                    height = 1, width = 11, 
                    activebackground='white', activeforeground='turquoise',
                    command= lambda:reg(entry_usuario.get(), entry_clave.get()))
    boton_regis['font'] = myFont
    boton_regis.place(relx=0.38, rely=0.58)


 
boton_login = tk.Button(main, text='Iniciar sesión',
                        borderwidth=0, bg='black',fg='red',
                        height = 1, width = 15, 
                        activebackground='red', activeforeground='black',
                        command=entrar)
boton_login['font'] = myFont
boton_login.place(relx= 0.33, rely= 0.35)

boton_reg = tk.Button(main, text='Registrarse',
                        borderwidth=0, bg='red',fg='black',
                        height = 1, width = 15, 
                        activebackground='black', activeforeground='red',
                        command=registrarse)
boton_reg['font'] = myFont
boton_reg.place(relx= 0.33, rely= 0.45)

main.mainloop()
