def print_menu():
    print('-'*8,'진수변환 프로그램','-'*8)
    print('1.10진수 입력\n2.2진수 변환\n3.8진수 변환\n4.16진수 변환\n5.프로그램 종료')


def get_Decimal():
    global a
    a=int(input('십진수 입력'))
def Dec_to_Binary():
    global a
    an=''
    while a>=2:
    
        m=a%2
        n=a//2
        an+=str(m)
        a=n
    an+=str(a)
    print(an[::-1])    
        
def Dec_to_Octal():
    global a
    an=''
    while a>=8:
    
        m=a%8
        n=a//8
        an+=str(m)
        a=n
    an+=str(a)
    print(an[::-1]) 
def Dec_to_Hexad():
    global a
    an=''
    while a>=16:
    
        m=a%16
        n=a//16
        an+=str(m)
        a=n
    an+=str(a)
    print(an[::-1]) 




while True:
    print_menu()
    i=int(input('menu : '))
    if i==1:
        get_Decimal()
    elif i==2:
        Dec_to_Binary()
    elif i==3:
        Dec_to_Octal()
    elif i==4:
        Dec_to_Hexad()
    elif i==5:
        break
