import time

def prime1():
    global upper
    t1=time.time()
    num=[]
    for i in range(2,upper+1):
        prime=True
        if i==2:
            prime=True
        else:
            for j in range(2,i):
                if i%j==0:
                    prime=False
                    break
        if prime==True:
            num.append(i)
    t2=time.time()
    print('elapsed time=',t2-t1)
    print('#of primes=',len(num))
    print(num)

def prime2():
    global upper
    t1=time.time()
    num=[]
    for i in range(2,upper+1):
        num.append(i)
    for i in range(2,upper+1):
        for j in range(2,upper+1):
            s=i*j
            if s in num:
                num.remove(s)
            if s>upper:
                break
    t2=time.time()
    print('elapsed time=',t2-t1)
    print('#of primes=',len(num))
    print(num)

upper=100
prime1()
prime2()
