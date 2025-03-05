def total(list):
    while True:
        if not list:
            return False
        else:
            return list[0]+total(list[1:])


list=[1,2,3,4,5,6,7,8,9,10]
print(total(list))
