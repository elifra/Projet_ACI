# ----- Chargement des fonctions utiles
#install.packages("gtools")
#library(gtools)
#source("fonctions_utiles.R")
#install.packages("e1071")
#library("e1071")
#install.packages("nnet")
#library(nnet)

#----------------------------------------------------------
# Première partie : Apprentissage par arbre de décision
#----------------------------------------------------------
library(rpart)
install.packages("rpart.plot")
library(rpart.plot)
source("fonctions_utiles.R")

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
ntmp = nall - ntrain 
nvalid = floor(0.5*ntmp) # number of examples for test: 15%
ntest = ntmp - nvalid # number of examples for test: 15% restant

set.seed(20) # choix d'une graine pour le tirage alÃ©atoire
index = sample(nall) # permutation alÃ©atoire des nombres 1, 2, 3 , ... nall

histoRGB_app = data_histoRGB[index[1:ntrain],] # création du jeu d'apprentissage
histoRGB_val = data_histoRGB[index[(ntrain+1):(ntrain+nvalid)],] # création du jeu de validation
histoRGB_test = data_histoRGB[index[(ntrain+nvalid+1):(ntrain+nvalid+ntest)],] # création du jeu de test
print(nrow(histoRGB_app))
print(nrow(histoRGB_val))
print(nrow(histoRGB_test))

# ----- Construction de l'arbre Tmax

tr = rpart(label~., data = histoRGB_app, control = list(minbucket = 1,cp = 0, minsplit = 1))
rpart.plot(tr, extra = 1)

predictionCorecte = sum(predict(tr, histoRGB_test, type = "vector")==histoRGB_test[,769])
print(predictionCorecte)

prediction = predict(tr, histoRGB_test, type = 'vector')
#print(prediction)

matConfusion_arbre=table(histoRGB_test$label, prediction,dnn=list('actual','predicted'))
print(matConfusion_arbre)

# ----- Élagage de l'arbre

rev(tr$cptable[,1])

for (val in  rev(tr$cptable[,1])){
  print("valeur de cp : ")
  print(val)
  tr_elague = prune(tr, cp = val)
  rpart.plot(tr_elague, extra = 1)
  
  #Apprentissage
  predictionCorecte = sum(predict(tr_elague, histoRGB_app, type = "vector")==histoRGB_app[,769])
  print("nombre de lignes de l'ensemble d'apprentissage")
  print(nrow(histoRGB_app))
  print("nombre de bonnes prédictions de cet arbre sur l'ensemble d'apprentissage : ")
  print(predictionCorecte)
  print("")
  
  #Validation
  predictionCorecte = sum(predict(tr_elague, histoRGB_val, type = "vector")==histoRGB_val[,769])
  print("nombre de lignes de l'ensemble de validation")
  print(nrow(histoRGB_val))
  print("nombre de bonnes prédictions de cet arbre sur l'ensemble de validation : ")
  print(predictionCorecte)
  print("")
}
