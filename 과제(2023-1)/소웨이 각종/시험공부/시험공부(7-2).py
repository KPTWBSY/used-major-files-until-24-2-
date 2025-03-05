list=[]
while True:
    choice=int(input('choose one'))
    if choice==1:
        while True:
            a=input()
            if a=='':
                break
            else:
                list.append(a)
        print(list)
    
    elif choice==2:
        list.pop(0)
        print(list)
    elif choice==3:
        print(list)
    else:
        break
