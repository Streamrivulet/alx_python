def fibonacci_sequence(n):
    first[0]=0

    second[1]=[1]

    print(first, second, end=" ")

    n -= 2
    
    while n > 0:
        second[n]={ first[-2] + second[-1]} 

        temp = second
        second = first + second
        first = temp

        print(first[n] + second[n], end=" ")
    
        n -= 1
      
        return [n]


