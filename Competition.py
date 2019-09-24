result = ""
file = open ("text.txt")
alphabet = " abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
for line in file:
    num = 0
    for c in line:
        if c in vowels:
            num = num+1
    result = result + alphabet[num]
print (result)