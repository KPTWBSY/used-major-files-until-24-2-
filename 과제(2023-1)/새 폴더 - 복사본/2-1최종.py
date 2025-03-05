price=float(input(" 음식 가격 : "))
tax=price*0.105
tip=price*0.15
total=tax+tip+price
print(" 세금 : %.2f \n 팁 : %.2f \n 지불 총액 : %.2f"%(tax,tip,total))

    
