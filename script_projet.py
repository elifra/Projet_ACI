#from tensorflow.keras.applications.vgg16 import VGG16
#from tensorflow.keras.applications.vgg16 import preprocess_input
#from tensorflow.keras.applications.vgg16 import decode_predictions
#from tensorflow.keras.models import Model
#from tensorflow.keras.preprocessing import image
#from tensorflow.keras import layers

import numpy as np
import os, sys
from statistics import mean

import pre_processing
import histoRGB_descriptor as d_histo
import SIFT_descriptor as d_sift

from sklearn.linear_model import LogisticRegression

table_data = pre_processing.table

def createFileDescripteurHisto() :
    #Création du fichier descripteur_histoRGB
    table_data_descripteurRGB = open("descripteur_histoRGB.txt", "w")
    
    #On récupère les histogrammes RGB calculés pour chaque image
    histos = d_histo.calculHistoRGB()

    #table_data_descripteurRGB.write("id   ")
    for i in range(769):
        if i==768 : table_data_descripteurRGB.write("label" + "\n")
        else : table_data_descripteurRGB.write("x" + str(i) + "   ")
    
    indHisto = 0
    for i in range(len(pre_processing.images)) :
        #table_data_descripteurRGB.write(str(pre_processing.ids[i]) + "   ")
        histoCourantR = histos[indHisto]
        histoCourantG = histos[indHisto+1]
        histoCourantB = histos[indHisto+2]
        for r in range(len(histoCourantR)) :
            table_data_descripteurRGB.write(str(histoCourantR[r]) + "   ")
        for g in range(len(histoCourantG)) :
            table_data_descripteurRGB.write(str(histoCourantG[g]) + "   ")
        for b in range(len(histoCourantB)) :
            if b==len(histoCourantB)-1 and i<len(pre_processing.images)-1: table_data_descripteurRGB.write(str(histoCourantB[b]) + "   " + str(pre_processing.labels[i]) + "\n")
            elif b==len(histoCourantB)-1 and i==len(pre_processing.images)-1 : table_data_descripteurRGB.write(str(histoCourantB[b]) + "   " + str(pre_processing.labels[i]))
            else : table_data_descripteurRGB.write(str(histoCourantB[b]) + "   ")
        indHisto = indHisto + 3
    
    table_data_descripteurRGB.close()

def createFileDescripteurSIFT() :
    #Création du fichier descripteur_SIFT
    table_data_descripteurSIFT = open("descripteur_SIFT.txt", "w")
    
    #On récupère les descripteurs SIFT calculés pour chaque image
    descript = d_sift.calculDescriptorSift()

    #1281 = 1280 attributs (10*128) + colonne du label 
    for i in range(1281):
        if i==1280 : table_data_descripteurSIFT.write("label" + "\n")
        else : table_data_descripteurSIFT.write("x" + str(i) + "   ")

    #1102 = nombre d'images sélectionnées
    ind_descript = 0
    for i in range(1102) :
        #On identifie les 10 points clés de l'image
        p0 = descript[ind_descript]
        p1 = descript[ind_descript + 1]
        p2 = descript[ind_descript + 2]
        p3 = descript[ind_descript + 3]
        p4 = descript[ind_descript + 4]
        p5 = descript[ind_descript + 5]
        p6 = descript[ind_descript + 6]
        p7 = descript[ind_descript + 7]
        p8 = descript[ind_descript + 8]
        p9 = descript[ind_descript + 9]

        #On remplie le fichier des 10 descripteurs par image (10*128 attributs par ligne)
        for ind in range(len(p0)) :
            table_data_descripteurSIFT.write(str(p0[ind]) + "   ")
        
        for ind in range(len(p1)) :
            table_data_descripteurSIFT.write(str(p1[ind]) + "   ")
        
        for ind in range(len(p2)) :
            table_data_descripteurSIFT.write(str(p2[ind]) + "   ")
        
        for ind in range(len(p3)) :
            table_data_descripteurSIFT.write(str(p3[ind]) + "   ")
        
        for ind in range(len(p4)) :
            table_data_descripteurSIFT.write(str(p4[ind]) + "   ")
        
        for ind in range(len(p5)) :
            table_data_descripteurSIFT.write(str(p5[ind]) + "   ")
        
        for ind in range(len(p6)) :
            table_data_descripteurSIFT.write(str(p6[ind]) + "   ")
        
        for ind in range(len(p7)) :
            table_data_descripteurSIFT.write(str(p7[ind]) + "   ")
        
        for ind in range(len(p8)) :
            table_data_descripteurSIFT.write(str(p8[ind]) + "   ")
        
        for ind in range(len(p9)) :
            if ind==len(p9)-1 and i<1101: table_data_descripteurSIFT.write(str(p9[ind]) + "   " + str(pre_processing.labels[i]) + "\n")
            elif ind==len(p9)-1 and i==1101 : table_data_descripteurSIFT.write(str(p9[ind]) + "   " + str(pre_processing.labels[i]))
            else : table_data_descripteurSIFT.write(str(p9[ind]) + "   ")
        ind_descript = ind_descript + 10

    table_data_descripteurSIFT.close()

if __name__ == "__main__":
    """
    createFileDescripteurHisto()
    
    table_descripteurRGB = np.loadtxt("descripteur_histoRGB.txt", dtype="str")
    print(table_descripteurRGB[:1124])
    print("Taille de la table = " + str(table_descripteurRGB.shape))
    """
    createFileDescripteurSIFT()

    table_descripteurSIFT = np.loadtxt("descripteur_SIFT.txt", dtype="str")
    print(table_descripteurSIFT[:1103])
    print("Taille de la table = " + str(table_descripteurSIFT.shape))