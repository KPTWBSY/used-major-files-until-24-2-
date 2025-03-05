s=input('입력')
my_list=list(s)
x=[]
y=[]
x.append(my_list[0])
y.append(0)
for i in range(1,len(my_list)+1):
    if my_list[i] in x:
        y.append(1)
    
    
print(y)
