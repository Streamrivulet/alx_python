import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
Last = number % 10

if number < 0:
    Last = -Last

print("Last digit of", number, "is", Last, end=" ")

if Last > 5:
    print("and is greater than 5")
elif Last == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

