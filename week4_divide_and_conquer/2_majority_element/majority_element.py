# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    
    left_elem = get_majority_element(a, left, (left + right - 1) // 2 + 1)
    right_elem = get_majority_element(a, (left + right - 1) // 2 + 1, right)
 
    lcount = 0
    print(a[left:right], left_elem, right_elem, left, right)
    for i in range(left, right):
        if a[i] == left_elem:
            lcount += 1
            print(0, lcount)
    if lcount > (right - left) // 2:
        print(1)
        return left_elem

    rcount = 0
    for i in range(left, right):
        if a[i] == right_elem:
            rcount += 1
            print(2, rcount)

    if rcount > (right - left) // 2:
        print(11, "\n")
        return right_elem

    return -1
 
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)