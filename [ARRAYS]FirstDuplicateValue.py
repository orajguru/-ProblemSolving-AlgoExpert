def firstDuplicateValue(array):
    sol = set()
    for value in array:
        if value in sol:
            return value
        sol.add(value)
    return -1
