#볼링게임(2.12)
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
        break'''
#최대최소(3.2)
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

        a=b=0
        if min_left>=min_right:
            a=min_right
        else:
            a=min_left
        if max_left>=max_right:
            b=max_left
        else:
            b=max_right
        return a,b
             

my_lst=[1,1,1,1,2,2,2]
min_val,max_val=find(my_lst)
print(min_val)
print(max_val)'''

'''min_left, max_left=find(lst[3,7,2])
min_right,max_right=find(lst[9,1,5])
return 1
find(lst[3,7,2])에서 mid=1
min_left,max_left=find(lst[3])
min_right,max_right=find(lst[7,2])
return 2
find(lst[3])>>3,3리턴
find(lst[7,2]>>>2,7 리턴)
return 2의 값: '''

#실수>분수(2.3)

'''class Fraction:
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
            
            return Fraction(int(self.num//common),int(self.den//common))

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
    
#최종!!!
    def Decimal_fraction(self,real):
        x=1
        while True:
            if real*10%1==0:
               self.num=int(real*10)
               self.den=10**x 
               return self 
            else:
                real=real*10
                x+=1

num2=Fraction(1,1)

decimal_number=float(input("실수를 입력하세요 "))
print(num2.Decimal_fraction(decimal_number))
print(num2.abbrevitation())'''

#하...뭔 클래스를 수정하라해서 다시한다 미치겟네(최최최종,완성)

'''class Fraction:
    def __init__(self,up=1,down=1):
        self.num=up
        self.den=down
        
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def gcd(self,a,b):
        while a%b!=0:
            a,b=b,a%b
        return b
  
    def abbrevitation(self):
        common=self.gcd(self.num,self.den)
        if self.num>self.den and common==self.den:
            return self.num/common
        else:
            return Fraction(int(self.num//common),int(self.den//common))

    def Decimal_fraction(self,real):
        x=1
        while True:
            if real*10%1==0:
               self.num=int(real*10)
               self.den=10**x 
               return self 
            else:
                real=real*10
                x+=1
                
num2=Fraction()

decimal_number=float(input("실수를 입력하세요 "))
print(num2.Decimal_fraction(decimal_number))
print(num2.abbrevitation())'''


#회문확인(48p)
'''def rec_palindrome(s):
    return s==s[::-1]

s1="saass"
print(rec_palindrome(s1))'''

#수열생성(48p)
'''[1,4,7,10,13,16,19...(1부터 3씩 14번 더하는 수열)]'''
'''lst=[]
#while i<44:
for i in range (1,43,3):
    lst.append(i)
print(lst)
lst2=[]
a=1
for i in range (15):
    lst2.append(a)
    a=a+3
print(lst2)'''

#수열생성2(48p)
'''[1,2,4,7,11,16,22,29...(더하는 숫자도 1씩 늘려감)]'''  
'''lst=[]
a=1 
i=0
while a<120:
    lst.append(a)
    a+=i
    i+=1
print(lst)'''

#중첩반복문 이용해 리스트 출력
'''scores=[[75,90,85],[60,100,75],[90,70,80]]
for score in scores:
    for s in score:
        if score.index(s)!=2:
            print(s,end=',')
        else:
            print(s)'''

#다항식을 튜플(계수,지수)의 리스트로 표현>>두 다항식의 덧셈,곱셈 수행[아직 다 안함]

'''P=[(9,4),(5,3),(4,2)]
X=[(7,3),(2,2)]

def plus(A,B):
    lst=[]
    for a in A:
        for b in B:
            if a[1]==b[1]:
                lst.append((a[0]+b[0],a[1]))
            

    return lst

print(plus([(9,4),(5,3),(4,2)],[(7,3),(2,2)]))'''

#수식 변환 평가(4.13)

