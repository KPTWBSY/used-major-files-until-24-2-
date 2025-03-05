def menu():
    print('1 \n2 \n3')

def add():
    global list
    list=[]
    while True:
        item=input('항목을 추가하세요')
        if item== '':
            break
        else:
            list.append(item)
    print(list)
    
def delete():
    del list[0]
    print(list)
    


while True:
    menu()
    choice=int(input('선택지 입력'))
     
    if choice==1:
        add()
    elif choice==2:
        delete()
    
