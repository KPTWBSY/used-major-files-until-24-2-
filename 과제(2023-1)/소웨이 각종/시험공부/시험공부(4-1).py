a=int(input(''))
if a>0 and a<=12000000:
    print(a*0.06)
elif a>12000000 and a<=46000000:
    print(720000+(a-12000000)*0.15)
else:
    print('else')
