"""
Alx class task 3
"""
class Square:
    """
    Declaring the class Square
    """
    def __init__(self, size = 0):
       
       """
       Setting the method
       """
       self.__size = size 

    
    @property

    def size(self):

        """
        Added property to retrieve the private size
        """
        return self.__size
       
       
    @size.setter
    def size(self, value):
          """
          Added setter to update the size
          """
          if type(value) is not int:
             raise TypeError("size must be an integer")
          elif value < 0:
             raise ValueError("size must be >= 0")
          else:
            self.__size = value
      

    def area(self):
        """
         Creating another method that calculate and return the area of the square.
        """
        return self.size ** 2
    
    def my_print(self):
        """
        Method that print 
        """
        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                else:
                    print(end="\n")

my_square = Square(3)
my_square.my_print()

