x,n = map(int, input().split())
s = (x**0-1)
for i in range(2,n+1,2):
    s += x**i

print(s)