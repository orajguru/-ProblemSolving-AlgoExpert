def minimumWaitingTime(queries):
    queries.sort(reverse = True)
    return sum(i * value for i, value in enumerate(queries))
