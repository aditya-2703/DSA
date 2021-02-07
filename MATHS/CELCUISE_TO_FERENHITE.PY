# Input:
# C = 32
# Output: 89
# Explanation: Using the conversion 
# formula of celsius to farhenheit , it
# can be calculated that, for 32 degree
# C, the temperature in Fahrenheit = 89.
# c to f =(0°C × 9/5) + 32 


# TAKES 0(1) TIME AND SPACE COMPLEXITY
def c_to_f(temp):
    f_temp=int(temp*(9/5))+32
    return f_temp

if __name__ == '__main__':
    print(c_to_f(32))
    