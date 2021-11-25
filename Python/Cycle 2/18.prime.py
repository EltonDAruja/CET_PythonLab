num = input("Enter a Number : ")
num = int(num)
flag = -1

for i in range(2,int(num/2)):
    if num % i == 0:
        flag=0
if flag == -1:
    print(num,"is Prime")
else:
    print(num,"is not Prime")