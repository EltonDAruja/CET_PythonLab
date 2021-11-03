a,b,c=input("Enter 3 Numbers : ").split()[:3]
a=int(a)
b=int(b)
c=int(c)
if a>c and b:
	print("Largest is : ",a)
elif b>c:
	print("Largest is : ",b)
else:
	print("Largest is : ",c)
