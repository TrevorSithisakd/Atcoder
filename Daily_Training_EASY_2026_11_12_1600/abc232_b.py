# caesar cipher conver the alphabet to bounds
# lower case letters already so like it is a - z and what are the numbers for these and how to convert them to the base alphabet again it was like z - a
# how to shfit above it is easy to multiply once it goes over you need the remainder of the number div by 26 so that is // 

s = input()
t = input()

for char in s:
    if ord(char) - ord("a") + int(t) <= 26:
        # fine for the shift probably
        print(chr(ord(char) + int(t)))
    else:
        # divide the remaining result by 26
        rem = (ord(char) - ord("a") + int(t)) // 2
        print(chr(rem))


# this was not the actual problem the actual problem was just subtracting the two strings and making sure they all had the same differences