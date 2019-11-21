#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from ImageProcessor import ImageProcessor as IP
from ColorFilter import ColorFilter as CF

def main():
    img = IP()
    array = img.load('./photo2.png')
    img.display(CF.to_red(array))

if __name__ == '__main__':
    main()
