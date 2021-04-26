import numpy as np
from skimage.color import rgb2lab, rgb2gray, lab2rgb
from skimage.io import imread, imshow
import matplotlib.pyplot as plt

cat = imread('/home/shovon26/Desktop/sp_effect/cat.jpeg')
lab = rgb2lab(cat)
lab_scaled = (lab + [0, 128, 128]) / [100, 255, 255]
plt.axis('off')
plt.imshow(lab_scaled)
plt.show()