'''class Sym:
    OPEN_B=1
    CLOSE_B=2
    PLUS=3
    MINUS=4
    TIMES=5
    DIVIDE=6
    MOD=7
    OPERAND=8
class Expression:
    def __init__(self,expr):
        self.stack1=[]
        self.stack2=[]
        self.size=100
        self.expr=expr 
        self.top=-1
        self.output=""

    def isEmpty(self,which):
        return len(which)==0
    def isFull(self,which):
        return len(which)==self.size
    def show_stack(self,which):
        print(which)

    def push(self,item,which):
        if not self.isFull(which):
            self.top+=1
            which.append(item)
            self.show_stack(which)
        else:
            print("Stack full")
    def pop(self,which):
        if not self.isEmpty(which):
            self.top-=1
            return which.pop()
        else:
            print("Stack empty")
    
    def eval_postfix(self):
        for sym in self.expr.split():
            print(sym,end=' ')
            sym_type=self.getSymtype(sym)
            if sym_type== Sym.OPERAND:
                self.push(int(sym),self.stack1)
            else:
                print(self.stack1[-1],self.stack1[-2],sym)

                
                op2=self.pop(self.stack1)
                op1=self.pop(self.stack1)
                if sym_type==Sym.PLUS:
                    self.push(op1+op2,self.stack1)
                elif sym_type==Sym.MINUS:
                    self.push(op1-op2,self.stack1)
                elif sym_type==Sym.TIMES:
                    self.push(op1*op2,self.stack1)
                elif sym_type==Sym.DIVIDE:
                    self.push(op1//op2,self.stack1)
                elif sym_type==Sym.MOD:
                    self.push(op1%op2,self.stack1)
                
        return self.pop(self.stack1)
    
    def infix_postfix(self):
        for token in expr.split():
            print(token,end=' ')
            if token.isalnum():
                self.push(token,self.stack1)

            elif token=='(':
                self.push(token,self.stack2)
            elif token==')':
                sym=self.pop(self.stack2)
                while sym!='(':
                    self.output+=(sym+' ')
                    sym=self.pop(self.stack2)
            else:
                while not self.isEmpty(self.stack2) and self.precedence(self.stack2[-1])>=self.precedence(token):
                    sym=self.pop(self.stack2)
                    self.output=self.output+(sym+' ')
                self.push(token,self.stack2)
        while not self.isEmpty(self.stack2):
            self.output+=(self.pop(self.stack2)+' ')
        print()
    def precedence(self,op):
        if op=='(': return 0
        elif op in ['+','-']: return 1
        elif op in ['*','/','%']:return 2

    def getSymtype(self,sym):
        if sym=='(':sym_type=Sym.OPEN_B
        elif sym==')':sym_type=Sym.CLOSE_B
        elif sym=='+':sym_type=Sym.PLUS
        elif sym=='-':sym_type=Sym.MINUS
        elif sym=='*':sym_type=Sym.TIMES
        elif sym=='/':sym_type=Sym.DIVIDE
        elif sym=='%':sym_type=Sym.MOD
        else: sym_type=Sym.OPERAND
        return sym_type

expr=input("input an infix :")
e=Expression(expr)
print()
e.infix_postfix()
print("postfix : ",e.output)
e.expr=e.output
print()
print("evaluation : ",e.eval_postfix())


expr=input("input an infix=")


e=Expression(expr)
print("중위 수식 : ",expr)
print()
e.infix_postfix()
print("변환 후위 수식 ",e.output)
e.stack=[]
e.expr =e.output
print()
print("후위 수식 계산 값=",e.eval_postfix())
print()'''


#수식 gpt
'''def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator=='(' or ')':
        return 0  # 괄호의 우선순위

def infix_to_postfix(expression):
    operand_stack = []  # 피연산자를 저장하는 스택
    operator_stack = []  # 연산자를 저장하는 스택
    result = ""

    for char in expression.split():
        if char.isalnum():  # 알파벳이나 숫자인 경우 피연산자 스택에 추가
            operand_stack.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            operator_stack.append(char)
            print(operator_stack)
            while operator_stack[-1]!= '(':
                result += operator_stack.pop()
            operator_stack.pop()  # '(' 제거
        else:
            while (operator_stack and precedence(operator_stack[-1]) >= precedence(char)):
                result += operator_stack.pop()
            operator_stack.append(char)

    while operator_stack:
        result += operator_stack.pop()

    return result

# 테스트
infix_expression = input("중위 표기법으로 수식을 입력하세요: ")
postfix_expression = infix_to_postfix(infix_expression)
print("후위 표기법으로 변환된 수식:", postfix_expression)'''


#아....죽겠다
#수식 변환 평가(4.13) (최종!!!!!!!!!!!20240403)

