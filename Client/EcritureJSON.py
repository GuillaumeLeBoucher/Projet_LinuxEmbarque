import json
 

#En admettant que le json se nomme fichier.json
with open("./App-Web/src/app/image-detail/shared/data.json", "r") as f_read:
    dico = json.load(f_read)
print(dico)
#Enregistrement du nouveau contenu au bon endroit (à définir)
NbPhotos = len(dico["PhotoPath"])
Listephotos = dico["PhotoPath"]
Listephotos.append({'id': NbPhotos+1, 'category': 'NewCat', 'caption': 'Test Json for NewCat', 'url': 'assets/img/test_01.jpg'})
dico["PhotoPath"] = Listephotos
print (dico)
#Sauvegarde (écrasement)
with open("./App-Web/src/app/image-detail/shared/data.json", "w") as f_write:
    json.dump(dico, f_write)