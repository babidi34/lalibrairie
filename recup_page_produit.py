import requests, csv
from bs4 import BeautifulSoup

fichier_data = open("page_produit_data.csv","w")
headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://www.lalibrairie.com/livres/des-ailes-d-argent--la-vengeance-d-une-femme-est-douce-et-impitoyable_0-6872120_9782330138516.html"
response = requests.get(url,headers=headers)

# On applique bs pour analyser le contenu de la requête :
parser = BeautifulSoup(response.content, 'html.parser')
body = parser.body

# on récupère nos data et on les place dans des variables puis
# on insère les datas dans les bonnes colonnes
fichier_data.write('Url de la page ; Titre ; Auteur ; \
Prix ; Description ; Resumé ; Collection ; Url image \n')

product_page_url = url + " ;"
fichier_data.write(product_page_url)

titre = body.find(itemprop="name")
titre = titre.text + " ;"
fichier_data.write(titre)

autor = body.find(itemprop="author")
autor = autor.text + " ;"
fichier_data.write(autor)

price = body.find(itemprop="price")
price = price.text + " ;"
fichier_data.write(price)

product_description = body.find(id="fiche-technique")
product_description = product_description.text.strip().replace('\n','')
product_description = product_description + " ;"
product_description = product_description.replace('  ',' ')
fichier_data.write(product_description)

resume = body.find(itemprop="description")
resume = resume.text + " ;"
fichier_data.write(resume)

collection = body.find("p", {"class":"collections text-gray text-mulit-light"})
collection = collection.find("a", {"class":"text-gray"})
collection = collection.text + " ;"
fichier_data.write(collection)

image_url = body.find("picture")
image_url = "https://www.lalibrairie.com" + image_url.img['src']
image_url = image_url + " ;"
fichier_data.write(image_url)


fichier_data.close()

# On lit maintenant le fichier

fichier_a_lire = open("page_produit_data.csv", 'r', newline="")
lire = csv.reader(fichier_a_lire,delimiter=';')
for row in lire:
    print(row)

fichier_a_lire.close()