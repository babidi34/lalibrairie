import requests
from bs4 import BeautifulSoup

fichier_data = open("data.csv","w")
headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://www.lalibrairie.com/livres/des-ailes-d-argent--la-vengeance-d-une-femme-est-douce-et-impitoyable_0-6872120_9782330138516.html"
response = requests.get(url,headers=headers)

# On applique bs pour analyser le contenu de la requête :
parser = BeautifulSoup(response.content, 'html.parser')
body = parser.body

# on récupère nos data et on les place dans des variables
product_page_url = url
titre = body.find(itemprop="name")
print(titre.text)
autor = body.find(itemprop="author")
print(autor.text)
price = body.find(itemprop="price")
print(price.text)
product_description = body.find(id="fiche-technique")
print(product_description.text)
resume = body.find(itemprop="description")
print(resume.text)
collection = body.find("p", {"class":"collections text-gray text-mulit-light"})
collection = collection.find("a", {"class":"text-gray"})
print(collection.text)
image_url = body.find("picture")
image_url = "https://www.lalibrairie.com" + image_url.img['src']
print(image_url)


fichier_data.close()