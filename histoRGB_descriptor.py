import sys
import skimage.io
import skimage.viewer
import os
from matplotlib import pyplot as plt

images = os.listdir("D:\Docs\Documents\Etudes\ESIR_2\ACI\Projet\dataset")
os.chdir("dataset")

# read original image, in full color, based on command
# line argument
image = skimage.io.imread(fname=images[0])

# display the image
viewer = skimage.viewer(image)
viewer.show()