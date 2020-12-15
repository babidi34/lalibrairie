import requests
from bs4 import BeautifulSoup

# faire un input qui demande un choix entre les différentes
# catégorie
print("Vous allez extraire les données d'une catégorie de \
livre sur lalibrairie.com et l'obtenir dans un .csv \n")
categorie = input("Choisis la catégorie de livre dont tu \
souhaites extraire les données: \n\n\
Tapes un chiffre pour choisir : \n\n1: Architecture et urbanisme \n2: Arts \n\
3: Bandes dessinées, Mangas \n4: Bien être et vie pratique \n\
5: Economie, industrie, technique \n6: Education, connaissance \n\
7: Jeunesse \n8: Littérature \n9: Loisirs, Distractions \n\
10: Sciences humaines, sociales")
print(categorie)
if categorie == "1":
    url = "https://www.lalibrairie.com/livres/rayon-architecture-et-urbanisme,19.html"
elif categorie == "2":
    url = "https://www.lalibrairie.com/livres/rayon-arts,62.html"
elif categorie == "3":
    url = "https://www.lalibrairie.com/livres/rayon-bandes-dessinees-mangas,143.html"
elif categorie == "4":
    url = "https://www.lalibrairie.com/livres/rayon-bien-etre-et-vie-pratique,997.html"
elif categorie == "5":
    url = "https://www.lalibrairie.com/livres/rayon-economie-industrie-technique,994.html"
elif categorie == "6":
    url = "https://www.lalibrairie.com/livres/rayon-education-connaissance,998.html"
elif categorie == "7":
    url = "https://www.lalibrairie.com/livres/rayon-jeunesse,335.html"
elif categorie == "8":
    url = "https://www.lalibrairie.com/livres/rayon-litterature,1000.html"
elif categorie == "9":
    url = "https://www.lalibrairie.com/livres/rayon-loisirs-distractions,999.html"
elif categorie == "10":
    url = "https://www.lalibrairie.com/livres/rayon-sciences-humaines-sociales,995.html"

def recup_url(url):
    fichier_data = open("url_categorie.csv","w")
    headers = {'User-Agent': 'Mozilla/5.0'}
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

        url_pagination = body.find("a" ,{"aria-label":"Next"})
        url = url + url_pagination['href']
        if url == last_url:
            break
        print(url)

    fichier_data.close()
print(url)
recup_url(url)
