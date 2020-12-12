from random import choice
import itertools     
import math
import Archivos
def primos_permitidos():
    """
    primos_permitidos crea una lista de tuplas 
    :param list[tuplas]: contiene parejas de numeros primos aleatorios
    :return: list[tuplas]
    """
    parejas_permitidas =  [(31,23),(47,19),(7,19),(17,41),(31,7),(29,47),(37,23),(2,79),(43,17),(7,37),(5,61),
    (17,31),(23,19),(23,7),(11,83),(17,7),(71,3),(37,29),(7,79),(11,59),(37,3),(3,59),(13,53),(79,11),(89,3),
    (2,97),(23,5),(13,41),(89,2),(5,97),(89,7),(41,7),(59,7),(19,41),(31,13),(29,19),(79,5),(83,7),
    (83,3),(43,7),(23,17),(23,29),(3,41),(17,47),(37,13),(37,11),(53,5),(43,3),(5,83),(7,67),(89,5),
    (19,53),(29,17),(53,11),(11,41),(5,47),(73,13),(13,23),(47,29),(5,89),(17,23),(5,43),(71,11),(67,5),
    (149,3),(7,47),(19,37),(127,7),(109,7),(7,53),(67,2),(19,41),(67,11),(7,97),(3,103),(3,131),(163,2),(11,61),
    (113,5),(73,5),(17,7),(61,5),(97,5),(43,13),(157,5),(2,107),(71,5),(3,151),(5,29),(2,151),(137,3),
    (13,29),(59,11),(137,5),(47,11),(13,47),(2,197),(53,17),(239,3),(229,2),(23,37),(53,13),(11,73)]
    return parejas_permitidas  

def crear_dicionarios():
    """
    crear_diccionarios crea un diccionario de caracteres
    :param dict: contiene caracteres usados en la escritura y asigna un valor a cada uno
    :return: dict(valor_alfanumerico)
    """
    valor_alfanumerico = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
    'm': 13, 'n': 14, 'ñ': 15, 'o': 16, 'p': 17, 'q': 18, 'r': 19, 's': 20, 't': 21, 'u': 22, 'v': 23, 'w': 24, 'x': 25, 'y': 26,
    'z': 27, 'A': 28, 'B': 29, 'C': 30, 'D': 31, 'E': 32, 'F': 33, 'G': 34, 'H': 35, 'I': 36, 'J': 37, 'K': 38, 'L': 39, 'M': 40,
    'N': 41, 'Ñ': 42, 'O': 43, 'P': 44, 'Q': 45, 'R': 46, 'S': 47, 'T': 48, 'U': 49, 'V': 50, 'W': 51, 'X': 52, 'Y': 53, 'Z': 54,
    'á': 55, 'Á': 56, 'é': 57, 'É': 58, 'í': 59, 'Í': 60, 'ó': 61, 'Ó': 62, 'ú': 63, 'Ú': 64, '/': 65, '(': 66, ')': 67, '"': 68,
    '=': 69, '&': 70, '%': 71, '$': 72, '#': 73, '!': 74, '¡': 75, '¿': 76, '?': 77, '*': 78, '-': 79, '+': 80, "'": 81, '0': 82,
    '1': 83, '2': 84, '3': 85, '4': 86, '5': 87, '6': 88, '7': 89, '8': 90, '9': 91, '|': 92, '°': 93, '<': 94, '>': 95, '{': 96,
    '}': 97, '[': 98, ']': 99, ',': 100, '.': 101, ':': 102, ';': 103, '_': 104, '^': 105, '`': 106, '~': 107, '¬': 108, ' ': 109}
    return valor_alfanumerico
