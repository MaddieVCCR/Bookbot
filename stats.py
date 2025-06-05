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

def sortlist(chars):
    report = []
    for char, count in chars.items():
        if char.isalpha():
            test = {
                "char": char,
                "num": count}
            report.append(test)
    report.sort(reverse = True, key=sort_on)
    return report

def sort_on(dict):
    return dict["num"]