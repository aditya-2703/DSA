# Input: N = 6 
# arr[] = [0900  0940 0950  1100 1500 1800]
# dep[] = [0910 1200 1120 1130 1900 2000]
# Output: 3
# Explanation: 
# Minimum 3 platforms are required to 
# safely arrive and depart all trains.


def Method_1(arrival,departure):
    arrival.sort()
    departure.sort()
    max_platform=1
    needed_platform=1
    i=1
    j=0
    n=len(arrival)  
    while i<n and j<n:
        if arrival[i]<=departure[j]:
            max_platform+=1
            i+=1
        elif arrival[i]>departure[j]:
            max_platform-=1
            j+=1
        if max_platform >needed_platform:
            needed_platform=max_platform
    print(needed_platform)


if __name__ == '__main__':
    arrival=[900,940,950,1100,1500,1800]
    departure=[910,1200,1120,1130,1900,2000]
    Method_1(arrival,departure)