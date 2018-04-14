from random import randint as random

count = 1

def compare(num):
    buffer = ""
    if (num % 3) == 0:
        buffer += "Fizz"
    if (num % 5) == 0:
        buffer += "Buzz"
    
    return buffer

while count <= 100:
    fb = compare(count)
    if fb == "":
        print (str(count))
    else:
        print(fb)

    count += 1