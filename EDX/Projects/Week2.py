def word_distribution(inputText):   
    parts = inputText.lower().split(' ')
    #print(parts)

    #create dictionary
    dicOut = dict()
    for p in parts:
        if not p[len(p) - 1].isalpha():
            p = p[:-1] #remove last char case punctuation symbol
        
        if not p[0].isalpha():
            p = p[1:] #remove first char case punctuation symbol

        if p in dicOut:
            dicOut[p] +=1
        else:
            dicOut[p] = 1

    return dicOut


print(word_distribution("Hello. How are you? Please say hello if you don’t love me!"))
print(word_distribution("That's when I saw Jane (John's sister)!"))