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
def s2b(a):
    """
    s2b Esta funcion recibe una string y devuelve una lista con los codigos binarios de los cararteres de la string
    :param diccionario binario: los caracteres y numeros con sus representaciones en codigo binario
    :param lista codigo_binario: lista de los codigos binarios de los caracteres de la string
    :return: lista con los codigos binarios

    """
    binario = {"A":"01000001","Á":"11000001","B":"01000010","C":"01000011","D":"01000100","E":"01000101","É":"11001001","F":"01000110","G":"01000111","H":"01001000","I":"01001001","Í":"11001101","J":"01001010","K":"01001011","L":"01001100","M":"01001101",
    "N":"01001110","Ñ":"11010001","O":"01001111","Ó":"11010011","P":"01010000","Q":"01010001","R":"01010010","S":"01010011","T":"01010100","U":"01010101","Ú":"11011010","V":"01010110","W":"01010111","X":"01011000","Y":"01011001","Z":"01011010","a":"01100001",
    "á":"11100001","b":"01100010","c":"01100011","d":"01100100","e":"01100101","é":"11101001","f":"01100110","g":"01100111","h":"01101000","i":"01101001","í":"11101101","j":"01101010","k":"01101011","l":"01101100","m":"01101101",
    "n":"01101110","ñ":"11110001","o":"01101111","ó":"11110011","p":"01110000","q":"01110001","r":"01110010","s":"01110011","t":"01110100","u":"01110101","ú":"11111010","v":"01110110","w":"01110111","x":"01111000","y":"01111001","z":"01111010", "!":"00100001","#":"00100011",
    "$":"00100100","%":"00100101","&":"00100110","'":"00100111","(":"00101000",")":"00101001","*":"00101010","+":"00101011",",":"00101100","-":"00101101",".":"00101110","/":"00101111","0":"00110000","1":"00110001","2":"00110010","3":"00110011","4":"00110100","5":"00110101","6":"00110110",
    "7":"00110111","8":"00111000","9":"00111001",":":"00111010",";":"00111011","<":"00111100","=":"00111101",">":"00111110","?":"00111111","@":"01000000","~":"00100000"}
    codigo_binario = []
    for x in a:
        if x in binario:
            codigo_binario.append(binario[x])    
    return codigo_binario       
def b2s(b):
    """
    b2s Esta funcion recibe una lista de codigos binarios y retorna una cadena con sus respectivas representaciones
    :param diccionario caracteres: codigos binarios con sus representaciones en caractres
    :param string string: cadena de caracteres de los codigos binarios
    :return: cadena de caracteres segun la entrada de codigos binarios
    """
    caracteres = {'01000001':"A","11000001":"Á","01000010":"B","01000011":"C","01000100":"D","01000101":"E","11001001":"É","01000110":"F","01000111":"G","01001000":"H","01001001":"I","11001101":"Í","01001010":"J","01001011":"K","01001100":"L","01001101":"M",
    "01001110":"N","11010001":"Ñ","01001111":"O","11010011":"Ó","01010000":"P","01010001":"Q","01010010":"R","01010011":"S","01010100":"T","01010101":"U","11011010":"Ú","01010110":"V","01010111":"W","01011000":"X","01011001":"Y","01011010":"Z","01100001":"a",
    "11100001":"á","01100010":"b","01100011":"c","01100100":"d","01100101":"e","11101001":"é","01100110":"f","01100111":"g","01101000":"h","01101001":"i","11101101":"í","01101010":"j","01101011":"k","01101100":"l","01101101":"m",
    "01101110":"n","11110001":"ñ","01101111":"o","11110011":"ó","01110000":"p","01110001":"q","01110010":"r","01110011":"s","01110100":"t","01110101":"u","11111010":"ú","01110110":"v","01110111":"w","01111000":"x","01111001":"y","01111010":"z","00100001":"!","00100011":"#",
    "00100100":"$","00100101":"%","00100110":"&","00100111":"'","00101000":"(","00101001":")","00101010":"*","00101011":"+","00101100":",","00101101":"-","00101110":".","00101111":"/","00110000":"0","00110001":"1","00110010":"2","00110011":"3","00110100":"4","00110101":"5","00110110":"6",
    "00110111":"7","00111000":"8","00111001":"9","00111010":":","00111011":";","00111100":"<","00111101":"=","00111110":">","00111111":"?","01000000":"@","00100000":"~"}
    string = ""                                                       
    for y in b:
        caracter = []
        if y in caracteres:                      
            caracter.append(caracteres[y])
            string += "".join(caracter)
    return string

def encriptar(mensaje, clave):   
    """
    encriptar recibe el mensaje para encriptar y su respectiva clave, le aplica la tabla de verdad XOR a los codigos binarios de estos
    :param strign x: mensaje en mayuscula
    :paran strign y: clave en maniscula
    :  
    """
    x = mensaje.upper() 
    y = clave.lower()
    c = x.replace(" ", "")
    d = y.replace(" ", "")
    mensaje_binario = s2b(c)
    clave_binario = s2b(d)
    mensaje_encriptado = []
    for i in range(0, len(c)):
        res = ""
        for j in range(0,8):
            x = mensaje_binario[i]
            y = x[j]
            x2 = clave_binario[i]
            y2 = x2[j]
            if y == y2:
                res += "0"
            else: 
                res += "1"    
        mensaje_encriptado.append(res)   
    string_encriptada = b2s(mensaje_encriptado)      
    return string_encriptada  

def desencriptar(mensaje, clave):
    men = mensaje.strip()
    mensaje_binario = s2b(mensaje)
    clave_binario = s2b(clave)
    mensaje_encriptado = []
    for i in range(0, len(men)):
        res = ""
        for j in range(0,8):
            x = mensaje_binario[i]
            y = x[j]
            x2 = clave_binario[i]
            y2 = x2[j]
            if y == y2:
                res += "0"
            else: 
                res += "1"    
        mensaje_encriptado.append(res)   
    string_encriptada = b2s(mensaje_encriptado)      
    return string_encriptada
    
def vernan(mensaje, clave, opcion):
    mensaje, clave = igualar(mensaje, clave)
    cadena = ""
    if opcion == "enc":
        cadena = encriptar(mensaje, clave)
    else:
        cadena = desencriptar(mensaje, clave)

    return cadena    
    

    

