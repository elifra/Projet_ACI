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

table_data = pre_processing.table

def createFileDescripteurHisto() :
    #Création du fichier descripteur_histoRGB
    table_data_descripteurRGB = open("descripteur_histoRGB.txt", "w")
    
    #On récupère les histogrammes RGB calculés pour chaque image
    histos = d_histo.calculHistoRGB()

    indHisto = 0
    for i in range(len(pre_processing.images)) :
        table_data_descripteurRGB.write(str(pre_processing.ids[i]) + "   ")
        histoCourantR = histos[indHisto]
        histoCourantG = histos[indHisto+1]
        histoCourantB = histos[indHisto+2]
        for r in range(len(histoCourantR)) :
            table_data_descripteurRGB.write(str(histoCourantR[r]) + "   ")
        for g in range(len(histoCourantG)) :
            table_data_descripteurRGB.write(str(histoCourantG[g]) + "   ")
        for b in range(len(histoCourantB)) :
            if b==len(histoCourantB)-1 and i<=len(pre_processing.images): table_data_descripteurRGB.write(str(histoCourantB[b]) + "\n")
            else : table_data_descripteurRGB.write(str(histoCourantB[b]) + "   ")
        indHisto = indHisto + 3
    
    table_data_descripteurRGB.close()


if __name__ == "__main__":
    createFileDescripteurHisto()
    
    table_descripteurRGB = np.loadtxt("descripteur_histoRGB.txt", dtype="str")
    print(table_descripteurRGB[:1123])
    print("Taille de la table = " + str(table_descripteurRGB.shape))