def isPrime(num):
    """
    isPrime verifica si un numero es primo o no
    :param int: num menor que 1
    :return: False
    :param int: num igual a 2
    :return: True
    :param range num: i divisor de num
    :return: False
    :return: True
    """
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True  
def crear_claves():
    """
    crear_claves genera una serie de numeros a partir de primos y coprimos
    :param int minPrim: valor inicial
    :param int maxPrim: valor final
    :param list[primos]: añade valores primos entre minPrim y maxPrim
    :param tuple: Toma una tupla aleatoria de parejas_permitidas
    :param int primo_1: valor de la tupla en posicion 0
    :param int primo_2: valor de la tupla posicion 1
    :param int n: valor de primo_1 por primo_2
    :param int Phi_euler: valor de primo_1 - 1 por primo_2 - 1
    :param int co_primo: valor no divisor de Phi_euler
    :param list clave_publica: co_primo, n
    :param list clave_privada: valor donde co_primo * j modulo Phi_euler es igual a 1, n
    :return: clave_publica, clave_privada
     """
    minPrim = 0
    maxPrim = 150
    primos = [i for i in range(minPrim, maxPrim) if isPrime(i)]
    primos_permi = primos_permitidos()
    tupla = choice(primos_permi)
    pri1 = tupla[0]
    pri2 = tupla[1]
    # ya tenemos los dos primos
    #print(pri1,"---",pri2)
    n = pri1 * pri2
    Phi_e = (pri1-1)*(pri2-1)  # z
    # encontrar un coprimo
    for numero in primos:
        if Phi_e % numero != 0:
            co_pri = numero  # k
            break
    clave_publica = [str(co_pri),str(n)]
    #print(clave_publica)
    for j in itertools.count(2):
        if (co_pri*j) % Phi_e == 1:
            clave_privada = [str(j),str(n)]
            break
    #print(clave_privada)
    clave_publica = ",".join(clave_publica)
    clave_privada = ",".join(clave_privada)
    return clave_publica,clave_privada
      
def encriptar_RSA (mensaje,clave_publi):
    """
    encriptar_RSA recibe un string y una clave_publica para encriptar
    :param list mensaje_encriptado: lista vacia
    :param list valores_numericos: toma los valores de crear_diccionarios segun el caracter
    :param int restante: valor resultante de los valores de valores_numericos por clave_publica[0] y divididos por clave_publica[1]
    :param float decimal: se toma la parte decimal de restante y se redondea a 3 decimales
    :param int encrip: valor de encriptado, decimal * clave_publi[1]
    :return: mensaje_final
    """
    dicio = crear_dicionarios()
    mensaje_aux = []
    cadena_1 = [ dicio[elemento]  for elemento in mensaje]
    #print(cadena_1,"valor inicial")
    for valor in cadena_1:
        res = (valor**int(clave_publi[0]))/int(clave_publi[1])
        dec, ent = math.modf(res)
        dec = round(dec,3)
        encrip = dec*int(clave_publi[1])
        mensaje_aux.append(str(round(encrip)))
    mensaje_final = ",".join(mensaje_aux)
    return mensaje_final

def desencriptar_RSA(mensaje, clave_privada):
    """
    desencriptar_RSA utiliza un mensaje encriptado y una clave unica para desencriptar el mensaje
    :param list[descifrado]: crea una lista vacia
    :param int exponenciado: toma el cada valor del mensaje y lo eleva a la clave_privada[0]
    :param int restante: toma el valor de ini y toma la parte entera con clave_privada[1]
    :param int desencriptado: toma el valor de res y lo multiplica por la clave_privada[1]
    :param list[keys]: lista con las llaves de crear_diccionarios
    :param list[values]: lista con los valores de crear_diccionarios
    :param string desencript:se concatena las llaves con el valor de descifrado
    :return: desencript
    """
    biblioteca = crear_dicionarios()
    descifrado = []
    for valor in  mensaje:
        ini = (int(valor)**int(clave_privada[0]))
        res = ini//int(clave_privada[1])
        sol = res * int(clave_privada[1])
        descifrado.append(ini-sol)
    keys = list(biblioteca.keys())
    values = list(biblioteca.values())
    desencript = ''
    for i in descifrado:
        desencript += keys[values.index(int(i))]
    return desencript
    
def rsa(mensaje, clave, opcion, opcion2,usuario):
    if opcion == 1:
        c_publica,c_privada = crear_claves()
        Archivos.arc_histo_rsa_llaves(c_publica,c_privada,usuario)
        return c_publica, c_privada
    if opcion == 0:
        if opcion2 == 'enc':
            mensaje = list(mensaje)
            clave_publi = clave.split(",")
            cad = encriptar_RSA(mensaje,clave_publi)
            #se guarda el historial
            Archivos.arch_historial(mensaje,clave_publi,cad,usuario)
            if len(cad) > 40:
                Archivos.arch_texto(cad,usuario)
                cad = "Debido a la longitud del mensaje se creo un archivo en la carpeta Texto."
            return cad
        if opcion2 == 'des':
            mensaje = mensaje.split(",")
            clave_privi = clave.split(",")
            cad = desencriptar_RSA(mensaje,clave_privi)
            #se guarda el historial
            Archivos.arch_historial(mensaje,clave_privi,cad,usuario)
            if len (cad) > 40:
                Archivos.arch_texto(cad,usuario)
                cad = "Debido a la longitud del mensaje se creo un archivo en la carpeta Texto."
            return cad