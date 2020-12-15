import requests, csv
from bs4 import BeautifulSoup

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