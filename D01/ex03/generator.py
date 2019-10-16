import random 

def generator(text, sep=" ", option=None):
    array = text.split(sep)
    if (option == None):
        for word in array:
            yield word
    
    elif (option == "ordered"):
        array.sort()
        for word in array:
            yield word

    elif (option == "unique"):
        unique = list()
        for word in array:
            if word not in unique:
                unique.append(word)
                yield word
    
    elif (option == "shuffle"):
        random.shuffle(array)
        for word in array:
            yield word

    else:
        exit("Unknown Option")


text = "Le Lorem Ipsum est simplement du faux est texte."
#for word in generator(text, sep=" "):
#    print(word)

#for word in generator(text, sep=" ", option="ordered"):
#    print(word)

#for word in generator(text, sep=" ", option="unique"):
 #   print(word)

for word in generator(text, sep=" ", option="caca"):
    print(word)