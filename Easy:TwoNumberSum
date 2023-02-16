def twoNumberSum(array, targetSum):
    dict = {}
    for i, n in enumerate(array):
        rem = targetSum - n
        if rem in dict.values():
            return [rem, n]
        dict[i] = n
    return []
    
            
        
