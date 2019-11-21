#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from ImageProcessor import ImageProcessor as IP
from ColorFilter import ColorFilter as CF

def main():
    img = IP()
    array = img.load('./42AI.png')
    img.display(array)
    img.display(CF.invert(array))
    img.display(array)
    img.display(CF.to_grayscale(array, 'w'))

if __name__ == '__main__':
    main()
