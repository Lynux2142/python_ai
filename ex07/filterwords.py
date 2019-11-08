#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from sys import argv
import string

def main():
    try:
        assert (len(argv) == 3)
        text = argv[1]
        n = int(argv[2])
    except:
        print('ERROR')
    else:
        text = text.translate({ord(char): None for char in string.punctuation})
        res = []
        for word in text.split():
            if (len(word) > n):
                res.append(word)
        print('ERROR' if (not res) else res)

if __name__ == '__main__':
    main()
