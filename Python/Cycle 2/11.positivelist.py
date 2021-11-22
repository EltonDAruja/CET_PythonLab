l = input("Enter list of integers: ").split()
l = list(map(int,l))
pl = [i for i in l if i > 0]
print(pl)