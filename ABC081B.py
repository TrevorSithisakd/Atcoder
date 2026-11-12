n = input()
nums = input().split()
ans = float('inf')
for i in range(0, int(n)):
    num = int(nums[i])
    j = 0
    while num % 2 == 0:
        num = num // 2
        j += 1
    ans = min(ans,j)

print(ans)

# the brute force is to check each number and that would b n 
# for each number  in the input check how many times it can be divided
