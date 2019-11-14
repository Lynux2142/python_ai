import numpy as np
from matplotlib.image import imread
from matplotlib import pyplot as plt

class ImageProcessor:
    def load(self, path):
        img = imread(path)
        print(f'Loading image of dimensions {len(img[0])} x {len(img)}')
        return (img)
    def display(self, array):
        plt.imshow(array)
        plt.show()
