def factr(n):
    if n == 1:
        return 1
    return n * factr(n-1)
n = int(input('Enter an integer?'))
num = factr(n)
print(num)