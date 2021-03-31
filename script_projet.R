# ----- Chargement des fonctions utiles
#install.packages("gtools")
#library(gtools)
#source("fonctions_utiles.R")
#install.packages("e1071")
#library("e1071")
#install.packages("nnet")
#library(nnet)
library(rpart)
install.packages("rpart.plot")
library(rpart.plot)
source("fonctions_utiles.R")

#----------------------------------------------------------
# Première partie : Apprentissage par régression logistique
#----------------------------------------------------------

  #------------------------------
  # Descripteur : Histogramme RGB
  #------------------------------

# ----- Chargement des données
ids_labels = read.table("./data_Projet/datas.txt", header = T)
data_histoRGB = read.table("./data_Projet/descripteur_histoRGB.txt", header = T)

table(data_histoRGB$label)

# ----- Separation Apprentissage/Test 

nall = nrow(data_histoRGB) #total number of rows in data
ntrain = floor(0.7 * nall) # number of examples (rows) for train: 70% (vous pouvez changer en fonction des besoins)
ntest = nall - ntrain # number of examples for test: le reste

set.seed(20) # choix d'une graine pour le tirage alÃ©atoire
index = sample(nall) # permutation alÃ©atoire des nombres 1, 2, 3 , ... nall

histoRGB_app = data_histoRGB[index[1:ntrain],] # création du jeu d'apprentissage
histoRGB_test = data_histoRGB[index[(ntrain+1):(ntrain+ntest)],] # création du jeu de test
print(nrow(histoRGB_app))
print(nrow(histoRGB_test))

# ----- Estimation du modele de regression logistique sur les donnÃ©es d apprentissage

tr = rpart(label~., data = histoRGB_app, control = list(minbucket = 1,cp = 0, minsplit = 1))
rpart.plot(tr, extra = 1)

pa = predict(tr, histoRGB_app, type = 'vector')
print(pa)

predictionCorecte = sum(predict(tr, histoRGB_test, type = "vector")==histoRGB_app[,770])
print(predictionCorecte)
