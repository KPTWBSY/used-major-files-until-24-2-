def main():
    print('========영한사전========')
    print('1. 단어 추가\n2. 단어 조회/수정\n3. 단어 삭제\n4. 전체 단어 출력\n5. 종료')
    print('='*24)
    
def add(words):
        w=input('단어를 입력하세요. 종료=[Enter] : ')
        if w=='':
            return
        elif w in words:
            print('이미 존재하는 단어입니다')
        else:
            m=input('뜻을 입력하세요 : ')
            words[w]=m
            
def check(words):
    w=input('조회할 단어를 입력하세요. 종료=[Enter] : ')
    if w in words:
        print('단어 : %s\n뜻 : %s'%(w,words[w]))
        while True:
            change=input('수정하시겠습니까(y/n) : ')
            if change=='y':
                words[w]=input('뜻 : ')
                print('수정되었습니다')
                break
            elif change=='n':
                break
            else:
                print('잘못된 입력입니다')
    elif w=='':
        return
    else:
        print('잘못된 입력입니다.')

def delete(words):
    dw=input('삭제할 단어를 입력하세요. 종료=[Enter] : ')
    if dw in words:
        del words[dw]
        print(dw,'가 삭제되었습니다.')
    elif dw=='':
        return
    else:
        print(dw,'은(는) 사전에 존재하지 않습니다.')

def show(words):
    for w in words:
        print('%-15s'%w, words[w])
    
words={}
while True:
    main()
    menu=int(input('선택 : '))
    print()
    if menu==1:
        add(words)
    elif menu==2:
        check(words)
    elif menu==3:
        delete(words)
    elif menu==4:
        show(words)
    elif menu==5:
        break
    else:
        print('메뉴를 다시 선택해주세요.')
