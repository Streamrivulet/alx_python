def fibonacci_sequence(n):
    first = 0
    second = 1
    print(first, second, end=" ")

    n -= 2
    
    while n > 0:

        print(first + second, end=" ")

        temp = second
        second = first + second
        first = temp

    
        n -= 1
      
    return [n]


