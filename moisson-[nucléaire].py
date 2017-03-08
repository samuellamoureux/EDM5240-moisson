Ce code permet d'aller chercher les url de tous les contrats publics donnés par la commission canadienne de sureté nucléaire au 2e trimestre de 2016-2017. 
Ceux-ci sont imprimés dans un nouveau fichier csv nommé "contrats-nuke1.csv"




#coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

url = "http://www.suretenucleaire.gc.ca/fra/transparency/contracts.cfm?listing_id=59"


entetes = {
    "User-Agent":"Samuel Lamoureux - Requête journalistique",
    "From":"sam.lamoureux@hotmail.com"
}

contenu = requests.get(url, headers=entetes)

page = BeautifulSoup(contenu.text, "html.parser")


    
for ligne in page.find_all("tr")[1:]:
    debut = "http://www.suretenucleaire.gc.ca/fra/transparency/"
    lien = debut + ligne.a["href"]
    print(lien)
    
    fich = "contrats-nuke1.csv"
    achille = open(fich,"a")
    talon = csv.writer(achille)
    talon.writerow(lien)
    



   
