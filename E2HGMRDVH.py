#Heissel Gustavo Mendez Ramirez 1674452
#Diego Vitela Herrera 1822993
#Aqui utilizamos el try por si ocurre algun error durante el codigo el cual seria la installacion del modulo
try:
    import requests
    import os
    import sys
    from bs4 import BeautifulSoup as bs
    import webbrowser

    print("Este script navega en las páginas de noticas de la UANL")
    inicioRango = int(input("Pagina inicial para buscar: "))
    finRango = int(input("Pagina final para buscar: "))
    dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
    if inicioRango > finRango:
        inicioRango,finRango = finRango,inicioRango
    for i in range (inicioRango,finRango,1):
        url = "https://www.uanl.mx/noticias/page/"+str(i)
        pagina = requests.get (url)
        if pagina.status_code != 200:
            raise TypeError("Pagina no encontrada")
        else:
            soup = bs(pagina.content,"html.parser")
            info = soup.select("h3 a")
            for etiqueta in info:
                url2 = etiqueta.get("href")
                pagina2 = requests.get(url2)
                if pagina2.status_code == 200:
                    soup2 = bs(pagina2.content,"html.parser")
                    parrafos = soup2.select("p")    
                    for elemento in parrafos:
                        if dependencia in elemento.getText():
                            print ("Abriendo",url2)
                            webbrowser.open(url2)
                            break
#Utilizamos except para arreglar el error e instalar los modulos
except Exception as e:
    os.system("pip install bs4")
    os.system('pip install PyPI-Browser') 

    print('Installing webbrowser...') 

    print('Ejecuta de nuevo tu script...') 

    exit() 
    

