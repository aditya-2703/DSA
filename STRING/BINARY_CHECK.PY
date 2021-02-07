# Input:
# str = 101
# Output:
# 1
# Explanation:
# Since string contains only 0 and 1, output is 1.


def Method_1(string):
    for i in string:
        print(type(i),i)
        if i!="0" and i!="1":
            return 0
        else:
            continue
    return 1


if __name__ == '__main__':
    string="0111100110101100"
    print(Method_1(string))