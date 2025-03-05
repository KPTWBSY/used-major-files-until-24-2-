class Account:
    def __init__(self,name,num,bal):
        self.__name=name
        self.__num=num
        self.__bal=bal
        self.__history=[]
        self.__history.append(('신규',self.__bal,self.__bal))

    def check_acc(self):
        return('계좌번호 : '+self.__num+' , 소유자 : '+self.__name+' , 잔액 : '+str(self.__bal)+'\n')

    
    def deposit(self,amount):
        self.__bal+=amount
        self.__history.append(('입금',amount,self.__bal))
        print(amount,'원이 입금되었습니다.\n')
      

    def withdraw(self,amount):
        if amount>self.__bal:
            print('잔액이 부족합니다.\n')
        else:
            self.__bal-=amount
            self.__history.append(('출금',amount,self.__bal))
            print(amount,'원이 출금되었습니다.\n')
            
    def show_his(self):
        for (a,b,c) in self.__history:
            print(a,'\t',b,'원\t잔액\t',c)
        
accounts={}       
while True:
    print('='*36,'\n''\t','SOOKMYUNG BANK ATM')
    print('='*36,'\n1.신규 계좌 생성\n2.잔액 조회\n3.입금\n4.출금\n5.거래 내역 조회\n6.종료')
    print('-'*36)
    pick=int(input('선택 : '))

    if pick==1:
        A=input('계좌 소유자 이름을 입력하세요: ')
        while True:
            B=input('생성할 계좌 번호를 입력하세요: ')
            if B in accounts:
                print('사용할 수 없는 계좌 번호입니다. 다시 입력하세요.')
            else:
                break
        C=int(input('입금할 금액을 입력하세요: '))
        print('\n[ 생성된 계좌 정보 ]\n'+'계좌번호 : ',B,', 소유자 : ',A,' , 잔액 : ',C,'\n')
        account=Account(A,B,C)
        accounts[B]=account
        
    elif pick==2:
        B=input('계좌 번호를 입력하세요 : ')
        if B in accounts:
            print(accounts[B].check_acc())
        else:
            print('해당 계좌가 없습니다\n')
            
    elif pick==3:
        B=input('계좌 번호를 입력하세요 : ')
        if B in accounts:
            amount=int(input('입금하실 금액을 입력하세요 : '))
            accounts[B].deposit(amount)
        else:
            print('해당 계좌가 없습니다\n')
                  
    elif pick==4:
        B=input('계좌 번호를 입력하세요 : ')
        if B in accounts:
            amount=int(input('출금하실 금액을 입력하세요 : '))
            accounts[B].withdraw(amount)

    elif pick==5:
        B=input('계좌 번호를 입력하세요 : ')
        if B in accounts:
            accounts[B].show_his()
            
    elif pick==6:
        break

