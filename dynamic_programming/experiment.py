def sort(arr,n):
	buno=max(arr)
	barr=[]
	for i in range(buno+1):
		barr.append([])
	for i in arr:
		barr[(i%10)].append(i)
	for i in barr:
		i.sort()
	newarr=[]
	for i in barr:
		newarr.extend(i)
	return newarr
    	
if __name__ == '__main__':
	arr=[9,8,7,1,2,0,3,6,5,4]
	print(*sort(arr,len(arr)))
	# print(*arr)