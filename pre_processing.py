import os
import numpy as np

#Création du fichier dataset
tab_data = open("datas.txt", "w")

#Stockage du jeu de données
images = os.listdir("D:\Docs\Documents\Etudes\ESIR_2\ACI\Projet\dataset")
ids = [] #tableau des id --> noms des images simplifiés
labels = [] #tableau des labels

#print("Nombre d'images = " + str(len(images)))

tab_data.write("id  label\n")

identifiant = 1
for i in range(len(images)):
    ids.append(identifiant)
    if "cloudy" in images[i]:
        tab_data.write(str(ids[i])+"  0\n")
        labels.append("cloudy")
    elif "rain" in images[i]:
        tab_data.write(str(ids[i])+"  1\n")
        labels.append("rain")
    elif "shine" in images[i]:
        tab_data.write(str(ids[i])+"  2\n")
        labels.append("shine")
    elif "sunrise" in images[i] and i==len(images)-1:
        tab_data.write(str(ids[i])+"  3")
        labels.append("sunrise")
    elif "sunrise" in images[i]:
        tab_data.write(str(ids[i])+"  3\n")
        labels.append("sunrise")
    identifiant = identifiant+1

tab_data.close()

"""
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

tab_data_lecture = open("datas.txt", "r")
lines = tab_data_lecture.readlines()
print("Nombre de lignes = " + str(len(lines)))
tab_data_lecture.close()
"""
table = np.loadtxt("datas.txt", dtype="str")
"""
print(table[:1123])
print("Taille de la table = " + str(table.shape))
"""