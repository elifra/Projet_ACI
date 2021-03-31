import cv2
import numpy as np
import os

#def calculDescriptorSift() :
images = os.listdir("D:\Docs\Documents\Etudes\ESIR_2\ACI\Projet\dataset")

img = cv2.imread("dataset\\"+images[700])
cv2.imshow('Image', img)
cv2.waitKey()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image en ndg', gray)
cv2.waitKey()

sift = cv2.xfeatures2d.SIFT_create()
keypoints_sift, descriptors = sift.detectAndCompute(gray, None)

print("Nombre de points d intérets = " + str(len(keypoints_sift)))
print(len(descriptors[0]))

img = cv2.drawKeypoints(gray,keypoints_sift, None)
cv2.imshow('Images des points d interets', img)
cv2.waitKey()