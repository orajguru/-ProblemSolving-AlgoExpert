class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    sol = LinkedList(0)
    temp = sol
    carry = 0
    while linkedListOne or linkedListTwo or carry:
        digitOne = linkedListOne.value if linkedListOne else 0
        digitTwo = linkedListTwo.value if linkedListTwo else 0
        finalDigit = digitOne + digitTwo + carry
        carry = finalDigit // 10
        finalDigit = finalDigit % 10
        temp.next = LinkedList(finalDigit)
        temp = temp.next
        linkedListOne = linkedListOne.next if linkedListOne else None
        linkedListTwo = linkedListTwo.next if linkedListTwo else None
    return sol.next
        
