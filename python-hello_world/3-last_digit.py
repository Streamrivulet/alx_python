import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
a = "Last digit of"
b = "is"
c = "and is greater than 5"
d = "and is 0"
e = "and is less than 6 and not 0"

f = number%10

if f > 5:
    print(a, number, b, f, c, sep=" ")

if f==5:
    print(a, number, b, f, d, sep=" ")

if f < 6 & f<0:
    print(a, number, b, f, e, sep=" ")