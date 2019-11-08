#!/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin/python

def main():
    langanges = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
    }
    for language, creator in langanges.items():
        print(f'{language} was created by {creator}')

if __name__ == '__main__':
    main()
