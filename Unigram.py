
def unigramGen(word):
    """return binary tuple form of uni-gram"""

    aux = {}
    result = []
    for char in word:
        if char not in aux:
            aux[char] = 1
        else:
            aux[char] += 1
        result.append((char, aux[char]))
    return result


def bitArrayGen(word):
    """return the 130 bit array"""

    commonSymbol = ["!", "#", "$", "%", "&", "*", "+", "-", "/", "@"]

    result = [0 for i in range(210)]

    # translate all the words to lower case
    word = word.lower()

    # split the word as uni-gram form(dictionary)
    unigram = unigramGen(word)

    # word: secure
    # unigram: {"s": 1, "e": 1, "c": 1, "u": 1, "r": 1, "e":2}
    # ord("s") = 97, (ord("s") - 97) * 5 + 1 - 1 = 90
    # bitArray[90] = 1
    for pair in unigram:
        if pair[0].isalpha():
            result[(ord(pair[0]) - 97) * 5 + pair[1] - 1] = 1
        elif pair[0] in commonSymbol:
            result[(commonSymbol.index(pair[0])) * 3 + 130 + pair[1] - 1] = 1
        elif pair[0].isdigit():
            result[(ord(pair[0]) - 49) * 5 + 160 + pair[1] - 1] = 1
    return result


print(unigramGen("secure"))

print(bitArrayGen("**"))
