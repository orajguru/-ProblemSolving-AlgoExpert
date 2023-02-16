def firstNonRepeatingCharacter(string):
    freq = {}
    for char in string:
        freq[char] = freq.get(char,0) + 1
    for i in range(len(string)):
        char = string[i]
        if freq[char] == 1:
            return i
    return -1
