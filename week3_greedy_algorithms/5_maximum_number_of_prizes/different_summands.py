# Uses python3
import sys

def optimal_summands(n):
    summands = []
    number = 1
    while n > 0:
        if n in summands:
            summands[-1] += n
            break
        summands.append(number)
        n -= number
        number += 1
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
