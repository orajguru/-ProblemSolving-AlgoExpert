def sunsetViews(buildings, direction):
    stack = []
    max = 0
    for i in range(len(buildings)):
        if direction == "EAST":
            if buildings[len(buildings)-1-i] > max:
                stack.append(len(buildings)-1-i)
                max = buildings[len(buildings)-1-i]
        elif direction == "WEST":
            if buildings[i] > max:
                stack.append(i)
                max = buildings[i]
    if direction == "EAST":
        stack = stack[::-1]
    return stack
