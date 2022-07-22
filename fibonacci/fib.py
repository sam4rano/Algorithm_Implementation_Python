# Recursive fibonacci
def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

num_terms = int(input('enter an integer? '))

# check if the number of terms is valid
if num_terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(num_terms):
       print(fib(i))

#result with 10: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34