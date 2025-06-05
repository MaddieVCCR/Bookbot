def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    toprocess = text.lower()
    charcount = {}
    for i in toprocess:
        if i in charcount:
           charcount[f"{i}"] +=1
        else:
            charcount[f"{i}"] =1
    return charcount

def
    
    