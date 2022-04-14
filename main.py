import time
from selenium import webdriver
from bs4 import BeautifulSoup

#create a .txt file with each spot you want in different lines
MEMS = open('memos.txt', 'r')
individuales = MEMS.readlines()

pregunta = []
for a in individuales:
    pregunta.append(a.strip())



browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://intranet.upv.es/pls/soalu/est_intranet.NI_Portal_n?p_idioma=c')
#create a .txt file with you UPV username and password in different lines
constrasena = open('contrasena.txt')
line = constrasena.readlines()
username = line[0]
password = line[1]
srs = browser.page_source
soup = BeautifulSoup(srs, 'lxml')
elementID = browser.find_elements_by_name('dni')
for i in elementID:
    i.send_keys(username)
    break
elementID2 = browser.find_element_by_name('clau')
elementID2.send_keys(password)
elementID2.submit()

srs = browser.page_source
soup = BeautifulSoup(srs, 'lxml')

elementID3 = browser.find_elements_by_class_name('titularEspecial')
for i in elementID3:
    i.click()
    break


browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
srs = browser.page_source
soup = BeautifulSoup(srs,'lxml')

elementID4 = browser.find_element_by_partial_link_text('Actividades y Escuelas: reserva de plaza semanal e inscripción / Consulta de disponibilidad')
elementID4.click()

srs = browser.page_source
soup = BeautifulSoup(srs,'lxml')

elementID5 = browser.find_element_by_xpath("//option[@value='20435']").click()

srs = browser.page_source
soup = BeautifulSoup(srs,'lxml')

linksList = []
horasDisponibles = browser.find_elements_by_class_name('upv_enlacelista')
for i in horasDisponibles:
    aa = i.get_attribute('href')
    if 'HSemActDesMat' in aa:
        pass
    elif 'HSemActividades' in aa:
        pass
    else:
        linksList.append(aa)

diaList = []
dia = soup.find_all('a', {'class':'upv_enlacelista'})
for i in dia:
    ee = str(i)
    if 'HSemActDesMat' in ee:
        pass
    elif 'HSemActividades' in ee:
        pass
    elif 'HSemActMatri' in ee:
        diaList.append(i.text)

cleanDia = []
for a in diaList:
    cleanDia.append(a[0:6])

for i in pregunta:
    index = cleanDia.index(i)
    respuestaLink = linksList[index]
    browser.get(respuestaLink)




