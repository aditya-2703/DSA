# def fibonacci(n):
# 	if n==0:
# 		return 0
# 	if n==1:
# 		return 1
# 	else:
# 		return fibonacci(n-1)+fibonacci(n-2)



# z=fibonacci(5)
# print(z)

def fibonacci(n):
	first=1
	second=1
	for i in range(n):
		first,second=second,first+second
	print(second)
    		







fibonacci(5)
