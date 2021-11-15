l1=input("Enter 1st list of integers : ").split()
l2=input("Enter 2nd list of integers : ").split()

# list length
if len(l1) == len(l2):
    print("The lists have the same length")
else:
    print("The lists do not have the same length")

# list sum
l1=list(map(int,l1))
l2=list(map(int,l2))
if sum(l1) == sum(l2):
    print("The lists have the same sum")
else:
    print("The lists do not have the same sum")

# occurance
occ=list()
l1=list(map(int,l1))
l2=list(map(int,l2))
for x in l1:
    for y in l2:
        if x==y:
            occ.append(x)
print("List of elements that occur in both lists : ",occ)