

def no_of_argu(*args):

	# using len() method in args to count
    x= list(args)
    print(x)
    for a,b in enumerate(x):
        print(a +1,': ', b)


print(no_of_argu(2, 5, 4))

# print(no_of_argu(4, 5, 6, 5, 4, 4))
# print(no_of_argu(3, 2, 32, 4, 4, 52, 1))
# print(no_of_argu(1))
