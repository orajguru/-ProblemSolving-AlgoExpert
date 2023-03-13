def isValidSubsequence(array, sequence):
    arrInd = 0
    seqInd = 0
    while arrInd < len(array) and seqInd < len(sequence):
        if array[arrInd] == sequence[seqInd]:
            seqInd += 1
        arrInd += 1
    return seqInd == len(sequence)
