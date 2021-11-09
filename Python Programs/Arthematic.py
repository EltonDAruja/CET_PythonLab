a,b=input("Enter 2 Numbers : ").split()[:2]
a=int(a)
b=int(b)
o=input("Enter Operator : ")
if o=="+":
	s=a+b
	print("Sum = ",s)
if o=="-":
	d=a-b
	print("Difference = ",d)
elif o=="*":
	p=a*b
	print("Product =",p)
elif o=="/":
	q=a/b
	print("Quotient =",q)
elif o=="%":
	r=a%b
	print("Remainder =",r)
