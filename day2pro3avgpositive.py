pn=0
pnn=0
nn=0
nnn=0
arr=[]
tot=0
print("Enter -1 TO EXIT")
while(arr!=-1):
    arr=int(input("Enter the elements= "))
    if(arr==0):
        print("Neither positive nor negative")
    elif(arr>0):
        pn=pn+arr
        pnn+=1
        avg=pn/pnn
    else:
        nn=nn+arr
        nnn+=1
        avgn=nn/nnn
        
print("Average of positive numbers=",avg)
print("Average of negative numbers= ",avgn)
