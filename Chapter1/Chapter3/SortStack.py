from Stack import Stack


# this function flushes s1 on top of s2
def flush(s1,s2):

    while not s1.empty():
        s2.push(s1.pop())

def sort_stack(s):

    # r is the temporary stack
    r = Stack()

    while not s.empty():

        # Get the top element
        tmp = s.pop()

        if r.empty():
            r.push(tmp)
        else:
            if tmp >= r.peek():
                r.push(tmp)
            else:
                flush(r,s)
                r.push(tmp)

    flush(r,s)

    return s

def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(5)
    s.push(6)
    s.push(1)
    s.push(0)
    s.push(19)
    s.push(1)
    s.push(0)
    s.push(-1)
    s.push(100)

    print(s)

    print("Sorting with smallest on top")
    sort_stack(s)
    print(s)


if __name__=="__main__":
    main()