'''class Sym:
    OPEN_B=1
    CLOSE_B=2
    PLUS=3
    MINUS=4
    TIMES=5
    DIVIDE=6
    MOD=7
    OPERAND=8
class Expression:
    def __init__(self,expr):
        self.stack1=[]
        self.stack2=[]
        self.size=100
        self.expr=expr 
        self.top=-1
        self.output=""

    def isEmpty(self,which):
        return len(which)==0
    def isFull(self,which):
        return len(which)==self.size
    def show_stack(self,which):
        print(which)

    def push(self,item,which):
        if not self.isFull(which):
            self.top+=1
            which.append(item)
            self.show_stack(which)
        else:
            print("Stack full")
    def pop(self,which):
        if not self.isEmpty(which):
            self.top-=1
            return which.pop()
        else:
            print("Stack empty")
    
    def eval_postfix(self):
        for sym in self.expr.split():
    
            sym_type=self.getSymtype(sym)
            if sym_type== Sym.OPERAND:
                self.push(int(sym),self.stack1)
            else:
                print(self.stack1[-2],self.stack1[-1],sym)

                op2=self.pop(self.stack1)
                op1=self.pop(self.stack1)
                if sym_type==Sym.PLUS:
                    self.push(op1+op2,self.stack1)
                elif sym_type==Sym.MINUS:
                    self.push(op1-op2,self.stack1)
                elif sym_type==Sym.TIMES:
                    self.push(op1*op2,self.stack1)
                elif sym_type==Sym.DIVIDE:
                    self.push(op1//op2,self.stack1)
                elif sym_type==Sym.MOD:
                    self.push(op1%op2,self.stack1)
        return self.pop(self.stack1)
    
    def infix_postfix(self):
        for token in expr.split():
            if token.isalnum():
                self.output+=(token+' ')
                self.push(token,self.stack1)
            elif token=='(':
                self.push(token,self.stack2)
            elif token==')':
                sym=self.pop(self.stack2)
                while sym!='(':
                    self.output+=(sym+' ')
                    sym=self.pop(self.stack2)
                self.pop(self.stack1)
                self.pop(self.stack1)
            else:
                while not self.isEmpty(self.stack2) and self.precedence(self.stack2[-1])>=self.precedence(token):
                    sym=self.pop(self.stack2)
                    self.pop(self.stack1)
                    self.output+=(sym+' ')
                self.push(token,self.stack2)
        while not self.isEmpty(self.stack2):
            self.output+=(self.pop(self.stack2)+' ')
        print()
    def precedence(self,op):
        if op=='(': return 0
        elif op in ['+','-']: return 1
        elif op in ['*','/','%']:return 2

    def getSymtype(self,sym):
        if sym=='(':sym_type=Sym.OPEN_B
        elif sym==')':sym_type=Sym.CLOSE_B
        elif sym=='+':sym_type=Sym.PLUS
        elif sym=='-':sym_type=Sym.MINUS
        elif sym=='*':sym_type=Sym.TIMES
        elif sym=='/':sym_type=Sym.DIVIDE
        elif sym=='%':sym_type=Sym.MOD
        else: sym_type=Sym.OPERAND
        return sym_type

expr=input("input an infix :")
e=Expression(expr)
print()
e.infix_postfix()
print("postfix : ",e.output)
e.expr=e.output
print()
print("evaluation : ",e.eval_postfix())'''


#수식 변환 평가(4.13)-중위수식>후위수식, 연산자,피연산자 스택 분리, 변화 상태 보이기(다중숫자 구현, 스택 분리는 아직)

