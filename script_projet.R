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
nvalid = floor(0.5*ntmp) # number of examples for valid: 15%
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

predictionCorecte = sum(predict(tr, histoRGB_test, type = "class")==histoRGB_test[,769])
print(predictionCorecte)

prediction = predict(tr, histoRGB_test, type = 'class')
#print(prediction)

matConfusion_arbre=table(histoRGB_test$label, prediction,dnn=list('actual','predicted'))
print(matConfusion_arbre)

# ----- Élagage de l'arbre

rev(tr$cptable[,1])

for (val in  rev(tr$cptable[,1])){
  print("valeur de cp : ")
  print(val)
  tr_elague = prune(tr, cp = val)
  rpart.plot(tr_elague, extra = 1, box.palette = "Blues")
  
  #Apprentissage
  predictionCorecte = sum(predict(tr_elague, histoRGB_app, type = "class")==histoRGB_app[,769])
  print("nombre de lignes de l'ensemble d'apprentissage")
  print(nrow(histoRGB_app))
  print("nombre de bonnes prédictions de cet arbre sur l'ensemble d'apprentissage : ")
  print(predictionCorecte)
  print("")
  
  #Validation
  predictionCorecte = sum(predict(tr_elague, histoRGB_val, type = "class")==histoRGB_val[,769])
  print("nombre de lignes de l'ensemble de validation")
  print(nrow(histoRGB_val))
  print("nombre de bonnes prédictions de cet arbre sur l'ensemble de validation : ")
  print(predictionCorecte)
  print("")
}

# ----- Estimation de l'erreur de généralisation

tr_elague = prune(tr, cp = 0.009398496) 
rpart.plot(tr_elague, extra = 1)
print("Mauvaises prédictions : ")
mauvaisesPredictions = sum(predict(tr_elague, histoRGB_test, type = "class")!=histoRGB_test[,769])
print(mauvaisesPredictions)
print("Erreur de Generalisation : ")
print(mauvaisesPredictions/nrow(histoRGB_test))


  #------------------------------
  # Descripteur : SIFT
  #------------------------------

# ----- Chargement des données
data_SIFT = read.table("./data_Projet/descripteur_SIFT.txt", header = T)

table(data_SIFT$label)

# ----- Separation Apprentissage/Test 

nall = nrow(data_SIFT) #total number of rows in data
ntrain = floor(0.7 * nall) # number of examples (rows) for train: 70% (vous pouvez changer en fonction des besoins)
ntmp = nall - ntrain 
nvalid = floor(0.5*ntmp) # number of examples for valid: 15%
ntest = ntmp - nvalid # number of examples for test: 15% restant

set.seed(20) # choix d'une graine pour le tirage alÃ©atoire
index = sample(nall) # permutation alÃ©atoire des nombres 1, 2, 3 , ... nall

SIFT_app = data_SIFT[index[1:ntrain],] # création du jeu d'apprentissage
SIFT_val = data_SIFT[index[(ntrain+1):(ntrain+nvalid)],] # création du jeu de validation
SIFT_test = data_SIFT[index[(ntrain+nvalid+1):(ntrain+nvalid+ntest)],] # création du jeu de test
print(nrow(SIFT_app))
print(nrow(SIFT_val))
print(nrow(SIFT_test))

# ----- Construction de l'arbre Tmax

tr = rpart(label~., data = SIFT_app, control = list(minbucket = 1,cp = 0, minsplit = 1))
rpart.plot(tr, extra = 1)

predictionCorecte = sum(predict(tr, SIFT_test, type = "class")==SIFT_test[,1281])
print(predictionCorecte)

prediction = predict(tr, SIFT_test, type = 'class')
#print(prediction)

matConfusion_arbre=table(SIFT_test$label, prediction,dnn=list('actual','predicted'))
print(matConfusion_arbre)

# ----- Élagage de l'arbre

rev(tr$cptable[,1])

for (val in  rev(tr$cptable[,1])){
  print("valeur de cp : ")
  print(val)
  tr_elague = prune(tr, cp = val)
  rpart.plot(tr_elague, extra = 1, box.palette = "Blues")
  
  #Apprentissage
  predictionCorecte = sum(predict(tr_elague, SIFT_app, type = "class")==SIFT_app[,1281])
  print("nombre de lignes de l'ensemble d'apprentissage")
  print(nrow(SIFT_app))
  print("nombre de bonnes prédictions de cet arbre sur l'ensemble d'apprentissage : ")
  print(predictionCorecte)
  print("")
  
  #Validation
  predictionCorecte = sum(predict(tr_elague, SIFT_val, type = "class")==SIFT_val[,1281])
  print("nombre de lignes de l'ensemble de validation")
  print(nrow(SIFT_val))
  print("nombre de bonnes prédictions de cet arbre sur l'ensemble de validation : ")
  print(predictionCorecte)
  print("")
}

# ----- Estimation de l'erreur de généralisation

tr_elague = prune(tr, cp = 0.007604563) 
rpart.plot(tr_elague, extra = 1)
print("Mauvaises prédictions : ")
mauvaisesPredictions = sum(predict(tr_elague, SIFT_test, type = "class")!=SIFT_test[,1281])
print(mauvaisesPredictions)
print("Erreur de Generalisation : ")
print(mauvaisesPredictions/nrow(SIFT_test))


#----------------------------------------------------------
# Deuxième partie : Apprentissage par Random Forest
#----------------------------------------------------------
library(rpart)
library(rpart.plot)
install.packages("randomForest")
library(randomForest)
source("fonctions_utiles.R")

  #------------------------------
  # Descripteur : Histogramme RGB
  #------------------------------

data_histoRGB = read.table("./data_Projet/descripteur_histoRGB.txt", header = T)
table(data_histoRGB$label)

# ---------- Separation Apprentissage/Validation/Test

nall = nrow(data_histoRGB) #total number of rows in data
ntrain = floor(0.7 * nall) # number of rows for train: 70% (vous pouvez changer en fonction des besoins)
ntest = nall - ntrain # number of rows for test: le reste

set.seed(20) # choix d une graine pour le tirage aléatoire
index = sample(nall) # permutation aléatoire des nombres 1, 2, 3 , ... nall

histoRGB_app = data_histoRGB[index[1:ntrain],] # création du jeu d'apprentissage
histoRGB_test = data_histoRGB[index[(ntrain+1):(ntrain+ntest)],] # création du jeu de test
print(nrow(histoRGB_app))
print(nrow(histoRGB_test))

# ---------- Construction de la foret (3 arbres)
labels = as.factor(histoRGB_app$label)
foret = randomForest(x = histoRGB_app, y = labels, ntree = 1, norm.votes=FALSE)

# ---------- Informations sur la forêt
print(foret)

# ---------- Calcul taux de bonnes classifications sur jeu d'apprentissage
predictionsCorrectes = sum(predict(foret, histoRGB_app)==histoRGB_app$label)
print("Taux de bonnes classifications jeu d'apprentissage")
print(predictionsCorrectes/nrow(histoRGB_app))

# ---------- Calcul erreur empirique et réelle
mauvaisesPredictions = sum(predict(foret, histoRGB_app)!=histoRGB_app$label)
print("Erreur empirique")
print(mauvaisesPredictions/nrow(histoRGB_app))

mauvaisesPredictions = sum(predict(foret, histoRGB_test)!=histoRGB_test$label)
print("Erreur réelle")
print(mauvaisesPredictions/nrow(histoRGB_test))
