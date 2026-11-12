n = input()

if n % 2 == 0:
    i = n // 2 -1
else:
    i = n // 2

ans = ""
for j in range(0, i):
    ans = ans + "-"
ans = ans + "#"


