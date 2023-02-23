def generateDocument(characters, document):
    charCount = {}
    for char in characters:
        if char not in charCount:
            charCount[char] = 0
        charCount[char] += 1
    for char in document:
        if char not in charCount or charCount[char] == 0:
            return False
        charCount[char] -= 1
    return True
