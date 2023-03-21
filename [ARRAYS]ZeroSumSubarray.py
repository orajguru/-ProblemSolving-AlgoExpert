def zeroSumSubarray(nums):
    store = set([0])
    sum = 0
    for i in nums:
        sum += i
        if sum in store:
            return True
        store.add(sum)
    return False
            
    
