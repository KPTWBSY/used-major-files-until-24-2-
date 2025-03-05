for a in range(1,10,3):
    for x in range(a,a+3):
        print(x,'단',end='\t\t')
    print()
    for b in range(1,10):
        for c in range(a,a+3):
            print(c,'*',b,'=',c*b,end='\t')
        print()
    print()