'''class Sym:
    OPEN_B=1
    CLOSE_B=2
    PLUS=3
    MINUS=4
    TIMES=5
    DIVIDE=6
    MOD=7
    OPERAND=8
class Expression:
    def __init__(self,expr):
        self.stack=[]
        self.size=100
        self.expr=expr 
        self.top=-1
        self.output=""

    def push(self,item):
        if not self.isFull():
            self.top+=1
            self.stack.append(item)
            self.show_stack()
        else:
            print("Stack full")
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.stack.pop()
        else:
            print("Stack empty")

    def eval_postfix(self):

        for sym in self.expr.split():
            print(sym,end=' ')
            sym_type=self.getSymtype(sym)
            if sym_type==Sym.OPERAND:
                self.push(int(sym))
            else:
                op2=self.pop()
                op1=self.pop()
                if sym_type==Sym.PLUS:
                    self.push(op1+op2)
                elif sym_type==Sym.MINUS:
                    self.push(op1-op2)
                elif sym_type==Sym.DIVIDE:
                    self.push(op1//op2)
                elif sym_type==Sym.MOD:
                    self.push(op1%op2)
                elif sym_type==Sym.TIMES:
                    self.push(op1*op2)
        return self.pop()
        
    def infix_postfix(self):
        for token in expr.split():
            print(token,end=' ')
            if token.isalnum():
                self.output+=(token+' ')
            elif token=='(':
                self.push(token)
            elif token==')':
                sym=self.pop()
                while sym !='(':
                    self.output+=(sym+' ')
                    sym=self.pop()
            else:
                while not self.isEmpty() and self.precedence(self.stack[-1])>=self.precedence(token):
                    sym=self.pop()
                    self.output+=(sym+' ')
                self.push(token)
        while not self.isEmpty():
            self.output+=(self.pop()+' ')
        print()

    def isEmpty(self): 
        return len(self.stack)==0
    
    def isFull(self): 
        return len(self.stack)==self.size
    
    def show_stack(self): 
        print(self.stack)

    def precedence(self,op):
        if op=='(':return 0
        elif op in ['+','-']:return 1
        elif op in ['*','/','%']:return 2

    def getSymtype(self,sym):
        if sym=='(':sym_type=Sym.OPEN_B
        elif sym==')':sym_type=Sym.CLOSE_B
        elif sym=='+':sym_type=Sym.PLUS
        elif sym=='-':sym_type=Sym.MINUS
        elif sym=='*':sym_type=Sym.TIMES
        elif sym=='/':sym_type=Sym.DIVIDE
        elif sym=='%':sym_type=Sym.MOD
        else:
            sym_type=Sym.OPERAND
        return sym_type

expr=input("input an infix=")


e=Expression(expr)
print("중위 수식 : ",expr)
print()
e.infix_postfix()
print("변환 후위 수식 ",e.output)
e.stack=[]
e.expr =e.output
print()
print("후위 수식 계산 값=",e.eval_postfix())
print()'''
       


#수식 변화(4.6,과제아님,숫자 한글자일 경우)

'''class Sym:
    OPEN_B=1
    CLOSE_B=2
    PLUS=3
    MINUS=4
    TIMES=5
    DIVIDE=6
    MOD=7
    OPERAND=8
class Expression:
    def __init__(self,expr):
        self.stack=[]
        self.size=100
        self.expr=expr 
        self.top=-1
        self.output=""
    def push(self,item):
        if not self.isFull():
            self.top+=1
            self.stack.append(item)
            self.show_stack()
        else:
            print("Stack full")
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.stack.pop()
        else:
            print("Stack empty")

    def eval_postfix(self):
        for sym in self.expr:
            print(sym,end=' ')
            sym_type=self.getSymtype(sym)
            if sym_type==Sym.OPERAND:
                self.push(int(sym))
            else:
                op2=self.pop()
                op1=self.pop()
                if sym_type==Sym.PLUS:
                    self.push(op1+op2)
                elif sym_type==Sym.MINUS:
                    self.push(op1-op2)
                elif sym_type==Sym.DIVIDE:
                    self.push(op1//op2)
                elif sym_type==Sym.MOD:
                    self.push(op1%op2)
                elif sym_type==Sym.TIMES:
                    self.push(op1*op2)
        return self.pop()
        
    def infix_postfix(self):
        for token in expr:
            print(token,end=' ')
            if token.isalnum():
                self.output+=token
            elif token=='(':
                self.push(token)
            elif token==')':
                sym=self.pop()
                while sym !='(':
                    self.output+=sym
                    sym=self.pop()
            else:
                while not self.isEmpty() and self.precedence(self.stack[-1])>=self.precedence(token):
                    sym=self.pop()
                    self.output+=sym
                self.push(token)
        while not self.isEmpty():
            self.output+=self.pop()
        print()

    def isEmpty(self): 
        return len(self.stack)==0
    def isFull(self): 
        return len(self.stack)==self.size
    def show_stack(self): 
        print(self.stack)

    def precedence(self,op):
        if op=='(':return 0
        elif op in ['+','-']:return 1
        elif op in ['*','/','%']:return 2

    def getSymtype(self,sym):
        if sym=='(':sym_type=Sym.OPEN_B
        elif sym==')':sym_type=Sym.CLOSE_B
        elif sym=='+':sym_type=Sym.PLUS
        elif sym=='-':sym_type=Sym.MINUS
        elif sym=='*':sym_type=Sym.TIMES
        elif sym=='/':sym_type=Sym.DIVIDE
        elif sym=='%':sym_type=Sym.MOD
        else:sym_type=Sym.OPERAND
        return sym_type
    
for expr in ["5*7+(4-3)/6%9","9/(3+6-5)*7*(6-4)"]:
    e=Expression(expr)
    print("중위 수식 : ",expr)
    print()
    e.infix_postfix()
    print("변환 후위 수식 ",e.output)
    e.stack=[]
    e.expr=e.output
    print()
    print("후위 수식 계산 값=",e.eval_postfix())
    print()'''

