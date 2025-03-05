class Maze:
    def __init__(self):
        self.maze=[[1,1,1,1,1],\
                   [1,0,0,1,1],\
                   [1,0,1,0,1],\
                   [1,0,0,'X',1],\
                   [1,1,1,1,1]]
        self.mark=[[0]*5 for i in range(5)]
        self.path=[]
        self.found=False

    def empty(self):
        return len(self.path)==0
    def add(self,row,col):
        self.path.append((row,col))
    def delete(self):
        return self.path.pop()
    def view(self):
        print("path",self.path)

    def rexplore(self,row,col):
        for x,y in [(0,-1),(1,0),(0,1),(-1,0)]:
            next_col=col+x
            next_row=row+y
            if self.maze[next_row][next_col]=='X':
                self.add(row,col)
                self.add(next_row,next_col)
                self.found=True
                return True
            elif self.maze[next_row][next_col]==0 and self.mark[next_row][next_col]==0:
                self.mark[next_row][next_col]=1
                if (row,col) not in self.path:
                    self.add(row,col)
                result=self.rexplore(next_row,next_col)
                if result: return True
                else:self.delete()
        return False
'''m=Maze()
m.found=m.rexplore(1,1)
if not m.found: print("탈출 경로 없음")
else: print("탈출 성공")
m.view()'''

'''def htower(n,a,b):
    global count
    count+=1
    if n==1:
        print("Disc %d, moved from Pole(%d) to (%d)"%(n,a,b))
    else:
        c=6-a-b
        htower(n-1,a,c)
        print("Disc %d, moved from Pole (%d) to (%d)" % (n,a,b))
        htower(n-1,c,b)
count=0
n=int(input("Enter disc number:"))
htower(n,1,2)
print("# move for %d discs : %d" %(n,count))'''

'''import time
def fibo1(n):
    global count1
    count1+=1
    if n<=1:return n
    else:return fibo1(n-2)+fibo1(n-1)
    
def fibo2(n):
    global count2
    count2+=1
    if n<=1: return (0,n)
    else:
        (a,b)=fibo2(n-1)
        return (b,a+b)
    
for num_max in [10,20]:
    count1=0
    count2=0
    f=[]
    print("fibo1",num_max)
    time1=time.time()
    for d in range(num_max):
        f.append(fibo1(d))
    time2=time.time()
    print("time1=",time2-time1)
    print("recursion1=",count1,'for F%d'%num_max)
    print()

    time1=time.time()
    print("fibo2",num_max,"=",fibo2(num_max))
    for d in range(num_max):
        f.append(fibo2(d)[1])
    time2=time.time()
    print("time2=",time2-time1)
    print("recursion2=",count2)
    print(f)
    print()'''

#이진탐색(반복문)

import time
'''time1=time.time()

def binary_search(lst,item,left,right):
    while left<right:
        mid=(left+right)//2
        if item==lst[mid]:
            return mid
        else:
            if item<lst[mid]:
                right=mid-1
            else:
                left=mid+1
    return -1
mylist=[5,8,9,11,13,17,23,32,45,52,60,72]
print(mylist)
for item in [60,9,10]:
    pos=binary_search(mylist,item,0,len(mylist)-1)
    print("position of %2d=%2d"%(item,pos))
time2=time.time()
print("time1=",time2-time1)

#이진탐색(재귀문)
time1=time.time()
def rbinsearch(lst,item,left,right):
    if left<=right:
        mid=(left+right)//2
        if item ==lst[mid]:
            return mid
        elif item<lst[mid]:
            return rbinsearch(mylist,item,left,mid-1)
        else:
            return rbinsearch(mylist,item,mid+1,right)
    return -1
mylist=[5,8,9,11,13,17,23,32,45,52,60,72]
print(mylist)
for item in [60,9,10]:
    pos=rbinsearch(mylist,item,0,len(mylist)-1)
    print("position of",item,"=",pos)
time2=time.time()
print("time1=",time2-time1)'''

'''#최대공약수 구하기
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)'''

#4-3번(최소/반복문)

'''def lowest(lst):
    if len(lst)==0:
        return 0
    else:
        min=lst[0]
        for i in range (len(lst)):
            if lst[i]<=min:
                min=lst[i]
            i=i+1
        return min
print(lowest([3,5,0,0,6]))'''

