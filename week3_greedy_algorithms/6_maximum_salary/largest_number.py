#Uses python3

import sys

def largest_number(a):
    nums = list(map(str, a))
    nums.sort()
    res = ""
    for x in nums:
        res += x
    return res

def IsGreatorOrEqual(digit, maxDigit):
    flag = 0
    if int(str(maxDigit)[0]) > int(str(digit)[0]):
        return False
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
