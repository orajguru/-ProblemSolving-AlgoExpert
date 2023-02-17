class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode.next is not None:
        if currentNode.value == currentNode.next.value:
            currentNode.next = currentNode.next.next
        else:
            currentNode = currentNode.next
    return linkedList
        
