from LinkedList import Node
from LinkedList import SingleLinkedList


def partition(sll,x):
    sll_gx = None
    n = sll.head
    # Check for single node list
    if (n.next == None):
        return sll

    if n.data >= x:
        sll.deleteNode(n.data)
        sll_gx.appendToTail(n.data)

    while (n.next != None):
        if (n.next.data >= x):
            new_node = Node(n.next.data)

            #This already skips the n.next if ends up deleted
            sll.deleteNode(n.next.data)
            if sll_gx == None:
                sll_gx = SingleLinkedList(new_node)
            else:
                sll_gx.appendToTail(new_node.data)
        else:
            n = n.next


    sll.printList()
    sll_gx.printList()

    sll.attach(sll_gx.head)

    sll.printList()

    return sll

def main():
    n = Node(3)
    sll = SingleLinkedList(n)
    buffer = [5,8,5,10,2,1]

    for b in buffer:
        sll.appendToTail(b)

    sll.printList()
    print("Partioning...")
    partition(sll,5)



if __name__=="__main__":
    main()