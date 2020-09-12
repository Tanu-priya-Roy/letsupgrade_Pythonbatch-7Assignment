def armstrong_number():
	for i in range(1,1001):
		count=0
		n=i
		while n:
			n=n//10
			count+=1
		n=i
		s=0
		while n:
			s=s+(n%10)**count
			n=n//10
		if(i==s):
			yield s


for x in armstrong_number():
	print(x)