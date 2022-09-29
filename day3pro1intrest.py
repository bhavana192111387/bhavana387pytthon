print("enter the principal amount:")
p=int(input())
print("enter the numberof yeras:")
t=float(input())
print("is the customer is senoir citizen:(y/n)")
ch=(input())
if(ch=="y"):
    r=12
else:
        r=10
si=(p*t*r)/100
print(" simple intrest:",si)
