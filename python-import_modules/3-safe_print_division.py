def safe_print_division(a, b):
    try:
        result = a/b
        print("{}/{} = {}" .format(a,b, result)) 

    except: ZeroDivisionError
    print("you cant divide by zero")
    
    finally: 
         print("An error occur")
        
    