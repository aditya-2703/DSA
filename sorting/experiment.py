# def hourglassSum(arr):
#     i=j=0
#     new=[]
#     while i<6 and j<6:
#         for i in range(3):
#             for j in range(3):
#                 print("arr[{}][{}] = {}".format(i,j,arr[i][j])) 
#             j+=1
#         i+=1      





# arr=[[1, 1, 1, 0, 0, 0],
#      [0, 1, 0, 0, 0, 0],
#      [1, 1, 1, 0, 0, 0],
#      [0, 0, 2, 4, 4, 0],
#      [0, 0, 0, 2, 0, 0],
#      [0, 0, 1, 2, 4, 0]]
# hourglassSum(arr)        
# m=max(size_base10(234),size_base10(234))
# print(m,size_base10(34),type(size_base10(89)))
from datetime import datetime
from time import *
t1="Sun 10 May 2015 13:54:36 -0700"
t2="Sun 10 May 2015 13:54:36 -0000"
fmt = "%a %d %b %Y %H:%M:%S %z"
l1=list(t1)
l2=list(t2)
for i in reversed(range(len(l1)-1)):
    z=abs(datetime.strptime(l1[i],fmt[i]))-abs(datetime.strptime(l2[i],fmt[i]))
    print(z)