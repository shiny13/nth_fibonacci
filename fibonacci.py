#use python3
import sys

def getNthFib(n):
    # Write your code here.
    if n == 2:
        return 1
    elif n == 1:
        return 0

    previous = 0
    current  = 1

    for _ in range(n-2):
        previous, current = current, previous + current

    return current

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(getNthFib(n))