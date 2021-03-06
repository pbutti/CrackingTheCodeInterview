from LinkedList import Node
from LinkedList import SingleLinkedList

# Attaches to a node another node. If carry > 0, then sums to the current node content.
def attachElement(node, value, carry):
    end = Node(value)
    if carry > 0:
        node.data += carry
    node.next = end

    return end

def GetSize(sll):
    if sll is None or sll.head is None:
        return 0
    count = 1
    n = sll.head
    while not n.next is None:
        count+=1
        n = n.next
    return count


def sumBackward(l1,l2):

    if (l1 is None or l1.head is None):
        return l2
    if (l2 is None or l2.head is None):
        return l1


    length1 = GetSize(l1)
    length2 = GetSize(l2)

    print("Sizes: ", length1,length2)

    diff = length1 - length2

    if (diff > 0):
        for i in range(diff):
            l2.appendToHead(0)
    elif (diff < 0):
        for i in range(abs(diff)):
            l1.appendToHead(0)

    #l1.printList()
    #l2.printList()

    p1 = l1.head
    p2 = l2.head

    #Create a sum linked list holding 0

    sum = SingleLinkedList(Node(0))

    #p3 points to the end of the list all the time.
    p3 = sum.head

    value = int(p1.data + p2.data) % 10
    carry = int(p1.data + p2.data) // 10

    # Add the element and update p3
    p3 = attachElement(p3,value,carry)


    # Run through p1
    while not p1.next is None:
        if (not p2.next is None):
            value = int((p1.next.data + p2.next.data)) % 10
            carry = int(p1.next.data + p2.next.data) // 10
            p3 = attachElement(p3,value,carry)
            p2 = p2.next
        else:
            p3 = attachElement(p3,p1.next.data,carry)
            #At this point carry will be always 0
            carry = 0

        p1 = p1.next

    # Now we just need to attach p2 in the case p1 was smaller

    while (not p2.next is None):
        p3 = attachElement(p3, p2.next.data,carry)
        carry = 0
        p2 = p2.next


    #Check if sum head is 0. If is 0, then remove the head. Will return an empty list, then

    if (sum.head.data == 0):
        sum.deleteNode(0)

    return sum



def sumForward(l1,l2):
    if (l1 is None or l1.head is None):
        return l2
    if (l2 is None or l2.head is None):
        return l1

    p1 = l1.head
    p2 = l2.head

    # Sum the heads

    value = int(p1.data + p2.data) % 10
    carry = int(p1.data + p2.data) // 10

    sum = SingleLinkedList(Node(value))

    # Loop over p1

    while not p1.next is None:
        if not p2.next is None:
            value = int(p1.next.data + p2.next.data + carry) % 10
            carry = int(p1.next.data + p2.next.data + carry) // 10
            sum.appendToTail(value)
            p2 = p2.next
        else:
            value = int(p1.next.data + carry) % 10
            carry = int(p1.next.data + carry) // 10
            sum.appendToTail(value)
        p1 = p1.next

    # p1 is done. Check if there is anything left in p2 to be added.

    while not p2.next is None:
        value = int(p2.next.data + carry) % 10
        carry = int(p2.next.data + carry) // 10
        sum.appendToTail(value)
        p2 = p2.next

    # Add the carry

    if carry > 0:
        sum.appendToTail(carry)

    return sum

def printForward(sll):
    power = 0
    value = 0
    if sll is None or sll.head is None:
        return 0
    n = sll.head
    value = n.data * (10**power)
    while not n.next is None:
        power+=1
        value += n.next.data * (10**power)
        n = n.next

    print("List integer (forward) = ",value)
    return value

def printBackward(sll):
    power = 0
    value = 0
    if sll is None or sll.head is None:
        return 0

    n = sll.head
    value += n.data

    while not n.next is None:
        value = value * 10 + n.next.data
        n = n.next


    print("List integer (backward) = ",value)
    return value


def main():

    ll1 = SingleLinkedList(Node(7))
    ll1.appendToTail(1)
    ll1.appendToTail(6)

    ll2 = SingleLinkedList(Node(5))
    ll2.appendToTail(9)
    ll2.appendToTail(2)

    ll1.printList()
    printForward(ll1)

    ll2.printList()
    printForward(ll2)

    sum = sumForward(ll1,ll2)

    ll1 = SingleLinkedList(Node(1))
    ll2 = SingleLinkedList(Node(9))
    ll2.appendToTail(9)

    sum = sumForward(ll1,ll2)
    printForward(sum)

    ll1 = SingleLinkedList(Node(6))
    ll1.appendToTail(1)
    ll1.appendToTail(7)

    ll2 = SingleLinkedList(Node(2))
    ll2.appendToTail(9)
    ll2.appendToTail(5)

    printBackward(ll1)
    printBackward(ll2)

    print("Summing backwards")
    sum = sumBackward(ll1,ll2)
    printBackward(sum)

    print("Special Case")
    ll1 = SingleLinkedList(Node(1))
    ll1.appendToTail(2)
    ll1.appendToTail(3)
    ll1.appendToTail(4)

    ll2 = SingleLinkedList(Node(5))
    ll2.appendToTail(6)
    ll2.appendToTail(7)

    sum = sumBackward(ll1,ll2)
    printBackward(sum)

if __name__=="__main__":
    main()