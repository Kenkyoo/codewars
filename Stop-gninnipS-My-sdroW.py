def spin_words(sentence):
    y = []
    for x in sentence.split():
        if len(x) >= 5:
            y.append(x[::-1])
        else:
            y.append(x)
    print(" ".join(y))

spin_words("Hey fellow warriors")
spin_words("This is a test")
spin_words("This is another test")