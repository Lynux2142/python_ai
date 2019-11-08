#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

from sys import argv, exit, stdout

def main():
    if (len(argv) == 1):
        exit(0)
    try:
        assert (len(argv) > 1)
        for elem in argv[1:]:
            assert (elem.replace(' ', '').isalnum())
    except:
        print('ERROR')
        exit(1)
    else:
        morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.', '0': '-----',
            ' ': '/'
        }
        data = argv[1:]
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                stdout.write(morse_dict[data[i][j].upper()])
                if (j < len(data[i]) - 1):
                    stdout.write(' ')
            if (i < len(data) - 1):
                stdout.write(' / ')
        print()

if __name__ == '__main__':
    main()
