def factn(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact
n = int(input('enter a number? '))
num = factn(n)
print(num)