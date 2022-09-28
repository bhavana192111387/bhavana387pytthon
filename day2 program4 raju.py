Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> try:
    n=int(input("Enter the number= "))
    rev=0
    if(n<0):
        print("Negative value")
        exit()
    else:
        while(n!=0):
            d=n%10
            rev=(rev*10)+d
            n//=10
        print("mirror image=",str(rev))
except ValueError:
    print("Alphabets are not allowed")
