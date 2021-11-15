l1=input("Enter a list of integers : ").split()
l1=list(map(int,l1))
l2=list()
for x in l1:
    if x % 2 != 0:
        l2.append(x)
print("After removing even numbers : ",l2)