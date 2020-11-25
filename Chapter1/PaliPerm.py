def paliperm(s):
    d={}
    length = 0
    for c in s:
        if not c.isalpha():
            continue
        else:
            if c.isupper():
                c = c.lower()
            if c not in d:
                d[c]=1
            else:
                d[c]+=1
            length+=1

    even = True
    if (length) % 2 != 0:
        even = False
    odd_count = 0
    for k in d:
        if d[k] % 2 != 0:
            odd_count+=1
    if even:
        if odd_count > 0:
            return False
        else:
            return True
    else:
        if odd_count != 1:
            return False
        else:
            return True


def bit_paliperm(s):
    n = convertStringToInt(s)
    return checkOneOddBit(n)

# This method checks if an integer has only one bit equal to one and the rest equal to 0
def checkOneOddBit(n):
    # trick: doing n & n - 1 should give 0 if there is only one bit up
    return n & (n - 1) == 0



def convertStringToInt(s):

    stringInt = 0x0

    for c in s:
        # I need an integer of at least 25 bits to map all possible characters
        if not c.isalpha():
            continue
        # This computes the shift an uppercase letter to a lowercase letter.
        # Since ord('A') < ord('a'), use the following
        shift = ord('a') - ord("A")
        # This tells you the bit location of each character
        bit_location =  ( ord(c) - ord('a') ) % shift
        # xor-ing will cancel bits that have already been turned on
        stringInt ^= 1 << bit_location
    return stringInt

def main():
    pp = paliperm("Tact coa")
    print(pp)
    pp = paliperm("tt accoa")
    print(pp)
    pp = paliperm("123 abs")
    print(pp)
    pp = paliperm("123 ~~ ddkkl123")
    print(pp)

    print("Using the bit mapping")
    print(bit_paliperm("Tact coa"))
    print(bit_paliperm("tt accoa"))
    print(bit_paliperm("123 abs"))
    print(bit_paliperm("123 ~~ ddkkl123"))

if __name__=="__main__":
    main()