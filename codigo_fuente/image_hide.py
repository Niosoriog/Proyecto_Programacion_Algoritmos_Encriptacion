import cv2 
from cv2 import cv2
import numpy as np

def binario(n):
    """
    
    :param int n: numero entero para convertir a binario
    :return string res: cadena de codigo binario
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
    return cad

def decimal(n):
    """
    :param string n: cadena de codigo binario
    :return num: numero en base diez
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
        
def conbinar(a,b): 
    """
    :param string a: cadena de codigo binario
    :param string b: cadena de codigo binario
    :retunr new_val: numero en base diez
    """
    x = str(a)
    y = str(b)
    new_val = 0
    if len(x)==8 and len(y)==8:
        new_str = x[:4] + y[:4]
        new_val = decimal(new_str)
    else:
        if len(x) != 8:
            i = 8 - len(x)
            new_str = '0'*i + x
            sec_new = new_str[:4] + y[:4]
            new_val = decimal(sec_new)
        else:
            i = 8 - len(y)
            new_str = '0'*i + y
            sec_new = x[:4] + new_str[:4]
            new_val = decimal(sec_new)  
    return new_val


red_1 = np.zeros((300,300), dtype='U25')
blue_1 = np.zeros((300,300), dtype='U25')
green_1 = np.zeros((300,300), dtype='U25')

red_2 = np.zeros((300,300), dtype='U25')
blue_2 = np.zeros((300,300), dtype='U25')
green_2 = np.zeros((300,300), dtype='U25')    

    
def read(a,b):
    """
    :param string a: ruta de acceso a una imagen
    :param string b: ruta de acceso a una imagen
    """
    image_1 = cv2.imread(a, 1)
    image_2 = cv2.imread(b, 1)

    for x in range(300):
        for y in range(300):
            b, g, r = image_1[x, y]
            red_1[x,y] = binario(r)
            blue_1[x,y] = binario(b)
            green_1[x,y] = binario(g)
    for x in range(300):
        for y in range(300):
            b, g, r = image_2[x, y]
            red_2[x,y] = binario(r)
            blue_2[x,y] = binario(b)
            green_2[x,y] = binario(g)



new_red = np.zeros((300,300), dtype='int32')
new_blue = np.zeros((300,300), dtype='int32')
new_green = np.zeros((300,300), dtype='int32')
    
def newValues():
    for x in range(300):
        for y in range(300):
            red = red_1[x,y]
            red2 = red_2[x,y]

            blue = blue_1[x,y]
            blue2 = blue_2[x,y]

            green = green_1[x,y]
            green2 = green_2[x,y]

            red_new_val = conbinar(red, red2)
            blue_new_val = conbinar(blue,blue2)
            green_new_val = conbinar(green, green2) 

            new_red[x,y] = red_new_val
            new_blue[x,y] = blue_new_val
            new_green[x,y] = green_new_val      
        
def hide_image(a,b):
    """
    :param string a: ruta de acceso a una imagen
    :param string b: ruta de acceso a una imagen
    :return new_red, new_blue, new_green: tupla de arrays numpy
    """
    c = a
    d = b
    read(c,d)
    newValues()
    return new_red, new_blue, new_green


