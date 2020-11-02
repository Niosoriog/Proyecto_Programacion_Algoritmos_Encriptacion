def encriptador(mensaje, clave):
    """
    Funcion para encriptar el mensaje
    :param string abc: cadena de caracteres posibles en el mensaje y clave
    :param string cadena: string vacio
    :param ciclor for: en el rango y longitud del mensaje
    :param condicional: mensaje en la posicion x igual a caracter de espacio
    :param string cadena: concatena cadena mas caracter de espacio
    :param else: busca en abc los caracteres de mensaje y clave en posicion x
    :param condicional indices pares: res es igual a un indice par
    :param string pos: llama funcion extranjero con el indice de res
    :param string cadena: concatena a cadena el string pos
    :param condicional indices impares: res es igual a un indice impar
    :param string pos: llama funcion extranjero con el indice de res
    :param string cadena: concatena a cadena el string pos
    :param else condicion de indices: res es igual al indice de el mensaje(id)
    :param string pos: llama funcion extranjero con el indice de res
    :param string cadena: concatena a cadena el string pos
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
    Funcion para encriptar el mensaje
    :param string abc: cadena de caracteres posibles en el mensaje y clave
    :param string lpoi: cadena de caracteres posibles de encriptacion
    :param string cadena: string vacio
    :param ciclor for: en el rango y longitud del mensaje
    :param condicional: mensaje en la posicion x igual a caracter de espacio
    :param string cadena: concatena cadena mas caracter de espacio
    :param else: busca en abc los caracteres de clave y en lpoi los caracteres del mensaje en posicion x
    :param condicional indices pares: res es igual a un indice par clave con indice par
    :param string pos: llama funcion entregar con el indice de id
    :param string cadena: concatena a cadena el string pos
    :param condicional indices impares: res es igual a un indice impar clave con indice impar
    :param string pos: llama funcion entregar con el indice de id
    :param string cadena: concatena a cadena el string pos
    :param else condicion de indices: res es igual al indice de el mensaje(id)
    :param string pos: llama funcion entregar con el indice de id
    :param string cadena: concatena a cadena el string pos
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
    :param string lpoi: letras para otros idiomas(lpoi) caracteres UNICODE 
    :param ciclo for: en el rango y longitud de lpoi
    :param condicional: si i == n, n es el valor que recibe de pos en la funcion de encriptar
    :return: lpoi en la posicion i
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
    :param string abc: abc contiene los caracteres para desencriptar y convertir de lpoi a abc
    :param string cba: un caracter que permite tener los mismos indices de abc mas el string abc con paso - 1
    :param int d: valor absoluto de c
    :param ciclo for: i en rango y longitud de abc
    :param condicional: si i == d, d es el valor absoluto que se recibe de la funcion desencriptar
    :param condicional: si c es menor que 0
    :return: cba en posicion i
    :param else: si c es mayor que 0
    :return: abc en posicion i 
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
    :param int tamano_texto: longitud de la cadena o mensaje
    :param int tamano_clave: longitud de la clave
    :param condicional: si tamano_texto es igual a tamano_clave
    :return: cadena, clave
    :param condicional: si tamano_texto es mayor a tamano_clave
    :param int op: op es igual a tamano_texto menos tamano_clave
    :param ciclo for: i en rango op completa la clave para la cadena
    :param string clave: clave es igual a clave mas clave en posicion i
    :param else: tamano_texto es menor que tamano_clave
    :param int op: op es igual a tamano_clave - tamano_texto
    :param string cadena: cadena es igual a cadena mas el caracter espacio por op
    :return: cadena, clave 
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