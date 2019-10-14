def text_analyzer(prompt=None):
    '''This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.'''
    while (prompt is None or len(prompt) == 0):
        prompt = input("What is the text to analyze ?\n")
    text_len = str(len(prompt))
    text_char = {
        'maj': 0,
        'lower': 0,
        'space': 0,
        'punctuation': 0
    }
    print("The text contains " + text_len + " characters:")
    for letter in prompt:
        if letter.isupper():
            text_char["maj"] += 1
        elif letter.islower():
            text_char["lower"] += 1
        elif letter == " ":
            text_char["space"] += 1
        elif letter in "?.,!;:" :
            text_char["punctuation"] += 1
    print("- " + str(text_char["maj"]) + " upper letters")
    print("- " + str(text_char["lower"]) + " lower letters")
    print("- " + str(text_char["punctuation"]) + " punctuation marks")
    print("- " + str(text_char["space"]) + " spaces")
