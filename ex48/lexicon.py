

WORD_TYPES = {
    "north" : "direction",
    "south" : "direction", 
    "east" : "direction",
    "west" : "direction",
    "go" : "verb",
    "kill" : "verb",
    "eat" : "verb",
    "the" : "stop",
    "in" : "stop",
    "of" : "stop",
    "bear" : "noun",
    "princess" : "noun",
}

def convert_number(word):
    try:
        return int(word)
    except:
        return None

def scan(sentence):
    words = sentence.split()
    results = []

    for word in words:
        word_type = WORD_TYPES.get(word)
        
        if word_type == None:
            # it might be a number, so try converting
            number = convert_number(word)

            if number != None:
                results.append(('number', number))
            else:
                results.append(('error', word))
        else:
            results.append((word_type, word))
   
    return results
