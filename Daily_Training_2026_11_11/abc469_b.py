# conditions 
# x either ox or -x either xo or x-
# all of the above conditions so its -xx or xxx or xx-
# findind the subsequence of the chairs
n = int(input())
s = input()

# use a sliding window with indexes? foward and back with size of 3 the window 
# how would the window work? we start with back and front = 0 and then front ++ until the distance between back or we do just 3 and check for special cases seperately
ans = 0
if s[0] == "x" and s[1] == "x":
    ans += 1
if s[n- 1] == "x" and s[n -2] == "x":
    ans += 1

back, front = 0, 2
for front in range(2, n):
    if s[back] == "x" and s[back + 1] == "x" and s[front] == "x":
        ans += 1
    front += 1
    back += 1

print(ans)
        