#연결리스트(저장본 1)

'''class Node:
    def __init__(self,item):
        self.data=item
        self.rlink=None
        self.llink=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def isEmpty(self):
        return not self.head
    
    def add_rear(self,item):
        node=Node(item)
        if not self.head:
            self.head=node
            self.tail=node
        else:
            self.tail.rlink=node
            node.llink=self.tail
            self.tail=node
            node.rlink=self.head

    def view(self):
        temp=self.head
        print("[",end=' ')
        while True:
            print(temp.data,end=' ')
            temp=temp.rlink
            if temp==self.head:
                break
        print("]",end=' ')
    
    def find(self,item):
        temp=self.head
        while True:
            if temp.data==item: return temp
            temp=temp.rlink
            if temp==self.head: break
        return None
    
    def move(self,item):
        node=self.find(item)
        if not node:
            print("Not found")
            return
        if node:
            node.rlink.data=node.data
            node.data=0

        

lst=LinkedList()
x=int(input("노드 수 입력"))
lst.add_rear(1)
for y in range(x//2):
    lst.add_rear(0)
lst.add_rear(2)
for y in range(x//2):
    lst.add_rear(0)

lst.view()

import random
def Roledice():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    return (dice1,dice2)
def player1():
    a=Roledice()
    if a!=(6,6) and a!=(5,5):
        print(a)
        x=int(a[0]+a[1])
        for i in range(x):
            lst.move(1)
        lst.view()
player1()'''

#연결리스트(저장본 2)

'''class Node:
    def __init__(self,item):
        self.data=item
        self.rlink=None
        self.llink=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def isEmpty(self):
        return not self.head
    
    def add_rear(self,item):
        node=Node(item)
        if not self.head:
            self.head=node
            self.tail=node
        else:
            self.tail.rlink=node
            node.llink=self.tail
            self.tail=node
            node.rlink=self.head

    def view(self):
        temp=self.head
        print("[",end=' ')
        while True:
            print(temp.data,end=' ')
            temp=temp.rlink
            if temp==self.head:
                break
        print("]",end=' ')
    
    def find(self,item):
        temp=self.head
        while True:
            if temp.data==item: return temp
            temp=temp.rlink
            if temp==self.head: break
        return None
    
    def move(self,item):
        import random
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        x=int(dice1+dice2)
        print((dice1,dice2))

        node=self.find(item)
        if not node:
            print("Not found")
            return
        if node:
            if (dice1,dice2)!=((5,5)and(6,6)):
                temp=node.rlink
                for a in range(x-1):

                    newtemp=temp
                    temp=newtemp.rlink
                temp.data=node.data
                node.data=0     

lst=LinkedList()
x=int(input("노드 수 입력"))
lst.add_rear(1)
for y in range(x//2-1):
    lst.add_rear(0)
lst.add_rear(2)
for y in range(x//2-1):
    lst.add_rear(0)

lst.view()

lst.move(1)
lst.move(2)
lst.move(1)
lst.view()'''


#d연결리스트 저장본 3

