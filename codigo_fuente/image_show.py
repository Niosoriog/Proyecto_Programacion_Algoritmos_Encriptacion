import cv2 
from cv2 import cv2
import numpy as np

def extraer(a):
    """
    :param string a: recibe una cadena de codigo binario
    :return c: retorna la mitad de la cadena mas cuatro ceros
    """
    c = a[4:] + "0000"
    return c

def decimal(n):
    """
    :param string n: string de codigo binario
    :return num: numero en decimal
    """
    exp = 7
    num = 0                       
    for x in n:
        if x=='1':
            num += 2**exp
            exp -= 1
        else:
            exp -= 1
    return num

def binario(n):
    """
    :param int n: numero entero 
    :return res: string de codigo binario
    """
    cad = ''
    exp = 7
    suma = 0
    while exp >= 0:
        if 2**exp <= n and suma+(2**exp) <= n:
            cad += '1'
            suma += 2**exp
            exp -= 1
        else:
            cad += '0'
            exp -= 1
    res = extraer(cad)
    return res

red_1 = np.zeros((300,300), dtype='U25')
blue_1 = np.zeros((300,300), dtype='U25')
green_1 = np.zeros((300,300), dtype='U25')

def read(a):
    """
    :param string a: ruta de acceso a una imagen
    """
    img = cv2.imread(a, 1)
    for x in range(300):
        for y in range(300):
            b, g, r = img [x, y]
            red_1[x,y] = binario(r)
            blue_1[x,y] = binario(b)
            green_1[x,y] = binario(g)


new_red = np.zeros((300,300), dtype='int32')
new_blue = np.zeros((300,300), dtype='int32')
new_green = np.zeros((300,300), dtype='int32')

def show():
    for x in range(300):
        for y in range(300):
            red = red_1[x,y]
            blue = blue_1[x,y]
            green = green_1[x,y]

            n_red = decimal(red)
            n_blue = decimal(blue)
            n_green = decimal(green)

            new_red[x,y] = n_red
            new_blue[x,y] = n_blue 
            new_green[x,y] = n_green
def show_image(a):
    """
    :param string a: ruta de acceso a la imagen
    :return new_red, new_blue, new_green: numpy arrays 
    """
    read(a)
    show()
    return new_red, new_blue, new_green


