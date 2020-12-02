from LinkedList import SingleLinkedList
from LinkedList import Node


def removeDups_noBuf(sll):

    #Ill formed single linked list
    if sll == None:
        return None

    #Linked list without head
    if sll.head == None:
        return sll

    p1 = sll.head

    while p1.next != None:
        p2 = p1.next
        while p2.next != None:
            print("Checking::",p2.data,p1.data)
            if p2.data == p1.data:
                sll.deleteNode(p2.data)
            #update p2
            p2 = p2.next
        print("Updating p1..")
        #update p1
        p1 = p1.next

    return sll

def removeDups(sll):

    buffer = []
    if sll == None:
        return sll

    if sll.head == None:
        return sll

    buffer.append(sll.head.data)

    p1 = sll.head.next

    while p1 != None:
        if (p1.data in buffer):
            sll.deleteNode(p1.data)
        else:
            buffer.append(p1.data)
        p1 = p1.next

    return sll


def main():

    n = Node(0)
    sll = SingleLinkedList(n)
    sll.appendToTail(1)
    sll.appendToTail(2)
    sll.appendToTail(3)
    for i in range(4):
        sll.appendToTail(0)

    for i in range(3):
        sll.appendToTail(3)
    for i in range(6):
        sll.appendToTail(0)
    for i in range(2):
        sll.appendToTail(6)

    sll.printList()
    removeDups(sll)

    print("After duplicate removal")
    sll.printList()

    for i in range(4):
        sll.appendToTail(0)

    for i in range(3):
        sll.appendToTail(3)
    for i in range(6):
        sll.appendToTail(0)
    for i in range(2):
        sll.appendToTail(6)

    print("After duplicate removal no buff")
    removeDups_noBuf(sll)
    sll.printList()

if __name__=="__main__":
    main()


