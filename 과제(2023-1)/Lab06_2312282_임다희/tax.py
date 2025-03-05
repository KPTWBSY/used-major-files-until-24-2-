def tax(amount):
    if amount>=0 and amount<=1200:
        return int(amount*0.06)
    elif amount>1200 and amount<=4600:
        return int(72+(amount-1200)*0.15)
    elif amount>4600 and amount <=8800:
        return int(582+(amount-4600)*0.24)
    elif amount>8800 and amount<=30000:
        return int(1590+(amount-8800)*0.35)
    else:
        return int(9010+(amount-30000)*0.38)
