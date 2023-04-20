def isMonotonic(array):
    asc, desc = True, True
    for i in range(len(array) - 1):
        asc = asc and array[i] <= array[i+1]
        desc = desc and array[i] >= array[i+1]
        if asc == False and desc == False:
            break
    return asc or desc
