import numpy as np
from skimage.color import rgb2lab, rgb2gray, lab2rgb
from skimage.io import imread, imshow
import matplotlib.pyplot as plt

img_gs = imread('/home/shovon26/Desktop/sp_effect/crayons.jpeg', as_gray = True)
fig, ax = plt.subplots(figsize = (9, 16))
imshow(img_gs, ax = ax)
ax.set_title('Grayscale image')
ax.axis('off')
plt.show()

