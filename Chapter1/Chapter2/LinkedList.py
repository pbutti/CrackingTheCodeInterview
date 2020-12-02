class Node:
    next = None
    data : int = 0

    def __init__(self, d):
        self.data = d

    def appendToTail(self,d):
        end = Node(d)
        n = self
        while(n.next != None):
            n = n.next
        n.next = end

    def printList(self):
        print("Printing single linking list")
        n = self
        while(n.next != None):
            print(n.data,"->")
            n=n.next
        print(n.data,"##")


class SingleLinkedList:
    head = None

    def __init__(self, n):
        self.head = n

    #def __init__(self,d):
    #    self.head = Node(d)

    def printList(self):
        if self.head != None:
            self.head.printList()
        else:
            print("List is empty ##")

    def appendToTail(self,d):
        self.head.appendToTail(d)

    def attach(self,node):

        n = self.head
        end = None
        while (n.next != None):
            n=n.next
        end = n
        end.next = node

    def deleteNode(self, d):
        if self.head == None:
            return None
        if self.head.data == d:
            self.head = self.head.next
            return self.head

        n = self.head

        while (n.next != None):
            if (n.next.data == d):
                n.next = n.next.next
                return self.head
            n = n.next
        return self.head


def main():
    node = Node(10)
    node.appendToTail(20)
    node.appendToTail(30)
    node.appendToTail(50)
    node.appendToTail(100)
    node.appendToTail(32538)
    node.printList()

    node_2 = Node(0)
    list_2 = SingleLinkedList(node_2)
    list_2.appendToTail(10)
    list_2.appendToTail(100)
    list_2.appendToTail(1000)
    list_2.printList()

    print("Removing 0")
    list_2.deleteNode(0)
    print("Removing 1000")
    list_2.deleteNode(1000)

    list_2.printList()

    print("Removing 10")
    list_2.deleteNode(10)

    print("Removing 100")
    list_2.deleteNode(100)

    list_2.printList()



if __name__=="__main__":
    main()


