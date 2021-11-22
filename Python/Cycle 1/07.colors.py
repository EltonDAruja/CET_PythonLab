colorlist1 = input("Enter first list of colours: ").split()
colorlist2 = input("Enter second list of colours: ").split()
for x in colorlist1:
    if x not in colorlist2:
        print(x)