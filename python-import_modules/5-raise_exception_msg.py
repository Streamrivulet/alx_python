def divide(a, b):  
    if b == 0:  
        raise Exception(" Cannot divide by zero. ")  
    return a / b  
try:  
    result = divide(10, 0)  
except Exception as e:  
    print(" An error occurred: ", e)  