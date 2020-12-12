from bs4 import BeautifulSoup
from urllib.request import urlopen


def parse_vigener(entry_soup):
    h1 = str(entry_soup.find('h1'))
    title_start = h1.find('C')
    title_end = h1.find('</h1>')
    p = entry_soup.find_all('p')
    title = h1[title_start:title_end]
    parrf_1 = p[0]
    parrf_2 = p[1]
    parrf_3 = p[2]
    res1 = parrf_1.get_text()
    res2 = parrf_2.get_text()
    res3 = parrf_3.get_text()
    cad = title+'\n'+str(res1)+str(res2)+str(res3)
    return cad
def parse_vernam(entry_soup):
    p = entry_soup.find_all('p')
    h1 =entry_soup.find_all('h1')
    h2 = entry_soup.find_all('h2')
    title = h1[0]
    parrf1 = p[0]
    title2 = h2[0]
    parrf2 = p[1]
    res1 = title.get_text()
    res2 = parrf1.get_text()
    res3 = title2.get_text()
    res4 = parrf2.get_text()
    cad = str(res1)+'\n'+str(res2)+str(res3)+str(res4)
    return cad
def parse_cesar(entry_soup):
    h1 = entry_soup.find_all('h1')
    p = entry_soup.find_all('p')
    title = h1[0]
    parrf1 = p[0]
    parrf2 = p[1]
    res1 = title.get_text()
    res2 = parrf1.get_text()
    res3 = parrf2.get_text()
    cad = str(res1)+'\n'+str(res2)+str(res3)
    return cad
def parse_solitario(entry_soup):
    h1 = entry_soup.find_all('h1')
    p = entry_soup.find_all('p')
    title = h1[0]
    parrf1 = p[3]
    parrf2 = p[4]
    parrf3 = p[5]
    res1 = title.get_text()
    res2 = parrf1.get_text()
    res3 = parrf2.get_text()
    res4 = parrf3.get_text()
    cad = str(res1)+'\n'+str(res2)+str(res3)+str(res4)
    return cad
def get_url_solitario():
    url = "https://es.qaz.wiki/wiki/Solitaire_(cipher)"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return parse_solitario(soup)
def get_url_vigener():
    url = "https://es.wikipedia.org/wiki/Cifrado_de_Vigen%C3%A8re"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return parse_vigener(soup)
def get_url_vernam():
    url = "https://es.wikipedia.org/wiki/Cifrado_Vernam"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return parse_vernam(soup)
def get_url_cesar():
    url = "https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return parse_cesar(soup)
def scrapp():
    vig = get_url_vigener()+'\n'
    ver = get_url_vernam()+'\n' 
    ces = get_url_cesar()+'\n'
    sol = get_url_solitario()
    return vig, ver, ces, sol

