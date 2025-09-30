n = int(input())     
nums =list (map(int, input().split()))[:n]   
count,count1,count2,count3 = 0,0,0,0

for i in nums:
    if i % 2 ==0:
        count+=1
    elif i % 2==1:
        count1+=1
        

    if 0 < i:
        count2+=1
    elif i < 0:
        count3+=1
        
print(f"Even: {count}\nOdd: {count1}\nPositive: {count2}\nNegative: {count3}")
    

