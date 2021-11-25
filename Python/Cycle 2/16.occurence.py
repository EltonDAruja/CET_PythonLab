s=input("Enter String : ").split()
tested=list()
for x in s:
    if x not in tested:
        count=0
        for y in s:
            if x==y:
                count+=1
        print(x," : ",count," times")
        tested.append(x)
