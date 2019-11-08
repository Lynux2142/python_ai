#!/usr/local/bin/python3

import os

def start_install():
    os.system('curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh > miniconda3.sh')
    os.system('bash miniconda3.sh -b -p /sgoinfre/goinfre/Perso/lguiller/miniconda3')

    export = 'export PATH="/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin:$PATH"\n'
    f = open(os.path.expanduser('~/.zshrc'), 'a+')
    file = f.read()
    if (file.find(export) == -1):
        f.write(export)
    os.system('source ~/.zshrc')
    os.environ['PATH'] = "/sgoinfre/goinfre/Perso/lguiller/miniconda3/bin:$PATH"
    os.system('/bin/rm -f miniconda3.sh')
    print('Python has been installed.')

def main():
    miniconda = '/sgoinfre/goinfre/Perso/lguiller/miniconda3'
    if (os.path.isdir(miniconda) == True):
        responce = input('Python is already installed, do you want to reinstall it ?\n[yes|no]> ')
        if (responce == 'yes'):
            os.system('rm -rf {}'.format(miniconda))
            print('Pyton has been removed.')
            start_install()
        else:
            print('exit.')
    else:
        start_install()

if __name__ == '__main__':
    main()
