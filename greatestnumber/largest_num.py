#greatest number among three
#steps
num1 = int(input('enter number 1? '))
num2 = int(input('enter number 2? '))
num3 = int(input('enter number 3? '))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)