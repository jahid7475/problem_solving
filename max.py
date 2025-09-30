# n=int(input())

# nums = list(map(int,input().split()))[:n]
# maximum_number = max(nums)

# print(maximum_number)

n=int(input())

nums = list(map(int,input().split()))[:n]
max = nums[0]

for i in nums:
    if max < i:
        max = i
print(max)


