class StackNode:
    next = None
    data = None

    def __init__(self, data):
        self.data = data

# This class implements a stack using a single linked list.
# Follows the LIFO protocol (last in, first out)

class Stack:

    # Initialize the stack with a dummy head node
    def __init__(self):
        self.__top  = None
        self.__size = 0

    # Remove the top of the item from the stack
    def pop(self):
        if self.empty():
            raise Exception("Pop-ed an empty stack!")
        node = self.__top
        self.__top = self.__top.next
        self.__size -= 1
        return node.data

    # Add an item on top of the stack
    def push(self, T):
        node = StackNode(T)
        node.next = self.__top
        self.__top = node
        self.__size += 1

    # Return the top of the stack
    def peek(self):
        if self.empty():
            raise Exception("Peeked an empty stack!")
        return self.__top.data

    # Return true if and only if the stack is empty
    def empty(self):
        return self.__size == 0

    # Return the size of the stack
    def size(self):
        return self.__size

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
        return out



def main():

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(185)
    print(s," size=",s.size(),"empty=",s.empty())
    s.pop()
    print(s," size=",s.size(),"empty=",s.empty())
    s.pop()
    print(s," size=",s.size(),"empty=",s.empty())
    s.pop()
    print(s," size=", s.size(),"empty=",s.empty())
    s.pop()






if __name__ == "__main__":
    main()
