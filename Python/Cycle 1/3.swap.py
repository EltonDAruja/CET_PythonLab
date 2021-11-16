a,b=input("Enter a & b : ").split()
a=int(a)
b=int(b)
print("a = {} b = {}".format(a,b))
print("After swap : ")
a=a+b
b=a-b
a=a-b
print("a = {} b = {}".format(a,b))
