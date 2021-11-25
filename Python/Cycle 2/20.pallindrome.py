num = input("Enter a Number : ")
num = int(num)
new = 0
check = num
while num>0 :
    r = num % 10
    new = new * 10 + r
    num = int(num / 10)
if new == check:
    print(check,"is Pallindrome")
else:
    print(check,"is not a Pallindrome")
