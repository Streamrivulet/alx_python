"""
Alx task 3 on classes and object 
"""

"""
Delaring the class
"""
class Square:
   """
   
   Delaring the class
   
   """
   
   def __init__(self, size = 0):
       self.__size = size

   @property
  
   def size(self):
        return self.__size
   size.setter
   def size(self, value):
       if type(value) is not int:
           raise TypeError("size must be an integer")
       elif value < 0:
           raise ValueError("size must be >= 0")
       else:
           self.__size = value

   def area(self):
        """
         #Creating another method that calculate and return the area of the square.
        """
        return self.size*self.size


   
   



    
   
   """
   Delaring the class
   """
  """ def __init__(self, size = 0): #Assigned a default value to size
      
      """
      #Raising and handling some exceptions
      """
      if type(size) is not int:
         raise TypeError("size must be an integer")
      elif size < 0:
         raise ValueError("size must be >= 0")
      else:
        self.__size = size

   def area(self):
        """
         #Creating another method that calculate and return the area of the square.
        """
        return self.__size*self.__size
