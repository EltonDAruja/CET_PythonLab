l=input("Enter list of integers : ").split()
l=map(int,l)
l=list(l)
for i,x in enumerate(l):
    if int(x) > 100:
        l[i]="over"
print("New list : ",l)