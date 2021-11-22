d = input("Enter elements of dictionary 1 : ").split()
d1 = dict()
for i,x in enumerate(d):
    if i%2==0:
        d1[x]=d[i+1]
d = input("Enter elements of dictionary 2 : ").split()
d2 = dict()
for i,x in enumerate(d):
    if i%2==0:
        d2[x]=d[i+1]
# for key in d2:
#    d1[key]=d2[key]
d2.update(d1)
print("Merged dictionary is: ")
print(d2)