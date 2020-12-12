import Archivos
def matroz():
    """
    Generacion de matriz para el mensaje y la clave
    :param tupla abc: caracteres que puede contener
    :param abc.sort: recorre y organiza abc
    :param matriz: lista vacia
    :param for: añadir elementos de abc a matriz
    :return matriz | abc 
    """

    abc = ["+","á","é","í","ó","ú","ü","@","'","-","*","=","?","¿","/","(",'"',")","!","¡",".",",",":",";","_","{","}","[","]","<",">","#","$","%","&","A","B","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","C","v","w","x","y","z","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]
    abc.sort()
    matriz = []

    for i in range(len(abc)):
        matriz.append(abc[i:]+abc[:i])

    return matriz, abc

# Encriptacion

def enc(m,y, matriz, abc):
    """ 
    Encriptacion del mensaje segun la matriz
    :param string enc: string vacio
    :param for: caracteres del mensaje (m)
    :param fila: busqueda posicion en fila de m en posicion i
    :param columna: busqueda posicion en columna de y(clave) en posicion i
    :param string enc: string concatenado por matriz (fila)(columna)
    :param else: string enc concatenado por espacio
    :return enc
    """
    enc = ""
    for i in range(len(m)):
        if m[i] != " ":            
            fila = abc.index(m[i])
            columna = abc.index(y[i])
            enc += matriz[fila][columna]
        else:
            enc += " "
    return(enc)

# Desencriptar

def dec(enc,y, matriz, abc):
    """ 
    Desencriptacion del mensaje segun la matriz
    :param string m: string mensaje vacio
    :param for: caracteres del mensaje encriptado (enc)
    :param columna: busqueda de caracteres en fila de matriz, enc en posicion i
    :param m: string concatenado por abc(columna)
    :param else: string m concatenado por un espacio
    :return m
    """
    m = ""
    for i in range(len(enc)):
        if enc[i] != " ":
            fila = abc.index(y[i])
            columna = matriz[fila].index(enc[i])
            m += abc[columna]
        else:
            m += " "
    return(m)

    # Cambios en la cadena (' ')

# Transformacion del mensaje, remover espacios y revertir

def transformacion(entrada, matriz, abc):
    """
    Transformacion de la cadena
    :param string espacio: caracter japones de reemplazo
    :param entrada: reemplazo de los espacios en por caracter de reemplazo
    :param espacio: remover caracter de reemplazo
    :param condicion espacio[0]: remover caracter de espacio
    :param condicion espacio[-1]: actualiza los caracteres de espacio
    :param remove: remueve caracter de espacio " "
    :param string entrada: une mediante un string vacio el caracter de espacio
    :param return entrada
    """
    espacio =["あ"]
    for x in entrada:
        if not((espacio[(len(espacio))-1] == " ")and(x == " ")):
            espacio.append(x)
    espacio.remove("あ")
    if espacio[0] == " ":
        espacio.remove(" ")
    if espacio[-1] == " ":
        espacio.reverse()
        espacio.remove(" ")
        espacio.reverse()
    entrada = "".join(espacio)
    return entrada
    
        
# Definicion de encriptacion o desencripcion palabras ( ENCRYPT o DECRYPT)

def que_quieres(entrada, matriz, abc):
    """ 
    Que desea el usuario encriptar o densencriptar
    :param E: variable que toma un valor si la palabra clave es ENCRYPT
    :param D: variable que toma un valor si la palabra clave es DECRYPT
    :param string claveReal: caracter vacio
    :param string llave: caracter vacio
    :param condicion D != -1: llave tendrá el string entrada en la posicion D+8 reemplazando los espacios
    :param claveReal: string entrada desde el inicio hasta el caracter D -1 
    :param condicion E != -1: llave tendrá el string entrada en la posicion E+8 reemplazando los espacios
    :param claveReal: string entrada desde el inicio hasta el caracter E -1 
    :return llave | claveReal | E | D
    """
    E = entrada.find("ENCRYPT")
    D = entrada.find("DECRYPT")
    claveReal = ""
    llave = ""
    if D != -1:
        #desencripta
        llave = entrada[D+8:].replace(' ','')
        claveReal = entrada[:D-1]
    elif E != -1:
        #encripta
        llave = entrada[E+8:].replace(' ','')
        claveReal = entrada[:E-1]
    return llave, claveReal, E, D

    

#Cifrando a la Vigenère

def Vigenere(llave,claveReal, E, D, matriz, abc):
    """ 
    Cifrando a la vigeneré
    :param list mensaje: lista vacia
    :param string clave: string claveReal y reemplazando los espacios por caracteres vacios
    :param int n: valor inicial 0
    :param int illave: longitud de la llave - 1
    :param int iclave: longitud de la clave - 1
    :param while: longitud del mensaje sea menor a longitud de la clave - 1
    :param string mensaje: agrega string de llave en posicion n
    :param if: n sea menor que longitud de llave  - 1
    :param int n: itera n += 1
    :param else: n toma el valor de 0
    :param string ll: une con un caracter vacio el mensaje
    :return ll
    """
    mensaje = []
    clave = claveReal.replace(' ', '')
    n = 0
    illave = len(llave)-1
    iclave = len(clave)-1
    while len(mensaje) <= iclave:
        mensaje.append(llave[n])
        if n < illave:
            n += 1
        else:
            n = 0
    ll = "".join(mensaje)
    return ll
    #print(claveReal)
    

# Actualizacion de la llave a llave real para el mensaje

def act_llave(claveReal, ll, E, D, matriz, abc):
    """
    Actualizacion de la llave a llaveReal
    :param string llaveReal: string caracter vacio
    :param int indiceCambioLlave: comienza en valor 0
    :param string c: string caracter vacio
    :param for: i en el rango de claveReal
    :param if: claveReal en posicion i es diferente de caracter espacio
    :param string llaveReal: concatenar a llaveReal ll en posicion de indiceCambioLlave
    :param int indiceCambioLlave: iteracion += 1
    :param else: llaveReal concatenado un caracter espacio
    :param if D != -1: llama a funcion dec(desencriptar) con 4 entradas
    :param if E != -1: llama a funcion enc(encriptar) con 4 entradas
    :return c
    """

    llaveReal = ""
    #lineas = ""
    indiceCambioLlave = 0
    c = ""
    for i in range(len(claveReal)):
        if claveReal[i] != " ":
            llaveReal += ll[indiceCambioLlave]
            #lineas += "_"
            indiceCambioLlave += 1
        else:
            llaveReal += " "
            #lineas += "_"
    #print(llaveReal)
    #print(lineas)
    if D != -1:
        #desencripta
        #print(dec(claveReal,llaveReal,matriz,abc))
        c = dec(claveReal,llaveReal,matriz,abc)
        
    elif E != -1:
        #encripta
        #print(enc(claveReal,llaveReal,matriz,abc))
        c = enc(claveReal,llaveReal,matriz,abc)
    return c    

def main(entrada, usuario):
    """ 
    Funcion main
    param: string entrada: entrada es igual a cadena de a
    param: variable indic: llama a la funcion matroz
    param: variable a: llama a transformacion con parametros entrada, indic en posicion 0 y 1
    param: variable b: llama a que_quieres con parametros a, indic en posicion 0 y 1
    param: variable c: llama Vigenere con parametros b en posiciones [0,4] e indic en posicion 0 y 1
    param: variable d: llama act_llave con parametros b en posicion 1, c , b en posicion 2 y 3 e indic en posicion 0 y 1
    return: d
    """
    #entrada = a
    #usuario = 'Sergio'
    indic = matroz()
    a = transformacion(entrada, indic[0], indic[1])
    b = que_quieres(a, indic[0], indic[1])
    c = Vigenere(b[0], b[1], b[2], b[3], indic[0], indic[1])
    d = act_llave(b[1], c, b[2], b[3], indic[0], indic[1])
    mensaje = b[1]
    clave = b[0]
    if d != mensaje :
        Archivos.arch_historial(mensaje,clave,d,usuario)
        # escribir mensaje desencriptado

    if len(d) > 40:
        Archivos.arch_texto(d,usuario)
        d = "Debido a la longitud del mensaje se creo un archivo en la carpeta Texto."
    return d, mensaje, clave, usuario