'''class Node:
    def __init__(self,item):
        self.data=item
        self.rlink=None
        self.llink=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def isEmpty(self):
        return not self.head
    
    def add_rear(self,item):
        node=Node(item)
        if not self.head:
            self.head=node
            self.tail=node
        else:
            self.tail.rlink=node
            node.llink=self.tail
            self.tail=node
            node.rlink=self.head

    def view(self):
        temp=self.head
        print("[",end=' ')
        while True:
            print(temp.data,end=' ')
            temp=temp.rlink
            if temp==self.head:
                break
        print("]",end=' ')
    
    def find(self,item):
        temp=self.head
        while True:
            if temp.data==item: return temp
            temp=temp.rlink
            if temp==self.head: break
        return None
    
    def Move(self,item,num,to):
        node=self.find(item)
        if not node:
            print("Not found")
            return False
        if node:
            if to==1:
                temp=node.rlink
                for a in range(num-1):
                    newtemp=temp
                    temp=newtemp.rlink
                temp.data=node.data
                node.data=0
            elif to==-1:
                temp=node.llink
                for a in range(num-1):
                    newtemp=temp
                    temp=newtemp.llink
                temp.data=node.data

    
    def move(self,item):
        import random
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        x=int(dice1+dice2)
        print(item, (dice1,dice2))

        node=self.find(item)
        if not node:
            print("Not found")
            return False

        if node:
            if (dice1,dice2)!=((5,5)or (6,6)):
                temp=node.rlink
                for a in range(x-1):

                    newtemp=temp
                    temp=newtemp.rlink
                if temp.data==(1 and 2):
                    return False
                else:
                    temp.data=node.data
                    node.data=0


            elif (dice1,dice2)==(5,5):
                temp=node.rlink
                while True:
                    if temp.data==1:
                        temp.data=2
                        node.data=1
                        break
                    elif temp.data==2:
                        temp.data=1
                        node.data=2
                        break
                    else:
                        newtemp=temp
                        temp=newtemp.rlink
                

     

lst=LinkedList()
x=int(input("노드 수 입력"))
lst.add_rear(1)
for y in range(x//2-1):
    lst.add_rear(0)
lst.add_rear(2)
for y in range(x//2-1):
    lst.add_rear(0)

lst.view()

while (lst.move(1) and lst.move(2))==True:
    lst.move(1)
    lst.move(2)
    
lst.view()'''


#저장본 4 

'''class Node:
    def __init__(self,item):
        self.data=item
        self.rlink=None
        self.llink=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def isEmpty(self):
        return not self.head
    
    def add_rear(self,item):
        node=Node(item)
        if not self.head:
            self.head=node
            self.tail=node
        else:
            self.tail.rlink=node
            node.llink=self.tail
            self.tail=node
            node.rlink=self.head

    def view(self):
        temp=self.head
        print("[",end=' ')
        while True:
            print(temp.data,end=' ')
            temp=temp.rlink
            if temp==self.head:
                break
        print("]",end=' ')
    
    def find(self,item):
        temp=self.head
        while True:
            if temp.data==item: return temp
            temp=temp.rlink
            if temp==self.head: break
        return None
    
    def Move(self,item,num,to):
        node=self.find(item)
        if not node:
            print("Not found")
            return False
        
        if node:
            if to==1:
                temp=node.rlink
                for a in range(num-1):
                    newtemp=temp
                    temp=newtemp.rlink
                temp.data=node.data
                node.data=0

            elif to==-1:
                temp=node.llink
                for a in range(num-1):
                    newtemp=temp
                    temp=newtemp.llink
                temp.data=node.data
                node.data=0
     

lst=LinkedList()
x=int(input("노드 수 입력"))
lst.add_rear(1)
for y in range(x//2-1):
    lst.add_rear(0)
lst.add_rear(2)
for y in range(x//2-1):
    lst.add_rear(0)

lst.view()


x=1
while True:
    import random
    num1=random.randint(1,6)
    num2=random.randint(1,6)
    print((num1,num2))

    if (num1,num2)!=((5,5)and(6,6)):
        lst.Move(1,int(num1+num2),x)
        lst.view()

    elif (num1,num2)==(6,6):
        if x==1: x=-1
        elif x==-1:x=1
        lst.view()
    elif num1==5:
        break'''

arr=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]

import numpy as np

newarr=np.array(arr)

print(newarr)

print("첫 원소 : ",newarr[0][0],"\n 마지막 원소 : " ,newarr[4][4])

print(newarr[:2:])
print(newarr[2:5:])
print(newarr[::,::2])
print(newarr[::2, ::2])
print(newarr[:2:].reshape(5,2))




            