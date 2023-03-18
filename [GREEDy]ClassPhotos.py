def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse = True)
    blueShirtHeights.sort(reverse = True)
    firstRow = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
    for i in range(len(redShirtHeights)):
        redHeights = redShirtHeights[i]
        blueHeights = blueShirtHeights[i]
        if firstRow == "RED":
            if redHeights >= blueHeights:
                return False
        else:
            if redHeights <= blueHeights:
                return False
    return True
