def stringCompression(s):
    if len(s) < 1:
        return ""
    if len(s) == 1:
        return s
    l: list(char) = [s[0]]

    # Add the first char
    count = 1
    for ic in range(1, len(s)):
        if s[ic] == l[-1]:
            count += 1
        else:
            l[-1] += str(count)
            l.append(s[ic])
            count = 1
        if len(l) >= len(s):
            return s
    l[-1] += str(count)
    return "".join(l)


def check(s):
    print(s, "->", stringCompression(s))


def main():
    check('aabcccccaaa')
    check('ABc')
    check('AaAaAa')
    check('AAABBBBbBBBB')
    check('b')


if __name__ == "__main__":
    main()
