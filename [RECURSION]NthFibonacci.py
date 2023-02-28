def getNthFib(n):
    fibo = [0,1]
    for i in range(n-2):
        fibo.append(fibo[i] + fibo[i+1])
    return fibo[n-1]
