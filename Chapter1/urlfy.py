def urlfy(s,n):
    print(s)
    s=list(s)
    offset = len(s) - n
    ic = len(s)-1
    while ic >= 0:
        if s[ic-offset] != " ":
            s[ic] = s[ic-offset]
            ic-=1
        else:
            s[ic] = "0"
            s[ic-1] = "2" 
            s[ic-2] = "%"
            offset  -=2
            ic-=3
    s = "".join(s)
    print(s)
    return s
    

def main():
    
    urlfy("Mr John Smith    ",13)
    urlfy("Mrs Rachel Agatha Maria Smith        ",29)



if __name__=="__main__":
    main()
