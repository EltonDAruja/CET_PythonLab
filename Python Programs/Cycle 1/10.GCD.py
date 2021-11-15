a,b=input("Enter 2 numbers : ").split()
a=int(a)
b=int(b)
if a > b :
    small=b
else :
    small=a
for x in range(1,small+1):
    if(a % x == 0)and(b % x == 0):
        gcd=x
print("GCD of ",a," and ",b," = ",gcd)
