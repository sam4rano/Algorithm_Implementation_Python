def reverse_r(string):
    if string == "":   #base case
        return string
    return string[-1] + reverse_r(string[:-1])
string = input('Enter a string')
string_r = reverse_r(string)
print(string_r)