import math
from collections import Counter

string = input()
n = len(string)
n_duplicates = n - len(set(string)) # aabb 2  


# number of unique permutations is? its the Permutation algorithm because order matters in the case of aba it is 3! / 2! number of duplications so it is n!/n_duplicates!
# i need to just count the number of duplicates there are say the 2 a's but how? do i go through the string and the note down the count of each element and then
# for each element i get the count of it and any count that appears more than once i divide it by it like multiple all their facotorials together so i don't even have to ingore 1factorial
# its counts for unique 
count = {}
for char in string:
    if not count[char]:
        count[char] = 1
    else:
        count[char] += 1

for val in count:
    n_duplicates *= math.factorial(val)
res = math.factorial(n)/math.factorial(n_duplicates)
print(res,n,n_duplicates)