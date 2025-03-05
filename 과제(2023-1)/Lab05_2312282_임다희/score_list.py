number=[]
while True:
    a=input('숫자를 입력해주세요. 종료=[Enter] : ')
    if a=='':
        if len(number)==0:
            print("숫자가 존재하지 않습니다.")
        else:
            number.sort()
            print(number)
            
            n=len(number)
            x=number[n-1]
            y=number[0]
            if n%2==0:
                z=(number[n//2]+number[(n//2)-1])/2
                print("최대값 : %d \n최소값 : %d \n중간값 : %.1f"%(x,y,z))
            else:
                z=number[(n-1)//2]
                print("최대값 : %d \n최소값 : %d \n중간값 : %d"%(x,y,z))
        break
    else:
        number.append(int(a))
