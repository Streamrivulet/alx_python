from add_0 import add
if add == __import__('add_0').add:

    a = 1
    b = 2
    add(a, b)

    print("{} + {} = {}" .format(a, b, add(a, b)), end="\n")




