a=input("Enter a list : ").split()
b=a
b[0],b[-1]=b[-1],b[0]
print("First List :",a)
print("New swapped List :",b)
