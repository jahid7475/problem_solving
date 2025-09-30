t = int(input())

results = []   

for _ in range(t):
    x, y = map(int, input().split())
    low = min(x, y)
    high = max(x, y)
    total = 0
    for i in range(low + 1, high):
        if i % 2 != 0:
            total += i
    results.append(total)   


for ans in results:
    print(ans)
