import cmath
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
d=(b**2-4*a*c)
x=(-b+cmath.sqrt(d))/(2*a)
y=(-b-cmath.sqrt(d))/(2*a)
print('the roots are:',x,'or',y,)
q1=a*x*x+b*x+c
q2=a*y*y+b*y+c
print('quadratic equation:',q1,'or',q2,)
