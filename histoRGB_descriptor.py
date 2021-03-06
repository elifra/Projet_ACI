import sys
import skimage.io
import os
import numpy as np
from skimage.viewer import ImageViewer
from matplotlib import pyplot as plt
from statistics import mean

def calculHistoRGB() :
    images = os.listdir("D:\Docs\Documents\Etudes\ESIR_2\ACI\Projet\dataset")

    # read original image, in full color, based on command
    # line argument
    #image = skimage.io.imread(fname="dataset\\"+images[268])
    #print("Taille de l'image : " + str(image.shape))

    # display the image
    #viewer = ImageViewer(image)
    #viewer.show()

    # tuple to select colors of each channel line
    colors = ("r", "g", "b")
    channel_ids = (0, 1, 2)

    histos = []
    for i in range(len(images)):
        # create the histogram plot, with three lines, one for
        # each color
        plt.xlim([0, 256])
        image = skimage.io.imread(fname="dataset\\"+images[i])
        for channel_id, c in zip(channel_ids, colors):
            histogram, bin_edges = np.histogram(
                image[:, :, channel_id], bins=256, range=(0, 255)
            )
            histos.append(histogram)
            #nbValeurs = 0
            #for i in histogram:
            #    nbValeurs = nbValeurs+i
            #print("Nombres de valeurs histo : " + str(nbValeurs))
            # canal = image[:, :, channel_id]
            # viewer = ImageViewer(canal)
            # viewer.show()
            #plt.plot(bin_edges[0:-1], histogram, color=c)
            #plt.xlabel("Color value")
            #plt.ylabel("Pixels")
            #plt.title(c)
            #plt.show()
    return histos