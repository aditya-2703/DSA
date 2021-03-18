from math import *
def bin_to_dec(binary):
    binary=str(binary)
    l=len(binary)-1
    result=0
    for i in range(l,-1,-1):
        result+=pow(2,l-i)*int(binary[i])
    return result
def dec_to_bin(number,arr):
    if number>=1:
        dec_to_bin(number//2,arr)
    arr.append(str(number%2))
def get_add(b1,b2):
  
    maxlen=max(len(b1),len(b2))
    b1=b1.zfill(maxlen)
    b2=b2.zfill(maxlen)
    
    carry=0
    result=""
    
    
    for i in range(maxlen-1,-1,-1):
        
        r = carry 
        r += 1 if b1[i] == '1' else 0
        r += 1 if b2[i] == '1' else 0
        result += ('1' if r % 2 == 1 else '0')  
    
     # Compute the carry. 
        carry = 0 if r < 2 else 1
  
    if carry != 0: 
        result = '1' + result 
    return result
def get_sub(b1,b2):
    b2=list(b2)
    for i in range(len(b2)):
        if b2[i]=="0":
            b2[i]="1"
        else:
            b2[i]="0"
    b2="".join(b2)
    b2=get_add(b2,"1")
    result=get_add(b1,b2)
    return result
def get_or(num1,num2):
    return num1|num2
def get_and(num1,num2):
    return num1&num2
def get_xor(num1,num2):
    return num1^num2
def get_not(num1):
    return ~num1
def get_rightshift(number):
    return number>>1
def get_leftshift(number):
    return number<<1
def is_even(number):
    if number&1:
        return False
    return True
def swap():
    global A,B
    A=A^B
    B=A^B
    A=A^B


if __name__ == '__main__':
    print("BINARY OF 15 IS ",end="")
    arr=[]
    dec_to_bin(15,arr)
    bin_val="".join(arr)

    print(f"DECIMAL VALUE OF 10001001 IS {bin_to_dec(11001)}")

    print(f"2 OR 5 IS {get_or(2,5)}")

    print(f"2 AND 5 IS {get_and(2,5)}")

    print(f"2 XOR 5 IS {get_xor(2,5)}")

    print(f"1 NOT IS {get_not(1)}")

    print(f"RIGHT SHIFT OF 45 IS {get_rightshift(45)}")

    print(f"LEFT SHIFT OF 45 IS {get_leftshift(45)}")

    print(f"NUMBER 37 IS EVEN") if is_even(37) else print(f"NUMBER 37 IS ODD")

    A=13
    B=15
    print(f"AFTER SWAPPING A:13 B:15 BECOMES ",end="")
    swap()
    print(f"A:{A} B:{B}")

    arr=[]
    dec_to_bin(8,arr)
    b1="".join(arr)
    arr=[]
    dec_to_bin(6,arr)
    b2="".join(arr)
    print(f"ADDITION OF {b1} AND {b2} IN BINARY IS {get_add(b1,b2)}")
    
    print(f"SUBTRACTION OF {b1} AND {b2} IN BINARY IS {get_sub(b1,b2)}")
    