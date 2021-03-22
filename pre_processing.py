import os

#Création du fichier dataset
tab_data = open("dataset.txt", "w")

#Stockage du jeu de données
images = os.listdir("D:\Docs\Documents\Etudes\ESIR_2\ACI\Projet\dataset")

ids = [] #tableau des id --> noms des images simplifiés
labels = [] #tableau des labels

identifiant = 1
for i in range(len(images)):
    ids.append(identifiant)
    if "cloudy" in images[i]:
        tab_data.write(images[i]+"  0\n")
        labels.append("0")
    elif "rain" in images[i]:
        tab_data.write(images[i]+"  1\n")
        labels.append("1")
    elif "shine" in images[i]:
        tab_data.write(images[i]+"  2\n")
        labels.append("2")
    elif "sunrise" in images[i]:
        tab_data.write(images[i]+"  3\n")
        labels.append("3")
    identifiant = identifiant+1

nb0 = 0
nb1 = 0
nb2 = 0
nb3 = 0
for l in range(len(labels)):
    if labels[l]=="0":
        nb0 = nb0 + 1
    elif labels[l]=="1":
        nb1 = nb1 + 1
    elif labels[l]=="2":
        nb2 = nb2 + 1
    elif labels[l]=="3":
        nb3 = nb3 + 1
print("Nombre de classes cloudy : " + str(nb0))
print("Nombre de classes rain : " + str(nb1))
print("Nombre de classes shine : " + str(nb2))
print("Nombre de classes sunrise : " + str(nb3))

tab_data.close()