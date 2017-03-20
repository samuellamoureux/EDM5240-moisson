### MES COMMENTAIRES ET CORRECTIONS SONT MARQUÉS PAR TROIS DIÈSES

### Les phrases ci-dessous n'étaient pas en commentaires et faisaient planter le script
# Ce code permet d'aller chercher les url de tous les contrats publics donnés par la commission canadienne de sureté nucléaire au 2e trimestre de 2016-2017. 
# Ceux-ci sont imprimés dans un nouveau fichier csv nommé "contrats-nuke1.csv"

### Script intéressant, mais qui ne fait que la première étape d'une démarche de moissonnage de données
### Une fois les URL trouvés, il faut ouvrir la page vers laquelle chacun pointe pour aller recueillir les infos relatives à chaque contrat

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
    
for ligne in page.find_all("tr")[1:]: ### Bien, tu évites de ramasser les entêtes du tableau
    contrat = []
    debut = "http://www.suretenucleaire.gc.ca/fra/transparency/"
    lien = debut + ligne.a["href"]
    print(lien)
    contrat.append(lien)

    contenu2 = requests.get(lien, headers=entetes)
    page2 = BeautifulSoup(contenu2.text, "html.parser")

    # print(len(page2.find_all("tr")))
    for ligne in page2.find_all("tr"):

### On se rend compte, en examinant le code HTML, que tous les détails des contrats sont dans un <tr> qui ne contient que deux choses:
### Un <th> où se trouve le titre de la ligne et un <td> où se trouve l'information qui nous intéresse
### Il suffit donc de ne recueillir que le contenu du <td>
        contrat.append(ligne.td.text.strip())

    print(contrat)

### On peut écrire une ligne de notre fichier CSV après le moissonnage de chaque contrat
    fich = "contrats-nuke1-JHR.csv"
    achille = open(fich,"a")
    talon = csv.writer(achille)
    talon.writerow(contrat)