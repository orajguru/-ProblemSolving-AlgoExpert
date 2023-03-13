def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    min, pair = float("inf"), []
    i, j = 0, 0
    while i < len(arrayOne) and j < len(arrayTwo):
        num1, num2 = arrayOne[i], arrayTwo[j]
        curr = abs(num1 - num2)
        if curr < min:
            min = curr
            pair = [num1, num2]
        if num1 > num2:
            j += 1
        else:
            i += 1
    return pair
    
    
