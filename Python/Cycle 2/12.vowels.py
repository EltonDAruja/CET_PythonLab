vowels = list("aeiou")
l = input("Enter word: ")
l = list(l)
vow = [i for i in l if i in vowels]
print(vow)