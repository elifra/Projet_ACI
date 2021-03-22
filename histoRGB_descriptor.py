import sys
import skimage.io
import os
from skimage.viewer import ImageViewer
from matplotlib import pyplot as plt

images = os.listdir("D:\Docs\Documents\Etudes\ESIR_2\ACI\Projet\dataset")

# read original image, in full color, based on command
# line argument
image = skimage.io.imread(fname="dataset\\"+images[0])

# display the image
viewer = ImageViewer(image)
viewer.show()