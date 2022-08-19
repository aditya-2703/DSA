# Gray Code

# https://nados.io/question/gray-code?zen=true
# 1. The gray code is a binary numeral system where two successive numbers differ in only one bit.
# 2. Given a non-negative integer n representing the total number of bits in the code, print the 
#      sequence of gray code. A gray code sequence must begin with 0.
 
#  Example:
#  Input: 2
#  Output: [0,1,3,2]
#  Explanation:
#  00 - 0
#  01 - 1
#  11 - 3
#  10 - 2
#  [0,2,3,1] is also a valid gray code sequence.
#  00 - 0
#  10 - 2
#  11 - 3
#  01 - 1


def get_solution(n):
    # if n==1 then there is if 0 or 1
    if n==1:
        return ["0","1"]
    # call which give us the n-1 
    arr = get_solution(n-1)

    result = []
    # take all prev element and append 0 before it 
    for i in arr:
        result.append("0"+i)
    # take all prev in reverse order add 1 before it
    # the reason because of we iterate reverse is the grey bit is also define as only one bit difference among two consicutive bits
    # for 0 1
    # add 0 before 00 01
    # add 1 before 10 11 but here from 01 to 10 there is two  bit change so we take reverse
    # add 1 reverse order 11 10 so now 01 to 11 only one bit difference 
    for i in arr[::-1]:
        result.append("1"+i)
    return result

if __name__ == '__main__':
    n = 3
    ans = get_solution(n)
    for i in range(len(ans)):
        ans[i] = int(ans[i],2)
    print(ans)