import cv2
import numpy as np
import os
import skimage.io

def calculDescriptorSift() :
    images = os.listdir("D:\Docs\Documents\Etudes\ESIR_2\ACI\Projet\dataset")


    descripteurs = []
    nb_keyPoints = []
    for i in range(len(images)) :   
        #print(i)
        img = skimage.io.imread(fname="dataset\\"+images[i])
        #cv2.imshow('Image', img)
        #cv2.waitKey()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('Image en ndg', gray)
        #cv2.waitKey()

        sift = cv2.xfeatures2d.SIFT_create()
        keypoints_sift, descriptors = sift.detectAndCompute(gray, None)

        #print(descriptors)
        if len(keypoints_sift) == 0 : print(images[i])
        else :
            nb_keyPoints.append(len(keypoints_sift))
            for j in range(len(descriptors)) :
                descripteurs.append(descriptors[j])

        #print("Nombre de points d intérets = " + str(len(keypoints_sift)))
        #print(len(descriptors[0]))

        #img = cv2.drawKeypoints(gray,keypoints_sift, None)
        #cv2.imshow('Images des points d interets', img)
        #cv2.waitKey()

    descripteurs_finaux = []
    ind_nb_keyPoints = 0
    ind_descripteurs = 0
    #On parcourt le tableau contenant le nombre de points d'intérêts par image
    while ind_nb_keyPoints < len(nb_keyPoints) :
        #Si l'image i a moins de 10 points d'intérêts, on ne la garde pas et on passe à la suivante
        if nb_keyPoints[ind_nb_keyPoints] < 10 :
            ind_descripteurs = ind_descripteurs + nb_keyPoints[ind_nb_keyPoints]
            ind_nb_keyPoints = ind_nb_keyPoints + 1
        #Sinon on garde seulement 10 points d'intérêts de l'image et on passe à la suivante
        else :
            for l in range(10) :
                descripteurs_finaux.append(descripteurs[ind_descripteurs+l])
            ind_descripteurs = ind_descripteurs + nb_keyPoints[ind_nb_keyPoints]
            ind_nb_keyPoints = ind_nb_keyPoints + 1
    return descripteurs_finaux