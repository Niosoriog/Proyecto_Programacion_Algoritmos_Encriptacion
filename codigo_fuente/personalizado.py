def encriptador(mensaje, clave):
    """
    Funcion para encriptar el mensaje con el metodo par - impar
    :param string mensaje: es el mensaje a encriptar.
    :param string clave: es la clave con la que se encriptara el mensaje.
    :return: cadena
    """
    # 114 caracteres
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.+-\*?¡¿!<>=)(/&%$#"_;:1234567890[]{^}áéíóúÁÉÍÓÚäëïöüÄËÏÖÜ@|°'
    cadena = ""
    for x in range(len(mensaje)):
        if mensaje[x] == " ":
            cadena = cadena + " "
        else:
            id = abc.index(mensaje[x])
            ic = abc.index(clave[x])
            
            if id % 2 == 0 and ic % 2 == 0:
                res = (id + 1) + (ic - 1)
                pos = extranjero(res)
                cadena += pos

            elif id % 2 == 1 and ic % 2 == 1:
                res = (id + ic) + 1 
                if res > len(abc):
                    res = res % len(abc)
                pos = extranjero(res)
                cadena += pos
            
            else:
                pos = extranjero(id)
                cadena += pos
    return cadena

def desencriptador(mensaje, clave):
    """
    Funcion para desencriptar el mensaje con el metodo de par-impar

    :param string mensaje: es el mensaje a encriptar.
    :param string clave: es la clave con la que se encriptara el mensaje.
    :return: cadena
    
    """ 
    # 114 caracteres
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.+-\*?¡¿!<>=)(/&%$#"_;:1234567890[]{^}áéíóúÁÉÍÓÚäëïöüÄËÏÖÜ@|°'
    #lpoi = '1234'
    lpoi = '阿贝德俄非黑ᚦᚩᚱᚳᚹᚺᚾᛃᛈᛇᛞᛟᛋᛥᛣ车厚卡艾耶么呢涅௭௬௫௪௩௨哦佩苦和色特吴维豆布勒吉尺伊列哈舍塔௯௮௧೦ൠஇਔஈফঠজઙюஙѮಹஹѲকৄಕೆईୠДЖЭБѪᚠᚢΞλΘψσ事時彼間大ᐁᑫᕴᒉᒣᓀᓭᕓᕂᙯᖅᙰЦЛѬബʃㅖㅊ၇'
    cadena = ""
    for x in range(len(mensaje)):
        if mensaje[x] == " ":
            cadena = cadena + " "
        else:
            res = lpoi.index(mensaje[x])
            ic = abc.index(clave[x])
            
            if res % 2 == 0 and ic % 2 == 0:
                id = res - ic 
                pos = entregar(id)
                cadena += pos

            elif res % 2 == 1 and ic % 2 == 1:
                id = res - ic -1
                pos = entregar(id)
                cadena += pos
            
            else:
                pos = entregar(res)
                cadena += pos
    return cadena

def extranjero(n):
    """
    Extranjero contiene caracteres UNICODE de otros alfabetos existentes o extintos para encriptar
    :param int n: es el entero que nos dice la posicion que tiene que encontrar en la lista lpoi.
    :return: el caracter asignado a esa posicion n.
    """ 
    # 114 caracteres
    #lpoi = '1234'
    lpoi = '阿贝德俄非黑ᚦᚩᚱᚳᚹᚺᚾᛃᛈᛇᛞᛟᛋᛥᛣ车厚卡艾耶么呢涅௭௬௫௪௩௨哦佩苦和色特吴维豆布勒吉尺伊列哈舍塔௯௮௧೦ൠஇਔஈফঠজઙюஙѮಹஹѲকৄಕೆईୠДЖЭБѪᚠᚢΞλΘψσ事時彼間大ᐁᑫᕴᒉᒣᓀᓭᕓᕂᙯᖅᙰЦЛѬബʃㅖㅊ၇'
    for i in range(len(lpoi)):
        if i == n:
            return lpoi[i]

def entregar(c):
    """
    Entregar contiene caracteres que puede contener un mensaje para desencriptar
    :param int c: es un numero entero que nos dice en que posicion esta el caracter que se debe devolver para desencriptar el mensaje
    :return: el caracter asignada a la posicion n.
    """
    #abc = 'abcd'
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.+-\*?¡¿!<>=)(/&%$#"_;:1234567890[]{^}áéíóúÁÉÍÓÚäëïöüÄËÏÖÜ@|°'
    cba = 'あ'+ abc[::-1]
    d = abs(c)
    for i in range(len(abc)):
        if i == d:
            if c < 0:
                return cba[i]
            else:
                return abc[c]


def igualar (cadena,clave):
    """
    Igualar toma la cadena y la clave y genera una clave real para toda la longitud del mensaje
    :param string cadena: Es el mensaje que ingresa el usuario 
    :param string clave: es la clave que se va a igualar al tamaño de la cadena para que no ocurran fallos al encriptar o desencriptar.
    :param condicional: si tamano_texto es igual a tamano_clave
    :return: el mensaje y la cadena cuando tengan la misma longitud.
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
def perso(mensaje, clave, opcion):
    men = mensaje.strip()
    cla = clave.strip()
    men,cla = igualar(men,cla)
    cad = ""
    if opcion == "enc":
        cad = encriptador(men, cla)
    elif opcion == "dec":
        cad =  desencriptador(men, cla)
    return cad