##program to find sum of n numbers

n=int(input("Enter the value of n: "))
res=0
for i in range(2,n+1): 
    res += 1/(i**3)
print(f"{res}")
