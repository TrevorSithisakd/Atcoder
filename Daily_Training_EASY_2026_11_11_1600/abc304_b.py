n = int(input())
k = max(0,len(str(n))-3)
print(n // 10**k * 10**k)