print('점수 입력')
scores=[]
while True:
    x=int(input())
    if 1<=x<=100:
        scores.append(x)
    elif x==0:
        break
    else:
        print('다시 입력 바랍니다')
        
sum=0
for y in scores:
    sum+=y
average=sum/len(scores)

h=-1
for z in range(len(scores)):
    if scores[z]>h:
        h=scores[z]

l=101
for w in range(len(scores)):
    if scores[w]<l:
        l=scores[w]

print('최고 점수: %d \n최저 점수: %d \n합계: %d \n평균: %.2f'%(h,l,sum,average))
