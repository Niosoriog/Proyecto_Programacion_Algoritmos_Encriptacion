from datetime import datetime
#  Escribe en el historial el mensaje 
def  arch_historial (m_inicial,clave,m_encriptado,usuario):
    """
    Guardar el mensaje inicial, la clave y el mensaje encriptado en un archivo con el nombre del usuario en forma de historial.

    :param string m_inicial: Es el mensaje que ingresa el usuario a encriptar.
    :param string clave: Es el mensaje que corresponde a la clave y servira para encriptar el mensaje. 
    :param string m_encriptado: Es el mensaje encriptado.
    :param string usuario: Es el nombre del usuario con el cual se creara el archivo en la carpeta historial.
    """
    now = datetime.now()
    hora_local = now.strftime("%m/%d/%Y, %H:%M:%S") 
    ruta = "archivos/historial/{}.txt".format(usuario)
    historial = open(ruta,"a+")
    historial.write("Fecha: "+hora_local)
    historial.write("\n")
    historial.write("mensaje original: "+ str(m_inicial))
    historial.write("\n")
    historial.write("clave: "+ str(clave))
    historial.write("\n")
    historial.write("mensaje encriptado: "+m_encriptado)
    historial.write("\n\n")
    historial.close
# si el mensaje tiene mas de 40 caracteres lo guarda en texto
def arch_texto(msg_encriptado,usuario):
    """
    Guarda un mensaje, en este caso el mensaje encriptado/desencriptado  si su longitud es mayor a 40 caracteres
    con el fin de que se vea de una manera mas entendible en el programa.
 
    :param string m_encriptado: Es el mensaje encriptado/desencriptado a mostrar en el archivo.
    :param string usuario: Es el nombre del usuario con el cual se creara el archivo en la carpeta Texto.
    """
    ubicacion_historial = "archivos/Texto/{}.txt".format(usuario)
    arch_histo = open(ubicacion_historial,"w+")
    #escribimos la hora local
    now = datetime.now()
    hora_local = now.strftime("%m/%d/%Y, %H:%M:%S") 
    arch_histo.write("Fecha: "+hora_local)
    arch_histo.write("\n")
    # escribe el mensaje 
    arch_histo.write("Mensaje :"+str(msg_encriptado))
    arch_histo.write("\n")
    arch_histo.close

# historial de las llaves del algoritmo RSA 
def arc_histo_rsa_llaves (clave_publica,clave_privada,usuario):
    """
    Guarda las llaves que se genenra en el algorimo asimetrico, en este caso en el algoritmo Rsa

    :param string clave_publica: Es la clave publica que genera el algoritmo RSA y que se guardara en el historial.
    :param string clave_privada: Es  la clave privada que genera el algoritmo RSA y que se guardara en el historial.
    :param string usuario: Es el nombre del usuario con el cual se creara el archivo en la carpeta historial.
    """
    now = datetime.now()
    hora_local = now.strftime("%m/%d/%Y, %H:%M:%S") 
    ruta = "archivos/historial/{}.txt".format(usuario)
    historial = open(ruta,"a+")
    historial.write("Fecha: "+hora_local)
    historial.write("\n")
    historial.write("Clave Publica: "+clave_publica)
    historial.write("\n")
    historial.write("Clave Privada: "+clave_privada)
    historial.write("\n")
    historial.close