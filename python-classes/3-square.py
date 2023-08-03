"""
Alx task 1 on classes and object 
"""

"""
Delaring the class
"""
class Square:
   """
   Delaring the class
   """
   def __init__(self, size = 0): #Assigned a default value to size
      
      """
      Raising and handling some exceptions
      """
      if type(size) is not int:
         raise TypeError("size must be an integer")
      elif size < 0:
         raise ValueError("size must be >= 0")
      else:
        self.__size = size

   def area(self):
        """
         Creating another method that calculate and return the area of the square.
        """
        return self.__size*self.__size
    
    