def fibonacci(inputFunc):
	def inner():
		start,end=inputFunc()
		lst =[0,1]
		i=1
		while(i<=end):
			if(i>=start):
				print(lst[i])
			lst.append(lst[-1]+lst[-2])
			i+=1
	return inner	

@fibonacci
def inputFunc():
	return int(input()),int(input())

inputFunc()