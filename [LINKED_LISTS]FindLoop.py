class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def findLoop(head):
    visited = set()
    while head:
        if head not in visited:
            visited.add(head)
        else:
            return head
        head = head.next
