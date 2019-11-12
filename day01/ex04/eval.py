class Evaluator:
    def zip_evaluate(coefs, words):
        try: assert (len(coefs) == len(words))
        except: return (-1)
        else:
            total = 0
            for coef, word in zip(coefs, words):
                total += float(len(word)) * coef
            return (total)
    def enumerate_evaluate(coefs, words):
        try: assert (len(coefs) == len(words))
        except: return (-1)
        else:
            total = 0
            for i, coef in enumerate(coefs, 0):
                total += float(len(words[i])) * coef
            return (total)
