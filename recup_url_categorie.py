import requests, csv
from bs4 import BeautifulSoup

fichier_data = open("url_categorie.csv","w")
headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://www.lalibrairie.com/livres/rayon-architecture-et-urbanisme,19.html"
last_url = ""
while True:
    last_url = url
    response = requests.get(url,headers=headers)
    # On applique bs pour analyser le contenu de la requête :
    parser = BeautifulSoup(response.content, 'html.parser')
    body = parser.body
    info = body.find_all("div" ,{"class":"infos"})
    for i in info:
        liens = "https://www.lalibrairie.com" + i.h2.a['href'] + "\n"
        liens = fichier_data.write(liens)

    url = body.find("a" ,{"aria-label":"Next"})
    url = "https://www.lalibrairie.com/livres/rayon-architecture-et-urbanisme,19.html" + url['href']
    if url == last_url:
        break
    print(url)

fichier_data.close()
