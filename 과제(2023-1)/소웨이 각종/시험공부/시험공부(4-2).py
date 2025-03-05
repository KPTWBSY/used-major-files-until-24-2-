s=int(input())
m=int(input())
d=int(input())
if s>120*60:
    sb=(s-120*60)*1.98
if m>200:
    mb=(m-200)*22
if d>800:
    db=(d-800)*55
print(format(int(sb+mb+db),','),'원')
print(format(int(37400+sb+mb+db),','),'원')
