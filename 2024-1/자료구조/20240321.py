score1=[(8,0),(4,3),(8,2),(4,6),(2,6),
        (10,0),(9,0),(10,0),(8,2),(10,0),(10,10)]
score2=[(10,0),(10,0),(10,0),(10,0),(10,0),
        (10,0),(10,0),(10,0),(10,0),(10,0),(10,0)]

score_list=[score1,score2]

#얼추 완성.
Score1=[]
total=i=0
while True:
    a=input("%d번째 프레임"%(i+1))
    a=tuple(int(x) for x in a.split(","))
    Score1.append(a)
    print(Score1)
    point1,point2=a[0],a[1]
    
    total+=point1+point2
    if i>=1:
        prev_point1,prev_point2=Score1[i-1]

    
        if prev_point1+prev_point2==10:
                if prev_point1*prev_point2==0:
                    if i>=2:
                        prev_prev_point1,prev_prev_point2=Score1[i-2]
                        if prev_prev_point1+prev_prev_point2==10 and (prev_prev_point1 or prev_prev_point2==0):
                            total+=point1*2+point2
                        else:
                            total+=point1+point2
                    else:
                        total+=point1+point2
                else:
                    total+=point1
                
    if point1+point2!=10 and i!=10:
        print(total)
        
    i+=1
    if i==10 and ((point1+point2)!=10):
        break
    elif i==11:
        print(total)
        break
    

'''Score1=[]
total=i=0
while True:
    a=input("%d번째 프레임"%(i+1))
    a=tuple(int(x) for x in a.split(","))
    Score1.append(a)
    print(Score1)
    point1,point2=a[0],a[1]
    
    total+=point1+point2

    if i>=1:
        prev_point1,prev_point2=Score1[i-1]

    
        if prev_point1+prev_point2==10:
            if i>=2:
                prev_prev_point1,prev_prev_point2=Score1[i-2]
                if prev_point1 or prev_point2==0:
                    if prev_prev_point1+prev_prev_point2==10 and (prev_prev_point1 or prev_prev_point2==0):
                        total+=point1*2+point2
                    else:
                        total+=point1+point2
                else:
                    total+=point1
                    print(total)
    if point1+point2!=10:
        print(total)
        
    i+=1
    if i==9 and prev_point1+prev_point2!=10:
        print(total)
        break
    elif i==10:
        print(total)
        break'''

#최종에 제일 가까운...
'''Score1=[]
total=i=0
while True:
    a=input("%d번째 프레임"%(i+1))
    a=tuple(int(x) for x in a.split(","))
    Score1.append(a)
    print(Score1)
    point1,point2=a[0],a[1]
    
    total+=point1+point2
    if i>=1:
        prev_point1,prev_point2=Score1[i-1]

    
        if prev_point1+prev_point2==10:
                if prev_point1*prev_point2==0:
                    if i>=2:
                        prev_prev_point1,prev_prev_point2=Score1[i-2]
                        if prev_prev_point1+prev_prev_point2==10 and (prev_prev_point1 or prev+prev_point2==0):
                            total+=point1*2+point2
                        else:
                            total+=point1+point2
                    else:
                        total+=point1+point2
                else:
                    total+=point1
                
    if point1+point2!=10:
        print(total)
        
    i+=1
    if i==9 and prev_point1+prev_point2!=10:
        print(total)
        break
    elif i==10:
        print(total)
        break'''
    

'''Score1=[]
total=i=0
while True:
    a=input("%d번째 프레임"%(i+1))
    a=tuple(int(x) for x in a.split(","))
    Score1.append(a)
    print(Score1)
    point1,point2=a[0],a[1]
    
    total+=point1+point2

    if i>=1:
        prev_point1,prev_point2=Score1[i-1]

    
        if prev_point1+prev_point2==10:
            if i>=2:
                prev_prev_point1,prev_prev_point2=Score1[i-2]
                if prev_point1 or prev_point2==0:
                    if prev_prev_point1+prev_prev_point2==10 and (prev_prev_point1 or prev_prev_point2==0):
                        total+=point1*2+point2
                    else:
                        total+=point1+point2
                else:
                    total+=point1
                    print(total)
    if point1+point2!=10:
        print(total)
    i+=1
    if i==10:
        print(total)
        break'''

'''Score1=[]
total=i=0
while True:
    a=input("%d번째 프레임"%(i+1))
    a=tuple(int(x) for x in a.split(","))
    Score1.append(a)
    print(Score1)
    point1,point2=a[0],a[1]
    
    total+=point1+point2
    prev_point1,prev_point2=Score1[i-1]

    if prev_point1+prev_point2==10:
        prev_prev_point1,prev_prev_point2=Score1[i-2]
        if prev_point1 or prev_point2==0:
            if prev_prev_point1+prev_prev_point2==10 and (prev_prev_point1 or prev_prev_point2==0):
                total+=point1*2+point2
            else:
                total+=point1+point2
        else:
            total+=point1
            print(total)
    if point1+point2!=10:
        print(total)
    i+=1
    if i==10:
        print(total)
        break
'''
    

'''for score in score_list:
    total=i=0
    frame=[]
    for first,second in score:
        f_total=first + second
        next_first,next_second=score[i+1]
        if first==10:
            result='STRIKE'
            f_total+=next_first+next_second
            if i!=9 and next_first==10:
                next_next_first,next_next_second=score[i+2]
                f_total+=next_next_first
        elif (first+second)==10:
            result='SPARE'
            f_total+=next_first
        else: result='NONE'
        total+=f_total
        frame.append((f_total,result))
        i+=1
        if i==10: break
    print(frame)
    print("Total=",total)
    print()'''
