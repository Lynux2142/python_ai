import time

def generate_rand_int(minimum, maximum):
    now = str(time.clock())
    rnd = float(now[::-1][:3:]) / 1000
    return (minimum + rnd * (maximum - minimum))

def generator(text, sep=' ', option=None):
    '''Option is an optional arg, sep is mandatory'''
    word_list = text.split(sep)
    if (option == 'ordered'):
        word_list.sort(key=lambda x:(not x.islower(), x))
    elif (option == 'unique'):
        word_list = list(dict.fromkeys(word_list))
    elif (option == 'shuffle'):
        rnd_word_list = []
        while (len(word_list)):
            rnd = generate_rand_int(0, len(word_list))
            rnd_word_list.append(word_list[int(rnd)])
            del word_list[int(rnd)]
        word_list = rnd_word_list
    print(word_list)
    for elem in word_list:
        yield elem
