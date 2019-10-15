import sys

def evaluate(coef, words):
    if (not isinstance(coef, list) or not isinstance(words, list)):
        return (-1)
    if (len(coef) != len(words)):
        return (-1)
    if (not all(isinstance(item, float) for item in coef) or not all(isinstance(item, str) for item in words)):
        return (-1)
    score = float(0.0)
    for item_c, item_w in zip(coef, words):
        add = float(item_c * len(item_w))
        score += add
    return score

#words = ["Le", "Lorem", "Ipsum", "est", "simple"]
#coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
#score = evaluate(coefs, words)
#print(score)

#words = ["L","Le"]
#coefs = [1.0, 0.5]
#score = evaluate(coefs, words)
#print(score)
