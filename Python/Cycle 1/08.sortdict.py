l = input("Enter the list of keys and values : ").split()
d = dict()
for i,x in enumerate(l):
    if i%2==0:
        d[x]=l[i+1]
print("In Ascending order: ",sorted(d))
print("In Descending order: ",sorted(d,reverse=True))
print(d)