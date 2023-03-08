def groupAnagrams(words):
    sol = {}
    for word in words:
        str = "".join(sorted(word))
        if str in sol:
            sol[str].append(word)
        else:
            sol[str] = [word]
    return list(sol.values())
            
