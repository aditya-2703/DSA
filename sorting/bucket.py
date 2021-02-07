def bucket_sort_float(array):
    bucket=[]
    for i in range(len(array)):
        bucket.append([])

    for i in array:
        key=int(10*i)
        bucket[key].append(i)

    for i in bucket:
        i.sort()
    nl=[]
    for i in bucket:
        nl.extend(i)
    return nl
def bucket_sort_int(array):
    max_element_len=len(str(max(array)))
    bucket=[]
    nl=[]
    for i in range(10):
        bucket.append([])

    for i in array:
        index=len(str(i))
        bucket[index].append(i)
    for i in bucket:
        i.sort()
        nl.extend(i)
    return nl

if __name__ == '__main__':
    array=[0.11,0.22,0.55,0.33,0.21,0.65,0.69]
    # array = [6, 5, 1, 123, 24, 324, 3, 5, 45, 346, 5, 626, 6, 26]
    if type(array[0])==type(12):
        new_array=bucket_sort_int(array)
        print(f"ARRAY BEFORE SORTING : {array}\nARRAY AFTER SORTING :  {new_array}")
    elif type(array[0])==type(0.1221):
        new_array = bucket_sort_float(array)
        print(f"ARRAY BEFORE SORTING : {array}\nARRAY AFTER SORTING :  {new_array}")
# ------------------------------------------------OR---------------------------------------------------------------------------------------------
# def insertion_sort(array):
#     for i in range(1, len(array)):
#         temp = array[i]
#         j = i - 1
#         while j >= 0 and temp < array[j]:
#             array[j + 1] = array[j]
#             j -= 1
#         array[j + 1] = temp
#     return array
#
#
# def bucket_sort(array):
#     bucket = []
#     for i in range(len(array)):
#         bucket.append([])
#     for i in array:
#         key = int(10 * i)
#         bucket[key].append(i)
#     new_list = []
#         # print(bucket)
#     for i in range(len(bucket)):
#         sort_in = insertion_sort(bucket[i])
#         new_list.append(sort_in)
#         i += 1
#     print(new_list)
#
#     nl = []
#     for i in new_list:
#         nl.extend(i)
#
#     return nl
#
#
# if __name__ == '__main__':
#     array = [0.11, 0.22, 0.55, 0.33, 0.21, 0.65, 0.69]
#     new_array = bucket_sort(array)
#     print(f"ARRAY BEFORE SORTING : {array}\nARRAY AFTER SORTING :  {new_array}")
