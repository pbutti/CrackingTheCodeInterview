from Stack import StackNode

# This class implements a stack which supports a min() method that
# gives back the minimum element in the stack with O(1) processing time

# Still supports push and pop() in O(1) time

class MinStackNode:

    def __init__(self,T):
        self.data = T
        self.next = None
        self.min  = None

    def __str__(self):
        out = "Node data:" + str(self.data)+"\n"
        if (self.next):
            out += "->" + str(self.next.data) +"\n"
        else:
            out += "-> X" + "\n"
        if (self.min):
            out += "=>" + str(self.min.data) +"\n"
        else:
            out+= "=> X" +"\n"

        return out


class MinStack_v2:

    def __init__(self):
        self.__top = None
        self.__size = 0


    def __str__(self):
        out = "Stack:  "
        n = self.__top
        if n:
            out += " " + str(self.__top.data) + "->"
        else:
            return out
        while n.next:
            out += str(n.next.data)
            n = n.next
            if n.next:
                out += "->"
        return out

    def push(self,T):

        node = MinStackNode(T)
        node.next = self.__top

        # If empty the node needs to point to itself
        if self.isempty():
            node.min = node
        else:
            # If a new minimum then the new node needs to know it is the min
            if T <= self.__top.min.data:
                node.min = node
            else:
                # If not a new minimum then the node needs to point to the min node
                node.min = self.__top.min
        #update the top
        self.__top = node

        self.__size+=1

    def pop(self):
        if self.isempty():
            raise Exception("pop(): Empty stack")

        node = self.__top
        self.__top = self.__top.next
        self.__size-=1

        return node.data

    def min(self):
        if self.isempty():
            raise Exception("min(): Empty stack")

        # If there is only one element that is the minimum
        return self.__top.min.data

    def isempty(self):
        return self.__size == 0




class MinStack:

    def __init__(self):
        self.__top    = None
        self.__topmin = None
        self.__size = 0

    def push(self,T):
        node = StackNode(T)
        node.next = self.__top
        self.__top = node

        if self.__topmin is None or T <= self.__topmin.data:
            nodemin = StackNode(T)
            nodemin.next = self.__topmin
            self.__topmin = nodemin
        self.__size+=1

    def pop(self):
        if self.isempty():
            raise Exception("pop(): Empty stack")

        node = self.__top
        self.__top = self.__top.next
        if (node.data <= self.__topmin.data):
            nodemin = self.__topmin
            self.__topmin = self.__topmin.next
        self.__size-=1
        return node.data

    def min(self):
        if self.isempty():
            raise Exception("min(): Empty stack")
        return self.__topmin.data

    def isempty(self):
        return self.__size == 0

    # String representation of the stack
    def __str__(self):
        out = "Stack:  "
        n = self.__top
        if n:
            out += " " + str(self.__top.data) + "->"
        else:
            return out
        while n.next:
            out += str(n.next.data)
            n = n.next
            if n.next:
                out += "->"

        out2 = "StackMin:  "
        n = self.__topmin
        if n:
            out2 += " " + str(self.__topmin.data) + "->"
        else:
            return out+"\n"+out2
        while n.next:
            out2 += str(n.next.data)
            n = n.next
            if n.next:
                out2 += "->"

        return out+"\n"+out2

def main():

    print("Checking min stack implementation")
    ms = MinStack()
    ms.push(3)
    print(ms)
    print("Min:",ms.min())
    ms.push(5)
    ms.push(6)
    ms.push(190)
    ms.push(1)
    ms.push(0)
    print(ms)
    print("Min:", ms.min())
    ms.pop()
    print(ms)
    print("Min:", ms.min())
    ms.push(2)
    print(ms)
    print("Min:", ms.min())
    ms.pop()
    print(ms)
    print("Min:", ms.min())

    print ("#################")

    ms2 = MinStack_v2()
    ms2.push(1)
    ms2.push(2)
    ms2.push(3)
    ms2.push(0)
    ms2.push(0)
    ms2.push(2)
    ms2.push(3)
    print(ms2,"with min",ms2.min())

    for i in range(6):
        print("Removing ", ms2.pop())
        print("Min = ",ms2.min())


if __name__=="__main__":
    main()