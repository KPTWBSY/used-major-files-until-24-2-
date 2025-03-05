import random
answer=random.randint(1,100)
num=0
times=6
while num!=answer and times>0:
    num=int(input(('정답 입력')))
    if num>answer:
        print('정답보다 큼')
    elif num<answer:
        print('정답보다 작음')
    times=times-1
    print(times,'번 기회가 남았습니다')
if num==answer:
    print('정답입니다.')
else:
    print('기회 초과. 정답은',answer)
