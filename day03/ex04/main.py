#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from ImageProcessor import ImageProcessor as IP
from AdvancedFilter import AdvancedFilter as AF

def main():
    img = IP()
    array = img.load('./42AI.png')
    img.display(array)
    img.display(AF.mean_blur(array, 10))
    print()

if __name__ == '__main__':
    main()
