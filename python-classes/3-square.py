"""
Alx task 1,m  on classes and object 
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
        """
        Adding property in order to retrieve private attribute size
        """
        return self.__size
   size.setter

   """
   Adding setter in order to update the size retrieved
   """
   def size(self, value):
       """ 
       #Raising and handling some exceptions
       """
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
        return self.size **2