import requests, csv
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
        
    fichier_data.close()

def recup_data():
    fichier_data = open("page_produit_data_masse.csv","w")
    fichier_url = open("url_categorie.csv","r")
    line = fichier_url.readline()
    headers = {'User-Agent': 'Mozilla/5.0'}
    fichier_data.write('Url de la page ; Titre ; Auteur ; \
        Prix ; Description ; Resumé ; Collection ; Url image \n')

    while line:
        url = line.strip()
        response = requests.get(url,headers=headers)
        print(url)


        # On applique bs pour analyser le contenu de la requête :
        parser = BeautifulSoup(response.content, 'html.parser')
        body = parser.body

        # on récupère nos data et on les place dans des variables puis
        # on insère les datas dans les bonnes colonnes
        
        try:
            product_page_url = url + " ;"
            fichier_data.write(product_page_url)
        except:
            product_page_url = "- ;"
            fichier_data.write(product_page_url)
        try:
            titre = body.find(itemprop="name")
            titre = titre.text + " ;"
            fichier_data.write(titre)
        except:
            titre = "- ;"
            fichier_data.write(titre)

        try:
            autor = body.find(itemprop="author")
            autor = autor.text + " ;"
            fichier_data.write(autor)
        except:
            autor = "- ;"
            fichier_data.write(autor)

        try:
            price = body.find(itemprop="price")
            price = price.text + " ;"
            fichier_data.write(price)
        except:
            price =  "- ;"
            fichier_data.write(price)

        try:
            product_description = body.find(id="fiche-technique")
            product_description = product_description.text.strip().replace('\n','')
            product_description = product_description + " ;"
            product_description = product_description.replace('  ',' ')
            fichier_data.write(product_description)
        except:
            product_description = "- ;"
            fichier_data.write(product_description)

        try:    
            resume = body.find(itemprop="description")
            resume = resume.text + " ;"
            fichier_data.write(resume)
        except:
            resume = "- ;"
            fichier_data.write(resume)

        try:
            collection = body.find("p", {"class":"collections text-gray text-mulit-light"})
            collection = collection.find("a", {"class":"text-gray"})
            collection = collection.text + " ;"
            fichier_data.write(collection)
        except:
            collection = "- ;"
            fichier_data.write(collection)

        try:
            image_url = body.find("picture")
            image_url = "https://www.lalibrairie.com" + image_url.img['src']
            image_url = image_url + " \n"
            fichier_data.write(image_url)
        except:
            image_url = "- \n"
            fichier_data.write(image_url)

        
        line = fichier_url.readline()

    fichier_data.close()

    # On lit maintenant le fichier

    fichier_a_lire = open("page_produit_data.csv", 'r', newline="")
    lire = csv.reader(fichier_a_lire,delimiter=';')
    for row in lire:
        print(row)

    fichier_a_lire.close()

recup_url(url)
recup_data()
print("Success !! Vos données ce trouve dans 'page_produit_data_masse.csv' ")
