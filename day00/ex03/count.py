import string
from sys import exit

def text_analyzer(text = ''):
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    try:
        assert (text)
    except:
        text = input('What is the text to analyse?\n>> ')
    upper_letter = 0
    lower_letter = 0
    punctuation_marks = 0
    spaces = 0

    for letter in text:
        if (letter.isupper()):
            upper_letter += 1
        elif (letter.islower()):
            lower_letter += 1
        elif letter in string.punctuation:
            punctuation_marks += 1
        elif (letter == ' '):
            spaces += 1
    print('The text contains {} characters:'.format(len(text)))
    print('- {} upper letters'.format(upper_letter))
    print('- {} lower letters'.format(lower_letter))
    print('- {} punctuation marks'.format(punctuation_marks))
    print('- {} spaces'.format(spaces))
