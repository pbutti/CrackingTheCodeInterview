def oneAway(s1,s2):
    if abs(len(s1)-len(s2)) >= 2:
        return False
    if (len(s1) <= len(s2)):
        sm=s1
        sM=s2
    else:
        sm=s2
        sM=s1

    edits = 0
    diffL=len(sM) - len(sm)

    for ic in range(len(sm)):
        # This only works if the edits can only be at most one, such that the max difference is 1.
        # For the general case two indices are needed
        if sm[ic] != sM[ic + edits*diffL]:
            edits+=1
        # This takes into account that if the two lengths are different, then there is at least an insertion/removal
        # operation to do
        if edits + diffL > 1:
            return False
    return True

def checkStrings(s1,s2):
    print(s1,s2,'->',oneAway(s1,s2))

def main():
    checkStrings('pale','ple')
    checkStrings('pales','pale')
    checkStrings('pale','bale')
    checkStrings('pale','bake')
    checkStrings('abcd','abcde')




if __name__=="__main__":
    main()