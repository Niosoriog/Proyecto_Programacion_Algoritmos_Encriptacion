def igualar (cadena,clave):
    """
    igualar Esta funcion se encarga de completar la clave en dado caso que el tamaño de esta sea menor que la del mensaje.
    :param string cadena1: El texto o mensaje que el usuario desea encriptar/desencriptar.
    :param string clave: la clave que se igualara a la longitud del mensaje .
    :return: la cadena y la clave ya igualada.
    """
    tamano_texto = len(cadena)
    tamano_clave = len(clave)
    if tamano_texto == tamano_clave:
        return cadena,clave
    if tamano_texto > tamano_clave:
        op=tamano_texto-tamano_clave
        #con este for completa la clave para que quede del mismo tamaño con la cadena
        for i in range(op):
            clave=clave+ clave[i]
    else:
        op=tamano_clave-tamano_texto
        cadena=cadena+(" "*op)
    return cadena,clave
# le llegan un caracter y este retorna la posicion donde se encuentrar en la cadena
def buscar (c):
    """
    buscar Esta funcion se encarga de buscar en un string predefinido la posicion en la que se encuentra cierto caracter.
    :param string c: El caracter del cual deseamos saber la posicion en el string predefinido.
    :return: un valor int que representa la posicion donde se encuentra ese caracter.
    """
    abc = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.+-\*?¡¿!<>=)(/&%$#"_;:1234567890[]{^}áéíóúÁÉÍÓÚäëïöüÄËÏÖÜ@|°'
    for i in range(len(abc)):
        if c == abc[i]:
            return(i)
#le llega un numero y retornar el valor en esa posicion de la cadena abc
def entregar(c):
    """
    entregar Esta funcion se encarga de buscar que caracter esta en una posicion x de la cadena abc.
    :param int n: El caracter del cual deseamos saber la posicion en el string predefinido.
    :return: un valor int que representa la posicion donde se encuentra ese caracter.
    """
    abc = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.+-\*?¡¿!<>=)(/&%$#"_;:1234567890[]{^}áéíóúÁÉÍÓÚäëïöüÄËÏÖÜ@|°'
    return abc[c]

# algoritmo de encriptacion
def encriptar_Solitario(cadena,clave):
    """
    Encriptar_Solitario esta funcion se encarga de hacer la encriptacion en base al algorimo Solitario
    :param string cadena1: El texto o mensaje que se desea encriptar.
    :param string clave: la clave con la cual es mensaje se sumara para generar el mensaje encriptado.
    :return:   mensaje encriptado.
    """
    cadenaaux=""
    for i in range(len(cadena)):
        c1= buscar(cadena[i])
        z1= buscar(clave[i])
        op = c1+z1
        if op > 114:
            op = op%114
        pos=entregar(op)
        cadenaaux+= pos
    return cadenaaux
# Algoritmo de desencriptacion
def desencriptar_Solitario(cadena,clave):
    """
    Dncriptar_Solitario esta funcion se encarga de hacer la desencriptacion en base al algorimo Solitario
    :param string cadena1: El texto o mensaje que se desea desencriptar.
    :param string clave: la clave con la cual es mensaje se restara para generar el mensaje desencriptado.
    :return:  mensaje desencriptado.
    """
    cadenaaux=""
    for i in range(len(cadena)):
        c1= buscar(cadena[i])
        z1= buscar(clave[i])
        op = c1-z1
        if op < 0:
            op = 115+op
        pos=entregar(op)
        cadenaaux+= pos
    return cadenaaux
    
def solit(mensaje, clave, opcion):
    
    mensaje,clave=igualar(mensaje,clave)
    cadena_salida = ""
    if opcion == "enc":
        cadena_salida = encriptar_Solitario(mensaje,clave)
    elif opcion == "dec":
        cadena_salida =  desencriptar_Solitario(mensaje,clave)
    return cadena_salida    
