#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from ImageProcessor import ImageProcessor as IP
from AdvancedFilter import AdvancedFilter as AF

def main():
    img = IP()
    array = img.load('./photo2.png')
    img.display(array)
    img.display(AF.gaussian_blur(array, 10, 5))

if __name__ == '__main__':
    main()