#4-3번(최소/재귀문)
#..을 만들려고 했는데?? 어쩌다보니...반복문을 더 간결하게 정리해버린듯
'''def rlowest(lst):
    while len(lst)>1:
        if lst[0]<=lst[1]:
            lst.remove(lst[1])
        else:
            lst.remove(lst[0])
    return lst

print(rlowest([3,5,0,0,6]))             
        
#재귀호출 76페이지 2번
def Rlowest(lst):
    if len(lst)==1:
        return lst[0]
    else:
        if lst[0]<=lst[1]:
            lst.remove(lst[1])
            return Rlowest(lst)
        else:
            lst.remove(lst[0])
            return Rlowest(lst)
    return lst
print(Rlowest([3,5,1,2,6]))

def Rhighest(lst):
    if len(lst)==1:
        return lst[0]
    else:
        if lst[0]>=lst[1]:
            lst.remove(lst[1])
            return Rhighest(lst)
        else:
            lst.remove(lst[0])
            return Rhighest(lst)
        return lst
print(Rhighest([3,5,1,2,6]))'''

'''def find(lst):
    if len(lst)==1:
        return (lst[0],lst[0])
    elif len(lst)==2:
        if lst[0]<lst[1]:
            return (lst[0],lst[1])
        elif lst[0]>lst[1]:
            return(lst[1],lst[0])
        else:
            return(lst[0],lst[0])
    else:
        mid=len(lst)//2
        min_left,max_left=find(lst[:mid])
        min_right,max_right=find(lst[mid:])
        return min(min_left,min_right),max(max_left,max_right)
my_lst=[3,7,2,9,1,5]
min_val,max_val=find(my_lst)
print(min_val)
print(max_val)'''

#48쪽 1번

'''lst=[21,7,40,29,11,5,90,78,64,15,88]
lowest=lst[0]
highest=lst[0]
for i in range (len(lst)):
    if lst[i]<lowest:
        lowest=lst[i]
        
for i in range (len(lst)):
    if lst[i]>highest:
        highest=lst[i]
a=[]
a.append(lowest)
a.append(highest)
print(tuple(a))


#과제 재귀 반복 최소최대 최종?
def find(lst):
    if len(lst)==1:
        return (lst[0],lst[0])
    elif len(lst)==2:
        if lst[0]<lst[1]:
            return (lst[0],lst[1])
        elif lst[0]>lst[1]:
            return(lst[1],lst[0])
        else:
            return(lst[0],lst[0])
    else:
        mid=len(lst)//2
        min_left,max_left=find(lst[:mid])
        min_right,max_right=find(lst[mid:])
        if min_left<=min_right:
            min_val= min_left
        else:
            min_val=min_right
        if max_left>=max_right:
            max_val= max_left
        else:
            max_val= max_right
        return (min_val,max_val)
my_lst=[3,7,2,9,1,5]
print(find(my_lst))'''



#range 함수를 사용하여 1보다 크고 n보다 작은 m의 배수들을 반환하는 함수를 작성하시오.
#48쪽 2번

'''def X(n,m):
    for a in range (n):
        if a!=0 and a*m<=n:
            print(a*m)
X(10,3)'''

#48쪽 3번(과제): 분수 연산&출력
class Fraction:
    def __init__(self,up,down):
        self.num=up
        self.den=down
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def gcd(self,a,b):
        while a%b!=0:
            a,b=b,a%b
        return b
    
    def __add__(self,other):
        new_num=self.num*other.den+self.den*other.num
        new_den=self.den*other.den
        common=self.gcd(new_num,new_den)
        return Fraction(new_num//common, new_den//common)
    
    def multiply(self,other):
        new_num=self.num*other.num
        new_den=self.den*other.den
        common=self.gcd(new_num,new_den)
        return Fraction(new_num//common,new_den//common)

#약분(abbreviation) 추가하기..
    def abbrevitation(self):
        common=self.gcd(self.num,self.den)
        if self.num>self.den and common==self.den:
            return self.num/common
        else:
            return Fraction(self.num//common,self.den//common)

#실수>소수 변환(decimal_fraction)추가하기

    def decimal_fraction(self,real):
        x,y=1,1
        while x/y!=real:
            if (x/y)<real:
                x+=1
            else:
                y+=1
        self.num=x
        self.den=y
        return self


num1=Fraction(35,14)
print(num1.abbrevitation())

num2=Fraction(1,1)
while True:
    decimal_number=float(input("실수를 입력하세요 "))
    if decimal_number==0:
        break
    else:
        print(num2.decimal_fraction(decimal_number))
        print(num2.abbrevitation())


        
