def read_file():
    f=open('새파일.txt')
    while True:
        line=f.readline()
        if len(line)==0:
            break
        line=line.strip()
        newmemo.append(line)
    f.close()

def write_file():
    f=open('새파일.txt','w')
    for item in mymemo:
        msg=item+'\n'
        f.write(msg)
    f.close()

mymemo=[]
while True:
    item=input()
    if item=='':
        break
    mymemo.append(item)
write_file()

newmemo=[]

read_file()

finalmemo=[]
for i in newmemo:
    finalmemo.append(int(i))

sum=0
for i in finalmemo:
    sum+=i
average=sum/len(finalmemo)

finalmemo.sort
h=finalmemo[len(finalmemo)-1]

print(average,'\n',h)
