a=input("Enter Year : ")
a=int(a)
if a%100==0:
	if a%400==0:
		print("It is a Leap Year")
	else:
		print("It is not a Leap Year")
else:
	if a%4==0:
		print("It is a Leap Year")
	else:
		print("It is not a Leap Year")
