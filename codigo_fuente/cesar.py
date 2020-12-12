import Archivos
def Encriptar_Cesar (cadena1,mov,usuario):
    """
    Encriptar_Cesar esta funcion se encarga de hacer la encriptacion en base al algorimo Cesar
    :param string cadena1: El texto o mensaje que se desea encriptar.
    :param int mov: El numero de movimientos que desea que se mueva cada elemento de la cadena.
    :return: mensaje encriptado.
    """
    cadenaaux=""
    if mov >25 or mov < 0:
        mov=mov%26
    for i in range(len(cadena1)):
        val=ord(cadena1[i])
        if cadena1[i] == " ":
            cadenaaux = cadenaaux + " "
        elif val>= 65 and val <=90 :
            val=val-65+mov
            if val < 0 :
                val=26+val
            if val > 25 :
                val = val%26
            val=val+65
            cadenaaux=cadenaaux+chr(val)
        elif val>= 97 and val <=122 :
            val = val - 97 + mov
            if val < 0 :
                val=26+val
            if val > 25:
                val = val % 26

            val = val + 97
            cadenaaux = cadenaaux + chr(val)
    Archivos.arch_historial(cadena1,mov,cadenaaux,usuario)
    if len(cadenaaux) > 40 :
        Archivos.arch_texto(cadenaaux,usuario)
        cadenaaux = "Debido a la longitud del mensaje se creo un archivo en la carpeta Texto."
    return cadenaaux
def Desencriptar_Cesar(cadena1,mov,usuario):
    """
    Desencriptar_Cesar esta funcion se encarga de hacer la desencriptacion en base al algorimo Cesar
    :param string cadena1: El texto o mensaje que se desea desencriptar.
    :param int mov: El numero de movimientos que desea que se mueva cada elemento de la cadena.
    :return:  mensaje encriptado.
    """
    cadena2=""
    if mov >25 or mov < 0 :
        mov=mov%26
    for i in range(len(cadena1)):
        val = ord(cadena1[i])
        if cadena1[i] == " ":
            cadena2 = cadena2 + " "
        elif val>= 65 and val <=90 :
            val=val-65-mov
            if val < 0 :
                val=26+val
            if val > 25 :
                val = val%26

            val=val+65
            cadena2=cadena2+chr(val)
        elif val>= 97 and val <=122 :
            val = val - 97 - mov
            if val < 0 :
                val=26+val
            if val > 25:
                val = val % 26
            val = val + 97
            cadena2 = cadena2 + chr(val)
    if len(cadena2) > 40:
        Archivos.arch_texto(cadena2,usuario)
        cadena2 = "Debido a la longitud del mensaje se creo un archivo en la carpeta Texto."
    return cadena2

def cesar(cad, movere, opcion,usuario):    
    pos = int(movere)
    cadena = ""
    if opcion == "enc":
        cadena =  Encriptar_Cesar(cad,pos,usuario)
    else:    
        cadena = Desencriptar_Cesar(cad,pos,usuario)
    return cadena
      