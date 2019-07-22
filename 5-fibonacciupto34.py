range1=34
n1=0
n2=1
i=2
if range1<= 0:
	print("Enter a positive integer..")
elif range1== 1:
	print (f"Fibonacci series up to {range1} :")
	print(n1)
else:
	print (f"Fibonacci series up to {range1} :")
	print(n1)
	print(n2)
	while i<range1:
		n3=n1+n2
		print(n3)
		n1=n2
		n2=n3
		i=i+1
