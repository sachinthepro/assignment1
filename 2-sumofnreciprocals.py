##program to find sum of n numbers

n=int(input("Enter the value of n: "))
res=0
for i in range(1,n+1): 
    res += 1/i
print(f"{res}")
