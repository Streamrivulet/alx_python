import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
a = "Last digit of"
b = "is"
c = "and is greater than 5"
d = "and is 0"
e = "and is less than 6 and not 0"
f = number%10

if number%10 > 5:
    print(a, number,  b, f, c, sep=" ")
if number%10 == 0:
    print(a, number, b, f, d, sep=" ")
if number%10 < 6 & number%10 != 0:
    print(a, number, b, f, e, sep=" ")
